import streamlit as st
import tempfile
import os

from audio_processor import AudioProcessor
from transcription_service import TranscriptionService
from text_processor import TextProcessor
from speech_synthesizer import SpeechSynthesizer
from video_processor import VideoProcessor
from config import GENERATED_AUDIO_PATH, OUTPUT_VIDEO_PATH


def main():
    """Main application function for VoiceRefine."""
    st.set_page_config(
        page_title="VoiceRefine - AI Audio Enhancement", 
        layout="wide",
        page_icon="🎙️"
    )
    
    st.title("🎙️ VoiceRefine - AI-Powered Audio Enhancement")
    st.markdown("### Transform poor audio quality into crystal-clear, professional speech!")
    
    # Create columns for better layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **VoiceRefine** automatically:
        - 🎯 Removes filler words ("um", "uh", "like")
        - ✍️ Corrects grammar and improves clarity
        - 🔊 Generates natural-sounding speech
        - 🎥 Syncs perfectly with your video
        """)
    
    with col2:
        st.info("💡 **Tip**: Upload any video with spoken content to get started!")

    uploaded_file = st.file_uploader(
        "Choose your video file", 
        type=["mp4", "mkv", "mov", "avi"],
        help="Upload a video file containing speech to enhance"
    )

    if uploaded_file:
        # Initialize services
        audio_processor = AudioProcessor()
        transcription_service = TranscriptionService()
        text_processor = TextProcessor()
        speech_synthesizer = SpeechSynthesizer()
        video_processor = VideoProcessor()
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video_file:
            temp_video_file.write(uploaded_file.read())
            temp_video_path = temp_video_file.name

        try:
            # Step 1: Extract and compress audio
            with st.spinner("🎵 Extracting audio from video..."):
                audio_path, video_duration = audio_processor.extract_and_compress_audio(temp_video_path)
            
            st.success("✅ Audio extracted successfully!")
            
            # Display original audio
            st.subheader("🎧 Original Audio")
            st.audio(audio_path)

            # Step 2: Transcribe original audio
            with st.spinner("📝 Transcribing audio..."):
                transcription, word_timings = transcription_service.transcribe_audio(audio_path)
            
            st.subheader("📋 Original Transcription")
            st.text_area("Original text:", transcription, height=100)

            # Step 3: Correct transcription using AI
            with st.spinner("🤖 Enhancing text with AI..."):
                corrected_text = text_processor.correct_transcription(transcription, video_duration)
            
            st.subheader("✨ Enhanced Transcription")
            st.text_area("Enhanced text:", corrected_text, height=100)

            # Step 4: Generate enhanced audio
            with st.spinner("🎙️ Generating enhanced audio..."):
                speech_synthesizer.generate_audio_from_text(corrected_text, GENERATED_AUDIO_PATH)
            
            st.subheader("🔊 Enhanced Audio")
            st.audio(GENERATED_AUDIO_PATH)

            # Step 5: Replace audio in video
            with st.spinner("🎬 Creating final video..."):
                video_processor.replace_audio_in_video(temp_video_path, GENERATED_AUDIO_PATH, OUTPUT_VIDEO_PATH)

            st.success("🎉 Video enhancement completed!")
            
            # Display final result
            st.subheader("🎬 Final Enhanced Video")
            st.video(OUTPUT_VIDEO_PATH)
            
            # Download button
            with open(OUTPUT_VIDEO_PATH, "rb") as video_file:
                st.download_button(
                    label="📥 Download Enhanced Video",
                    data=video_file.read(),
                    file_name="enhanced_video.mp4",
                    mime="video/mp4"
                )
                
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
            st.info("💡 Make sure your Google Cloud and Azure OpenAI credentials are properly configured.")
            
        finally:
            # Cleanup temporary file
            if os.path.exists(temp_video_path):
                os.remove(temp_video_path)
    else:
        st.markdown("""
        ---
        ### 🚀 How it works:
        
        1. **Upload** your video file
        2. **Extract** audio automatically
        3. **Transcribe** speech to text
        4. **Enhance** with AI (remove fillers, fix grammar)
        5. **Generate** new professional audio
        6. **Download** your enhanced video
        
        ### 🔧 Requirements:
        - Google Cloud Speech-to-Text API
        - Google Cloud Text-to-Speech API  
        - Azure OpenAI API
        """)


if __name__ == "__main__":
    main() 