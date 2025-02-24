

import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "your-secret-key"  # Replace with a non-sensitive key

    # Load OpenAI API key from environment variable
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
