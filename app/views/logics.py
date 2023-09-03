from flask import Blueprint
import openai
import math
from config.constants import (OpenAIConfig,
                              SentimentAnalyzer
                              )

openai.api_key = OpenAIConfig.OPENAI_API_KEY
mod = Blueprint("logics", __name__, template_folder="templates")

def validate_request(data):
    if not data or not data.get("prompt"):
        return "invalid"
    return "valid"

def generate_ai_poem(prompt):
    try:
        prompt = prompt + ". Generate a poem on this idea"
        response = openai.Completion.create(
            model=OpenAIConfig.OPENAI_MODEL,
            prompt=prompt,
            max_tokens= OpenAIConfig.POEM_MAX_TOKENS,
        )
        if response:
            generated_poem = response.choices[0].text.strip()
            return generated_poem
        else:
            return "error"
    except:
        return "error"
    

def analyze_emotion(poem):
    sentiment = SentimentAnalyzer.analyzer.polarity_scores(poem)
    total_score = 0
    for emotion, score in sentiment.items():
        if emotion in SentimentAnalyzer.emotion_mapping and score > 0:
            total_score += score
    emotion_percentages = {SentimentAnalyzer.emotion_mapping[emotion]: round((score / total_score) * 100, 1) 
                        for emotion, score in sentiment.items() 
                        if emotion in SentimentAnalyzer.emotion_mapping and score > 0}
    return emotion_percentages
    