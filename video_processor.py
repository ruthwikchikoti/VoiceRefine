from moviepy.editor import VideoFileClip, AudioFileClip


class VideoProcessor:
    """Handles video processing operations like audio replacement."""
    
    @staticmethod
    def replace_audio_in_video(video_path, audio_path, output_path):
        """Replace the audio in the video with the new synced audio."""
        video_clip = VideoFileClip(video_path)
        audio_clip = AudioFileClip(audio_path)

        final_video = video_clip.set_audio(audio_clip)
        final_video.write_videofile(output_path, codec='libx264', audio_codec='aac')

        video_clip.close()
        audio_clip.close() 