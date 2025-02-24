# Quick Setup Guide

## 🚀 Running VoiceRefine Locally

### Prerequisites
- Python 3.8+ installed
- Google Cloud account with Speech APIs enabled
- Azure OpenAI account

### 1. Clone and Setup
```bash
git clone <your-repo-url>
cd VoiceRefine
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Environment Configuration
Create a `.env` file:
```env
AZURE_OPENAI_API_KEY=your_azure_openai_api_key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
GOOGLE_APPLICATION_CREDENTIALS=path/to/your/service-account.json
```

### 3. Run the Application
```bash
streamlit run main.py
```

### 4. Open Browser
Navigate to `http://localhost:8501`

---

