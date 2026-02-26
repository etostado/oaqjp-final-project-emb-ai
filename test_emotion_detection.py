from EmotionDetection import emotion_detector

def run_tests():
    test_cases = [
        ("I am glad this happened", "joy"),
        ("I am really mad about this", "anger"),
        ("I feel disgusted just hearing about this", "disgust"),
        ("I am so sad about this", "sadness"),
        ("I am really afraid that this will happen", "fear"),
    ]

    for text, expected_dominant in test_cases:
        result = emotion_detector(text)
        dominant = result.get("dominant_emotion")

        assert dominant == expected_dominant, (
            f"FAILED for: '{text}' | expected: '{expected_dominant}' | got: '{dominant}' | full result: {result}"
        )

    print("All unit tests passed!")


if __name__ == "__main__":
    run_tests()
