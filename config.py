import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Azure OpenAI Configuration
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = "https://internshala.openai.azure.com/"
AZURE_OPENAI_VERSION = "2024-08-01-preview"
AZURE_OPENAI_MODEL = "gpt-4o"

# Audio Configuration
TARGET_SAMPLE_RATE = 44100
TARGET_SIZE_MB = 10

# Application Settings
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Define common filler words and non-verbal sounds
FILLER_WORDS = {"um", "uh", "like", "you know", "so", "well", "ah"}
NON_VERBAL_SOUNDS = {"cough", "scream", "breath", "sigh"}

# File paths
TEMP_AUDIO_PATH = os.path.join(CURRENT_DIR, "temp_audio.wav")
TRANSCRIPTION_PATH = os.path.join(CURRENT_DIR, "transcription_with_punctuation.txt")
CORRECTED_PATH = os.path.join(CURRENT_DIR, "corrected_transcription_with_pauses.txt")
GENERATED_AUDIO_PATH = os.path.join(CURRENT_DIR, "generated_audio_with_pauses.wav")
OUTPUT_VIDEO_PATH = os.path.join(CURRENT_DIR, "final_video.mp4") 