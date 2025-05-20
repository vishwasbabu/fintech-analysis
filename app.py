import os
import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

MODEL_PATH = os.getenv("MODEL_PATH", "model")


def load_model(path: str):
    """Load the fine-tuned model from the given path."""
    tokenizer = AutoTokenizer.from_pretrained(path)
    model = AutoModelForCausalLM.from_pretrained(path)
    return pipeline("text-generation", model=model, tokenizer=tokenizer)


chatbot = load_model(MODEL_PATH)


def respond(message: str, history: list[tuple[str, str]]):
    """Generate a response for the user's message."""
    output = chatbot(message, max_new_tokens=200)
    text = output[0]["generated_text"]
    if text.startswith(message):
        text = text[len(message) :]
    return text.strip()


CSS = """
body {background-color: #f5f7fa;}
#component-0 {max-width: 800px; margin: auto;}
"""

with gr.Blocks(css=CSS, title="Chime S-1 Chatbot") as demo:
    gr.Markdown(
        """# Chime S‑1 Chatbot
Ask questions about Chime's S‑1 filing. This interface lets you interact with a Llama model fine‑tuned on the official document.
"""
    )
    gr.ChatInterface(respond)

if __name__ == "__main__":
    demo.launch()
