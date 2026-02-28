import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Unit tests for the emotion_detector function."""

    def test_emotions(self):
        # Test for positive / joy emotion
        self.assertEqual(emotion_detector("I am very happy today")["emotion"], "joy")

        # Test for sadness
        self.assertEqual(emotion_detector("I am very sad and depressed")["emotion"], "sadness")

        # Test for fear
        self.assertEqual(emotion_detector("I am terrified of the dark")["emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
