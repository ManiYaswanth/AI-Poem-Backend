import os
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon if you haven't already
nltk.download('vader_lexicon')

# Create a class of the VADER sentiment analyzer
class SentimentAnalyzer:
    analyzer = SentimentIntensityAnalyzer()
    emotion_mapping = {
                    "pos": 'joy',
                    "compound": 'surprise', 
                    "neg": 'sadness', 
                    "neu": 'neutral'
                }

class OpenAIConfig:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = "text-davinci-003"
    POEM_MAX_TOKENS = 200

# Example poem text
example_poem = """
\n\nNo more joy, no more cheer \nI've lost the spark that brought me here \nIt's been so long since I've been able to care \nThose days of happiness I can't repair \n\nMy spirit is waning, my heart still so hollow \nI can hardly remember why I used to follow \nThis cloud of heaviness it won't let me go\nI can barely see in front of me as the darkness grows \n\nA sadness sets in, I can no longer pretend \nLike a storm that's taking away a life I can't mend \nThe emptiness remains and I know it's not fair \nThat I can't feel happy anymore anywhere.
"""