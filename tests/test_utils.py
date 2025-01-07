import unittest
from src.utils import load_data, preprocess_data, split_data, evaluate_model, save_model
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import os
import json

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.data_path = "test_data.json"
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        self.model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")
        self.data = ["This is a test sentence.", "Another test sentence."]
        self.labels = [0, 1]
        self.max_length = 512

        # Create a test data file
        with open(self.data_path, 'w') as f:
            json.dump(self.data, f)

    def tearDown(self):
        if os.path.exists(self.data_path):
            os.remove(self.data_path)

    def test_load_data(self):
        data = load_data(self.data_path)
        self.assertEqual(data, self.data)

    def test_preprocess_data(self):
        inputs = preprocess_data(self.data, self.tokenizer, self.max_length)
        self.assertIn("input_ids", inputs)
        self.assertIn("attention_mask", inputs)
        self.assertEqual(inputs["input_ids"].shape[1], self.max_length)

    def test_split_data(self):
        train_data, test_data = split_data(self.data, test_size=0.5)
        self.assertEqual(len(train_data), 1)
        self.assertEqual(len(test_data), 1)

    def test_evaluate_model(self):
        accuracy = evaluate_model(self.model, self.tokenizer, self.data, self.labels)
        self.assertIsInstance(accuracy, float)

    def test_save_model(self):
        output_dir = "test_model"
        save_model(self.model, self.tokenizer, output_dir)
        self.assertTrue(os.path.exists(output_dir))
        self.assertTrue(os.path.exists(os.path.join(output_dir, "config.json")))
        self.assertTrue(os.path.exists(os.path.join(output_dir, "pytorch_model.bin")))
        self.assertTrue(os.path.exists(os.path.join(output_dir, "vocab.txt")))

        # Clean up
        if os.path.exists(output_dir):
            for file in os.listdir(output_dir):
                os.remove(os.path.join(output_dir, file))
            os.rmdir(output_dir)

if __name__ == "__main__":
    unittest.main()
