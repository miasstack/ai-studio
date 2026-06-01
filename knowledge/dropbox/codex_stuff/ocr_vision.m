#import <Foundation/Foundation.h>
#import <AppKit/AppKit.h>
#import <Vision/Vision.h>

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        if (argc < 3) {
            fprintf(stderr, "usage: ocr_vision OUTPUT.txt IMAGE...\n");
            return 2;
        }

        NSMutableString *finalText = [NSMutableString string];

        for (int i = 2; i < argc; i++) {
            NSString *path = [NSString stringWithUTF8String:argv[i]];
            NSURL *url = [NSURL fileURLWithPath:path];
            [finalText appendFormat:@"\n\n===== %@ =====\n", [url lastPathComponent]];

            VNRecognizeTextRequest *request = [[VNRecognizeTextRequest alloc] init];
            request.recognitionLevel = VNRequestTextRecognitionLevelAccurate;
            request.usesLanguageCorrection = YES;
            request.recognitionLanguages = @[@"en-US"];

            VNImageRequestHandler *handler = [[VNImageRequestHandler alloc] initWithURL:url options:@{}];
            NSError *error = nil;
            BOOL ok = [handler performRequests:@[request] error:&error];
            if (!ok) {
                [finalText appendFormat:@"[ocr failed: %@]\n", error ?: @"unknown"];
                continue;
            }

            for (VNRecognizedTextObservation *observation in request.results) {
                VNRecognizedText *candidate = [[observation topCandidates:1] firstObject];
                if (candidate != nil) {
                    [finalText appendFormat:@"%@\n", candidate.string];
                }
            }
        }

        NSString *outPath = [NSString stringWithUTF8String:argv[1]];
        NSError *writeError = nil;
        BOOL wrote = [finalText writeToFile:outPath atomically:YES encoding:NSUTF8StringEncoding error:&writeError];
        if (!wrote) {
            fprintf(stderr, "write failed: %s\n", [[writeError localizedDescription] UTF8String]);
            return 1;
        }
    }
    return 0;
}
