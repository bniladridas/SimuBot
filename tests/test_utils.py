import unittest
from src.utils import preprocess_image

class TestUtils(unittest.TestCase):
    def test_preprocess_image(self):
        import numpy as np
        image = np.zeros((100, 100, 3), dtype=np.uint8)
        processed = preprocess_image(image)
        self.assertEqual(processed.shape, (224, 224, 3))

if __name__ == "__main__":
    unittest.main()