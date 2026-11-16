import Foundation
import Vision
import AppKit

func processImage(path: String) {
    print("\n================== FULL OCR: \(path) ==================")
    let url = URL(fileURLWithPath: path)
    guard let image = NSImage(contentsOf: url),
          let tiffData = image.tiffRepresentation,
          let bitmap = NSBitmapImageRep(data: tiffData),
          let cgImage = bitmap.cgImage else {
        print("Error loading image")
        return
    }
    
    let requestHandler = VNImageRequestHandler(cgImage: cgImage, options: [:])
    let request = VNRecognizeTextRequest()
    request.recognitionLevel = .accurate
    request.usesLanguageCorrection = false // preserve exact characters
    
    try? requestHandler.perform([request])
    guard let observations = request.results else { return }
    
    // Sort by y descending (top to bottom), then x ascending (left to right)
    // Note: VN boundingBox has y=0 at bottom, y=1 at top
    let sorted = observations.sorted { (a, b) -> Bool in
        if abs(a.boundingBox.origin.y - b.boundingBox.origin.y) > 0.015 {
            return a.boundingBox.origin.y > b.boundingBox.origin.y
        }
        return a.boundingBox.origin.x < b.boundingBox.origin.x
    }
    
    for obs in sorted {
        let b = obs.boundingBox
        if let str = obs.topCandidates(1).first?.string {
            print(String(format: "x:%.2f y:%.2f w:%.2f h:%.2f | %@", b.origin.x, b.origin.y, b.size.width, b.size.height, str))
        }
    }
}

processImage(path: "geotech-2/WhatsApp Image 2026-11-15 at 22.40.06.jpeg")
