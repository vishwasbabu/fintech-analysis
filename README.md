# Fintech Analysis

This repository demonstrates how to download the Chime S-1 filing and use it to fine-tune a Llama model for a chatbot. Due to the network restrictions in this environment, the provided scripts are designed to be executed in an environment with internet access.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `requirements.txt` with the following packages (or install them manually):

```
requests
beautifulsoup4
transformers
datasets
gradio
```

## Download the Chime S-1 Filing

```bash
python scripts/download_chime_s1.py
python scripts/preprocess_s1.py
```

These commands fetch the filing from the SEC and convert it to plain text under `data/chime_s1.txt`.

## Train the Llama Chatbot

Before running the training script, ensure you have accepted the license for the `meta-llama/Llama-4-Scout-17B-16E-Instruct` model on HuggingFace and that you have sufficient compute resources.

```bash
python scripts/train_llama_chatbot.py
```

The resulting model will be saved in the `model/` directory.

## Launch the Chatbot UI

After training, start an interactive Gradio demo with:

```bash
python app.py
```

This command opens a local web server where you can ask questions about the Chime S‑1 filing.

## Deploy to HuggingFace

After training, you can upload the model using the `huggingface-cli`:

```bash
huggingface-cli login  # enter your token
huggingface-cli repo create chime-s1-chatbot
huggingface-cli upload model/* --repo chime-s1-chatbot
```

This will create a repository under your HuggingFace account with the trained chatbot.

## Notes

The scripts were developed without internet access in this coding environment, so they have not been executed here. Run them in your local environment with internet connectivity to download the data and train the model.
