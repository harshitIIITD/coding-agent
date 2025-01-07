import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
import os
import json

class CodingAIAgent:
    def __init__(self, model_name="Qwen", model_path=None):
        self.model_name = model_name
        self.model_path = model_path
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def load_model(self):
        if self.model_path and os.path.exists(self.model_path):
            self.model = AutoModelForCausalLM.from_pretrained(self.model_path)
        else:
            self.model = AutoModelForCausalLM.from_pretrained(self.model_name)

    def fine_tune(self, train_dataset, output_dir="fine_tuned_model", epochs=3, batch_size=8):
        training_args = TrainingArguments(
            output_dir=output_dir,
            num_train_epochs=epochs,
            per_device_train_batch_size=batch_size,
            save_steps=10_000,
            save_total_limit=2,
        )

        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=train_dataset,
        )

        trainer.train()
        self.model.save_pretrained(output_dir)
        self.tokenizer.save_pretrained(output_dir)

    def generate_code(self, prompt, max_length=100):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(inputs["input_ids"], max_length=max_length)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Coding AI Agent")
    parser.add_argument("--fine-tune", action="store_true", help="Fine-tune the LLM")
    parser.add_argument("--generate", action="store_true", help="Generate code using the AI agent")
    parser.add_argument("--prompt", type=str, help="Prompt for code generation")
    parser.add_argument("--train-data", type=str, help="Path to the training data for fine-tuning")
    args = parser.parse_args()

    agent = CodingAIAgent()

    if args.fine_tune:
        if not args.train_data:
            raise ValueError("Training data path must be provided for fine-tuning.")
        with open(args.train_data, "r") as f:
            train_data = json.load(f)
        agent.fine_tune(train_data)

    if args.generate:
        if not args.prompt:
            raise ValueError("Prompt must be provided for code generation.")
        print(agent.generate_code(args.prompt))

if __name__ == "__main__":
    main()
