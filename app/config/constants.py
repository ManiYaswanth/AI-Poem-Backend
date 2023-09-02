import os
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon if you haven't already
# nltk.download('vader_lexicon')

# Create an instance of the VADER sentiment analyzer
class SentimentAnalyzer:
    analyzer = SentimentIntensityAnalyzer()
    emotion_mapping = {
                    "pos": 'joy',
                    "compound": 'surprise', 
                    "neg": 'sadness', 
                    "neu": 'neutral'
                }

# Example poem text
poem = """
I'm alive yet I feel empty
My soul spent so much time unready
I have heart and I have smiles
But lost in my own private aisles
I'm happy yet I feel sad
Emotions running good and bad
My life is filled with much delight
But there are days I don't feel quite right
"""
class OpenAIConfig:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = "text-davinci-003"
    POEM_MAX_TOKENS = 100
