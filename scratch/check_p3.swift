import Foundation
import Vision
import AppKit

let file = "geotech-2/WhatsApp Image 2026-11-15 at 22.40.08.jpeg"
let url = URL(fileURLWithPath: file)
guard let image = NSImage(contentsOf: url),
      let tiffData = image.tiffRepresentation,
      let bitmap = NSBitmapImageRep(data: tiffData),
      let cgImage = bitmap.cgImage else {
    exit(1)
}

let requestHandler = VNImageRequestHandler(cgImage: cgImage, options: [:])
let request = VNRecognizeTextRequest()
request.recognitionLevel = .accurate

try? requestHandler.perform([request])
guard let observations = request.results else { exit(0) }

for obs in observations {
    let bbox = obs.boundingBox
    if let str = obs.topCandidates(1).first?.string {
        // print y coordinate (normalized 0 to 1 from bottom to top)
        print(String(format: "y: %.3f - %@", bbox.origin.y, str))
    }
}
