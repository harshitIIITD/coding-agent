import os
import requests
import zipfile
import json
import random
from transformers import pipeline

def download_dataset(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(response.content)

def extract_dataset(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def paraphrase_text(text, paraphraser):
    paraphrases = paraphraser(text, num_return_sequences=1)
    return paraphrases[0]['generated_text']

def obfuscate_code(code):
    # Simple obfuscation by replacing variable names
    obfuscated_code = code.replace("a", "x").replace("b", "y").replace("c", "z")
    return obfuscated_code

def transform_code(code):
    # Simple transformation by reversing the code string
    transformed_code = code[::-1]
    return transformed_code

def prepare_dataset(raw_data_path, prepared_data_path):
    with open(raw_data_path, 'r') as f:
        raw_data = json.load(f)

    paraphraser = pipeline("text2text-generation", model="t5-small")

    prepared_data = []
    for entry in raw_data:
        prepared_entry = {
            "input": entry["input"],
            "output": entry["output"]
        }
        prepared_data.append(prepared_entry)

        # Apply data augmentation techniques
        paraphrased_input = paraphrase_text(entry["input"], paraphraser)
        obfuscated_output = obfuscate_code(entry["output"])
        transformed_output = transform_code(entry["output"])

        prepared_data.append({"input": paraphrased_input, "output": entry["output"]})
        prepared_data.append({"input": entry["input"], "output": obfuscated_output})
        prepared_data.append({"input": entry["input"], "output": transformed_output})

    with open(prepared_data_path, 'w') as f:
        json.dump(prepared_data, f, indent=4)

def main():
    dataset_url = "https://example.com/dataset.zip"
    zip_path = "data/dataset.zip"
    extract_to = "data/raw_dataset"
    raw_data_path = os.path.join(extract_to, "raw_data.json")
    prepared_data_path = "data/train_data.json"

    download_dataset(dataset_url, zip_path)
    extract_dataset(zip_path, extract_to)
    prepare_dataset(raw_data_path, prepared_data_path)

if __name__ == "__main__":
    main()
