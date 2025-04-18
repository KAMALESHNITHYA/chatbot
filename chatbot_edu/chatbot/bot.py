# chatbot/bot.py

import json
import re

class ChatBot:
    def __init__(self, faq_path):
        with open(faq_path, 'r') as file:
            self.data = json.load(file)

    def preprocess(self, text):
        text = text.lower()
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        return text

    def get_response(self, user_input):
        user_input = self.preprocess(user_input)

        for item in self.data["faq"]:
            for pattern in item["patterns"]:
                if self.preprocess(pattern) in user_input:
                    return item["response"]

        return "Sorry, I couldn’t find an answer for that. Please try rephrasing."
