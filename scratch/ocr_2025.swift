import Foundation
import Vision
import AppKit

let files = [
    "geotech-2/WhatsApp Image 2026-11-15 at 22.40.06.jpeg",
    "geotech-2/WhatsApp Image 2026-11-15 at 22.40.07.jpeg",
    "geotech-2/WhatsApp Image 2026-11-15 at 22.40.08.jpeg"
]

for file in files {
    print("\n================== FILE: \(file) ==================")
    let url = URL(fileURLWithPath: file)
    guard let image = NSImage(contentsOf: url) else {
        print("Failed to load \(file)")
        continue
    }
    
    guard let tiffData = image.tiffRepresentation,
          let bitmap = NSBitmapImageRep(data: tiffData),
          let cgImage = bitmap.cgImage else {
        print("Failed to get CGImage for \(file)")
        continue
    }
    
    let requestHandler = VNImageRequestHandler(cgImage: cgImage, options: [:])
    let request = VNRecognizeTextRequest()
    request.recognitionLevel = .accurate
    request.usesLanguageCorrection = true
    
    do {
        try requestHandler.perform([request])
        guard let observations = request.results else {
            print("No text recognized")
            continue
        }
        
        let recognizedStrings = observations.compactMap { observation in
            observation.topCandidates(1).first?.string
        }
        print(recognizedStrings.joined(separator: "\n"))
    } catch {
        print("Failed OCR: \(error)")
    }
}
