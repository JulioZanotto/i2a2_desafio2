from flask import render_template, request, jsonify
from app import app
import openai

openai.api_key = app.config['OPENAI_API_KEY']

@app.route('/', methods=['GET', 'POST'])
def index():
    response_message = ''

    if request.method == 'POST':
        user_input = request.form['user_input']
        if user_input:
            response = openai.Completion.create(
                engine="davinci",
                prompt=user_input,
                max_tokens=50
            )
            response_message = response.choices[0].text.strip()

    return render_template('index.html', response_message=response_message)
