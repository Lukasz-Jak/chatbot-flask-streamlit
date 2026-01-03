from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

app = Flask(__name__)


@app.route('/chat/hello')
def hello_world():
    return 'Hello World!'


def send_message(message, previous_response_id):
    response = client.responses.create(
        model='gpt-4.1-mini',
        input=message,
        previous_response_id=previous_response_id
    )

    return response.output_text, response.id


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()

    if not data or 'message' not in data:
        return jsonify({'error': 'Missing field(s)'}), 400

    message = data['message']
    previous_response_id = data.get('previousResponseId')

    response, response_id = send_message(message, previous_response_id)

    return jsonify({
        'response': response,
        'responseId': response_id
    })


if __name__ == '__main__':
    app.run()
