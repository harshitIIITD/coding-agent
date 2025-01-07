import os
import requests
import zipfile
import json

def download_dataset(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(response.content)

def extract_dataset(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def prepare_dataset(raw_data_path, prepared_data_path):
    with open(raw_data_path, 'r') as f:
        raw_data = json.load(f)

    prepared_data = []
    for entry in raw_data:
        prepared_entry = {
            "input": entry["input"],
            "output": entry["output"]
        }
        prepared_data.append(prepared_entry)

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
