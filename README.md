  # **VoiceRefine** 🎙️

  _Transform poor audio quality into crystal-clear, professional speech with AI-powered enhancement_

  ---

  ## **✨ What is VoiceRefine?**

  **VoiceRefine** is an intelligent audio enhancement tool that automatically transforms poorly recorded video audio into professional-quality speech. Whether your video contains filler words, poor grammar, or unclear speech, VoiceRefine uses advanced AI to clean it up and create perfectly synchronized, natural-sounding audio.

  ### **🎯 Perfect for:**
  - Content creators and YouTubers
  - Online educators and lecturers  
  - Podcast producers
  - Business professionals
  - Anyone who wants to enhance video audio quality

  ---

  ## **🚀 Key Features**

  - **🎯 Smart Filler Removal**: Automatically removes "um", "uh", "like", and other speech fillers
  - **✍️ Grammar Correction**: Improves sentence structure and clarity using AI
  - **🔊 Natural Speech Generation**: Creates human-like audio with proper intonation
  - **🎥 Perfect Synchronization**: Maintains video timing and natural pauses
  - **📱 Easy Web Interface**: Simple drag-and-drop interface built with Streamlit
  - **⚡ Fast Processing**: Efficient pipeline for quick audio enhancement

  ---

  ## **🛠️ Technology Stack**

  ### **Core Technologies**
  - **Python** - Backend processing
  - **Streamlit** - Web interface
  - **MoviePy** - Video/audio processing
  - **PyDub** - Audio manipulation

  ### **AI Services**
  - **Azure OpenAI (GPT-4)** - Text correction and enhancement
  - **Google Cloud Speech-to-Text** - Audio transcription
  - **Google Cloud Text-to-Speech** - Natural speech generation

  ### **Modular Architecture**
  ```
  VoiceRefine/
  ├── main.py                 # Main Streamlit application
  ├── config.py               # Configuration and constants
  ├── audio_processor.py      # Audio extraction and compression
  ├── transcription_service.py # Speech-to-text functionality
  ├── text_processor.py       # AI text enhancement
  ├── speech_synthesizer.py   # Text-to-speech generation
  ├── video_processor.py      # Video processing operations
  └── requirements.txt        # Dependencies
  ```

  ---

  ## **⚙️ Installation & Setup**

  ### **1. Clone the Repository**
  ```bash
  git clone https://github.com/ruthwikchikoti/VoiceRefine
  cd VoiceRefine
  ```

  ### **2. Create Virtual Environment**
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```

  ### **3. Install Dependencies**
  ```bash
  pip install -r requirements.txt
  ```

  ### **4. Configure API Keys**

  Create a `.env` file in the project root:

  ```env
  # Azure OpenAI Configuration
  AZURE_OPENAI_API_KEY=your_azure_openai_api_key
  AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint

  # Google Cloud Configuration  
  GOOGLE_APPLICATION_CREDENTIALS=path/to/your/service-account.json
  ```

  **Getting API Keys:**

  - **Azure OpenAI**: Sign up at [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/cognitive-services/openai-service/)
  - **Google Cloud**: Create a project at [Google Cloud Console](https://console.cloud.google.com/) and enable Speech-to-Text and Text-to-Speech APIs

  ---

  ## **▶️ Running the Application**

  ### **Option 1: Run the new modular version (Recommended)**
  ```bash
  streamlit run main.py
  ```

  ### **Option 2: Run the legacy version**
  ```bash
  streamlit run app.py
  ```

  The application will open in your browser at `http://localhost:8501`

  ---

  ## **📖 How to Use**

  1. **Upload Your Video**: Choose any video file (MP4, MOV, AVI, MKV)
  2. **Automatic Processing**: 
    - Audio extraction
    - Speech transcription
    - AI-powered text enhancement
    - Natural speech generation
    - Video synchronization
  3. **Download Results**: Get your enhanced video with professional audio

  ---

  ## **🏗️ Project Structure**

  This project follows a modular architecture for better maintainability:

  - **`config.py`** - Centralized configuration management
  - **`audio_processor.py`** - Handles audio extraction and compression
  - **`transcription_service.py`** - Google Cloud Speech-to-Text integration
  - **`text_processor.py`** - AI-powered text enhancement with Azure OpenAI
  - **`speech_synthesizer.py`** - Google Cloud Text-to-Speech integration
  - **`video_processor.py`** - Video processing and audio replacement
  - **`main.py`** - Main Streamlit application with improved UI

  ---

  ## **🔧 Development Environment**

  ### **Dev Container (Optional)**
  This project includes a dev container configuration for consistent development environments. You can delete the `.devcontainer` folder if you don't use Docker-based development.

  ### **Local Development**
  For local development, simply follow the installation steps above.

  ---

  ## **🚀 Deployment**

  ### **Streamlit Cloud**
  1. Push your code to GitHub
  2. Connect your repository to [Streamlit Cloud](https://streamlit.io/cloud)
  3. Configure your environment variables in Streamlit Cloud settings
  4. Deploy!

  ### **Local Deployment**
  ```bash
  streamlit run main.py --server.port 8501
  ```



  ---

  ## **🆘 Troubleshooting**

  ### **Common Issues**

  **API Errors:**
  - Ensure all API keys are correctly configured in your `.env` file
  - Check that Google Cloud services are enabled for your project
  - Verify Azure OpenAI endpoint and key are valid

  **Audio Quality Issues:**
  - Input videos should have clear speech for best results
  - Avoid very noisy or music-heavy audio
  - Ensure adequate file size and quality

  **Performance:**
  - Large video files may take longer to process
  - Consider compressing input videos for faster processing



  **Built with ❤️ for better audio experiences**

