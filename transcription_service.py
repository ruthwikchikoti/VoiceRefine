import os
from google.cloud import speech_v1p1beta1 as speech
from config import TARGET_SAMPLE_RATE, TRANSCRIPTION_PATH


class TranscriptionService:
    """Handles speech-to-text transcription using Google Cloud Speech API."""
    
    def __init__(self):
        self.client = speech.SpeechClient()
    
    def transcribe_audio(self, audio_path):
        """Transcribe the audio using Google Speech-to-Text with punctuation."""
        with open(audio_path, "rb") as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=TARGET_SAMPLE_RATE,
            language_code="en-US",
            enable_automatic_punctuation=True,
            enable_word_time_offsets=True
        )

        response = self.client.recognize(config=config, audio=audio)

        full_transcript = ""
        word_timings = []

        for result in response.results:
            full_transcript += result.alternatives[0].transcript + " "
            for word in result.alternatives[0].words:
                word_timings.append({
                    'word': word.word,
                    'start_time': word.start_time.total_seconds(),
                    'end_time': word.end_time.total_seconds()
                })

        with open(TRANSCRIPTION_PATH, "w") as file:
            file.write(full_transcript)

        return full_transcript, word_timings 