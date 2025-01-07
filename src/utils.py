import os
import json
import torch
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def load_data(data_path):
    with open(data_path, 'r') as f:
        data = json.load(f)
    return data

def preprocess_data(data, tokenizer, max_length=512):
    inputs = tokenizer(data, padding=True, truncation=True, max_length=max_length, return_tensors="pt")
    return inputs

def split_data(data, test_size=0.2):
    train_data, test_data = train_test_split(data, test_size=test_size)
    return train_data, test_data

def evaluate_model(model, tokenizer, data, labels):
    model.eval()
    inputs = tokenizer(data, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=-1)
    accuracy = accuracy_score(labels, predictions)
    return accuracy

def save_model(model, tokenizer, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)
