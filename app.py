from flask import Flask, request, render_template
from flask_cors import CORS
import json
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = Flask(__name__)
CORS(app)

model_name = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
conversation_history = []

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/chatbot', methods=['POST'])
def handle_prompt():
    data = request.get_json(force=True)
    input_text = data['prompt']

    history = "\n".join(conversation_history[-6:]) # Use last 6 messages for context
    context = (history + "\n" + input_text).strip()

    inputs = tokenizer(context, return_tensors="pt", truncation=True, max_length=128)

    outputs = model.generate(
        **inputs,
        max_new_tokens=60,
        do_sample=True,
        top_p=0.9,
        temperature=0.8,
        repetition_penalty=1.2,
        no_repeat_ngram_size=3,
    )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    conversation_history.append(input_text)
    conversation_history.append(response)
    conversation_history[:] = conversation_history[-6:]

    return response

if __name__ == '__main__':
    app.run()