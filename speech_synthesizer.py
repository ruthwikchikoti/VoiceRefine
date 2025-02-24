from google.cloud import texttospeech_v1 as texttospeech


class SpeechSynthesizer:
    """Handles text-to-speech conversion using Google Cloud Text-to-Speech API."""
    
    def __init__(self):
        self.client = texttospeech.TextToSpeechClient()
    
    def generate_audio_from_text(self, text, output_audio_path):
        """Generate audio from text using Google Text-to-Speech, leveraging pauses."""
        input_text = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US", 
            name="en-US-Journey-D"
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16
        )
        
        response = self.client.synthesize_speech(
            input=input_text, 
            voice=voice, 
            audio_config=audio_config
        )

        with open(output_audio_path, "wb") as out:
            out.write(response.audio_content) 