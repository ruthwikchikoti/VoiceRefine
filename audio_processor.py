import os
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
from config import CURRENT_DIR, TARGET_SIZE_MB


class AudioProcessor:
    """Handles audio extraction and compression operations."""
    
    @staticmethod
    def extract_and_compress_audio(video_path, output_format="wav", target_size_mb=TARGET_SIZE_MB):
        """Extract audio from video and compress it."""
        temp_wav_path = os.path.join(CURRENT_DIR, "temp_audio.wav")
        compressed_audio_path = os.path.join(CURRENT_DIR, f"compressed_audio.{output_format}")

        video_clip = VideoFileClip(video_path)
        video_clip.audio.write_audiofile(temp_wav_path)

        audio = AudioSegment.from_wav(temp_wav_path)
        audio = audio.set_channels(1)

        duration_seconds = len(audio) / 1000.0
        target_bitrate = int((target_size_mb * 8 * 1024) / duration_seconds)

        audio.export(compressed_audio_path, format=output_format, bitrate=f"{target_bitrate}k")
        os.remove(temp_wav_path)

        return compressed_audio_path, video_clip.duration 