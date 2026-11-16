import Foundation
import Vision
import AppKit
import PDFKit

let pdfUrl = URL(fileURLWithPath: "Revised Exam Timetable Nov. - Dec., 2026.pdf")
guard let pdfDoc = PDFDocument(url: pdfUrl) else {
    print("Failed to open PDF")
    exit(1)
}

print("Total pages: \(pdfDoc.pageCount)")

for pageIndex in 0..<pdfDoc.pageCount {
    guard let page = pdfDoc.page(at: pageIndex) else { continue }
    let pageRect = page.bounds(for: .mediaBox)
    
    // Render page to image
    let image = NSImage(size: pageRect.size)
    image.lockFocus()
    if let context = NSGraphicsContext.current?.cgContext {
        context.setFillColor(NSColor.white.cgColor)
        context.fill(pageRect)
        page.draw(with: .mediaBox, to: context)
    }
    image.unlockFocus()
    
    guard let tiffData = image.tiffRepresentation,
          let bitmap = NSBitmapImageRep(data: tiffData),
          let cgImage = bitmap.cgImage else {
        continue
    }
    
    let requestHandler = VNImageRequestHandler(cgImage: cgImage, options: [:])
    let request = VNRecognizeTextRequest()
    request.recognitionLevel = .accurate
    request.usesLanguageCorrection = false
    
    do {
        try requestHandler.perform([request])
        guard let observations = request.results else { continue }
        
        print("\n================== PAGE \(pageIndex + 1) ==================")
        let recognizedStrings = observations.compactMap { observation in
            observation.topCandidates(1).first?.string
        }
        print(recognizedStrings.joined(separator: "\n"))
    } catch {
        print("Failed to perform OCR: \(error)")
    }
}
