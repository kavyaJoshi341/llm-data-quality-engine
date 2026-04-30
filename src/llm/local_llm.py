from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = None
model = None

def load_model():
    global tokenizer, model
    if tokenizer is None or model is None:
        tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
        model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

def generate_local_response(prompt):
    try:
        load_model()
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
        outputs = model.generate(**inputs, max_length=256)
        return tokenizer.decode(outputs[0], skip_special_tokens=True)
    except Exception:
        return "Insight generation unavailable (resource constraint)"