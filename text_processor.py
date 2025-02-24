import openai
from config import (
    FILLER_WORDS, NON_VERBAL_SOUNDS, CORRECTED_PATH,
    AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, 
    AZURE_OPENAI_VERSION, AZURE_OPENAI_MODEL
)


class TextProcessor:
    """Handles text processing, filler word removal, and AI-based correction."""
    
    def __init__(self):
        # Configure Azure OpenAI
        openai.api_type = "azure"
        openai.api_key = AZURE_OPENAI_API_KEY
        openai.api_base = AZURE_OPENAI_ENDPOINT
        openai.api_version = AZURE_OPENAI_VERSION
    
    @staticmethod
    def remove_filler_words_and_add_pauses(text):
        """Remove filler words and replace them with pauses (full stops or ellipses)."""
        words = text.split()
        processed_words = []
        
        for word in words:
            clean_word = word.lower().strip(".,!?")
            if clean_word not in FILLER_WORDS and clean_word not in NON_VERBAL_SOUNDS:
                processed_words.append(word)
            elif clean_word in FILLER_WORDS:
                # Replace filler words with pauses
                processed_words.append(".")
            elif clean_word in NON_VERBAL_SOUNDS:
                # Replace non-verbal sounds with longer pauses
                processed_words.append("...")
        
        return " ".join(processed_words)
    
    def correct_transcription(self, text, target_duration):
        """Send transcription to Azure OpenAI GPT-4 for grammar correction, keeping pauses."""
        # Remove filler words and replace them with pauses before sending to GPT-4
        text_with_pauses = self.remove_filler_words_and_add_pauses(text)

        messages = [
            {
                "role": "system", 
                "content": f"Correct this transcription while preserving pauses, punctuation, and the overall structure. Remove filler words and maintain pauses where filler words and non-verbal sounds existed."
            },
            {
                "role": "user", 
                "content": f"Please correct the following text to fit within {target_duration:.2f} seconds while preserving the pauses:\n\n{text_with_pauses}"
            }
        ]

        response = openai.ChatCompletion.create(
            engine=AZURE_OPENAI_MODEL,
            messages=messages,
            max_tokens=500
        )
        
        corrected_text = response.choices[0].message['content'].strip()

        with open(CORRECTED_PATH, "w") as file:
            file.write(corrected_text)

        return corrected_text 