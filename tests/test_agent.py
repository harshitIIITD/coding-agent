import unittest
from src.agent import CodingAIAgent

class TestCodingAIAgent(unittest.TestCase):

    def setUp(self):
        self.agent = CodingAIAgent()

    def test_load_model(self):
        self.agent.load_model()
        self.assertIsNotNone(self.agent.model)

    def test_fine_tune(self):
        # Mock training data
        train_data = [{"input_ids": [0, 1, 2], "labels": [0, 1, 2]}]
        self.agent.fine_tune(train_data)
        self.assertTrue(self.agent.model is not None)

    def test_generate_code(self):
        prompt = "def hello_world():"
        generated_code = self.agent.generate_code(prompt)
        self.assertIn("hello_world", generated_code)

if __name__ == "__main__":
    unittest.main()
