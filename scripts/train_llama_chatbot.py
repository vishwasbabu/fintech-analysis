"""Fine-tune a Llama model on the Chime S-1 filing."""

import os
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    Trainer,
    TrainingArguments,
    DataCollatorForLanguageModeling,
)
from datasets import load_dataset, Dataset

MODEL_NAME = "meta-llama/Llama-4-Scout-17B-16E-Instruct"  # requires acceptance of the license on HuggingFace
DATA_FILE = os.path.join("data", "chime_s1.txt")


def load_local_dataset(file_path: str, tokenizer):
    """Create a HuggingFace dataset from a local text file."""
    texts = [open(file_path, "r", encoding="utf-8").read()]
    dataset = Dataset.from_dict({"text": texts})
    return dataset.map(lambda e: tokenizer(e["text"]), batched=True)


def main():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

    dataset = load_local_dataset(DATA_FILE, tokenizer)
    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    training_args = TrainingArguments(
        output_dir="model",
        num_train_epochs=1,
        per_device_train_batch_size=1,
        save_steps=100,
        logging_steps=10,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        data_collator=data_collator,
    )

    trainer.train()
    trainer.save_model("model")
    tokenizer.save_pretrained("model")


if __name__ == "__main__":
    main()
