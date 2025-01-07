# Coding AI Agent with Deep Thinking Ability

## Project Description

This project aims to create a coding AI agent with deep thinking ability using open source LLM such as Qwen. The AI agent will be fine-tuned to assist in coding tasks, providing intelligent code suggestions, and improving coding efficiency.

## Purpose

The purpose of this project is to leverage the power of large language models (LLMs) to create an AI agent that can assist developers in writing code. By fine-tuning the LLM, we aim to enhance its ability to understand and generate code, making it a valuable tool for developers.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/harshitIIITD/coding-agent.git
   cd coding-agent
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Fine-tune the LLM:
   ```bash
   python src/agent.py --fine-tune
   ```

4. Use the AI agent to generate code:
   ```bash
   python src/agent.py --generate
   ```

## Setup Instructions

1. Ensure you have Python 3.7 or higher installed.
2. Clone the repository and navigate to the project directory.
3. Install the required dependencies using the provided `requirements.txt` file.
4. Follow the instructions in the `data/README.md` file to obtain and prepare the dataset for fine-tuning the LLM.
5. Run the fine-tuning script to train the LLM on the prepared dataset.
6. Use the AI agent to generate code by running the appropriate script.

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

## Contributing

We welcome contributions to this project! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Open a pull request to the main repository.

Please ensure that your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for more details.
