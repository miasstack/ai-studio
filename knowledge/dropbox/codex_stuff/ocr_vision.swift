import Foundation
import Vision
import AppKit

let args = CommandLine.arguments.dropFirst()
guard args.count >= 2 else {
    fputs("usage: ocr_vision.swift OUTPUT.txt IMAGE...\n", stderr)
    exit(2)
}

let output = String(args.first!)
let imagePaths = args.dropFirst().map(String.init)
var finalText = ""

for path in imagePaths {
    let url = URL(fileURLWithPath: path)
    guard let image = NSImage(contentsOf: url),
          let tiff = image.tiffRepresentation,
          let bitmap = NSBitmapImageRep(data: tiff),
          let cgImage = bitmap.cgImage else {
        finalText += "\n\n===== \(url.lastPathComponent) =====\n[image load failed]\n"
        continue
    }

    let request = VNRecognizeTextRequest()
    request.recognitionLevel = .accurate
    request.usesLanguageCorrection = true
    request.recognitionLanguages = ["en-US"]

    let handler = VNImageRequestHandler(cgImage: cgImage, options: [:])
    do {
        try handler.perform([request])
        let observations = request.results ?? []
        let lines = observations.compactMap { $0.topCandidates(1).first?.string }
        finalText += "\n\n===== \(url.lastPathComponent) =====\n"
        finalText += lines.joined(separator: "\n")
    } catch {
        finalText += "\n\n===== \(url.lastPathComponent) =====\n[ocr failed: \(error)]\n"
    }
}

do {
    try finalText.write(toFile: output, atomically: true, encoding: .utf8)
} catch {
    fputs("write failed: \(error)\n", stderr)
    exit(1)
}
