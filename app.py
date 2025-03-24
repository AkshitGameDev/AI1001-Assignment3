from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def webhook():
    quotes = [
        "Believe you can and you're halfway there.",
        "The only way to do great work is to love what you do.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Don't watch the clock; do what it does. Keep going.",
        "The future belongs to those who believe in the beauty of their dreams."
    ]
    response = {
        "fulfillmentText": random.choice(quotes)
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()
