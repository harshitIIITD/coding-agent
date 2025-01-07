# Dataset Preparation for Fine-Tuning the LLM

## Introduction

This document provides instructions on how to obtain and prepare the dataset for fine-tuning the large language model (LLM) used in this project.

## Obtaining the Dataset

1. Download the dataset from the following link:
   [Dataset Download Link](https://example.com/dataset)

2. Extract the downloaded dataset to the `data` directory within the project.

## Preparing the Dataset

1. Ensure that the dataset is in JSON format. Each entry in the dataset should contain the following fields:
   - `input`: The input text for the LLM.
   - `output`: The expected output text from the LLM.

2. Place the prepared dataset file in the `data` directory and name it `train_data.json`.

## Example Dataset Entry

Here is an example of a single entry in the dataset:

```json
{
  "input": "Write a Python function to add two numbers.",
  "output": "def add_numbers(a, b):\n    return a + b"
}
```

## Using the Dataset

1. The dataset will be used for fine-tuning the LLM. Ensure that the dataset is properly formatted and placed in the `data` directory.

2. Follow the instructions in the main `README.md` file to fine-tune the LLM using the prepared dataset.

## Additional Notes

- Make sure to review the dataset for any inconsistencies or errors before using it for fine-tuning.
- If you encounter any issues with the dataset, please open an issue on the project's GitHub repository.

## Using the New Script for Dataset Preparation

We have included a new script to download and prepare the dataset automatically. Follow the steps below to use the script:

1. Run the script to download and prepare the dataset:
   ```bash
   python data/download_and_prepare_data.py
   ```

2. The script will download the dataset, extract it, and prepare it in the required JSON format. The prepared dataset will be saved as `data/train_data.json`.

3. Ensure that the prepared dataset is properly formatted and placed in the `data` directory.

## Example Usage of the Script

Here is an example of how to use the new script to download and prepare the dataset:

```bash
python data/download_and_prepare_data.py
```

The script will handle the downloading, extracting, and preparing of the dataset, saving you time and effort.
