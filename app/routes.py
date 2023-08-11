from flask import render_template, request, jsonify
from app import app
import openai

openai.api_key = app.config['OPENAI_API_KEY']

@app.route('/', methods=['GET', 'POST'])
def index():
    conversation = []

    if len(conversation) == 0:
        conversation.append("ElizaGPT: Olá! Eu sou a ElizaGPT, uma psicanalista virtual. Como posso ajudar você hoje?")

    if request.method == 'POST':
        user_input = request.form['user_input']
        if user_input:
            conversation.append(f"User: {user_input}")
            response_message = generate_response("\n".join(conversation))
            conversation.append(f"{response_message}")
        else:
            response_message = ''

    return render_template('index.html', conversation=conversation)
    
def generate_response(conversation):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use o modelo de chat GPT-3.5 Turbo
        temperature=0.7,
        messages=[
            {"role": "system", "content": "You are a helpful assistant named ElizaGPT and will answer questions from patients."},
            {"role": "user", "content": conversation}
        ]
    )
    return response.choices[0].message['content'].strip()