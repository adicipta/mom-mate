# 🫂 Mom Mate

Mom Mate is an AI-powered chatbot designed to support pregnant women, young mothers, and families. It helps with planning a healthy pregnancy, provides balanced nutrition guidelines, and delivers interactive answers based on trusted health references (e.g., documents from the Indonesian Ministry of Health).

## 📊 Overview
- Plan for a **healthy pregnancy** with reliable guidelines.
- Access **balanced nutrition recommendations** for pregnant and breastfeeding mothers.
- Get **contextual answers** directly from official health documents.

## 🚀 Features

- **📚 Document-based Q&A** - Answers are grounded in official PDFs.
- **🧠 Conversational Memory** - Keeps track of chat history.
- **⚡ Fast Retrieval** - Uses FAISS for semantic similarity search.
- **🌐 User-friendly UI** - Built with Streamlit for easy interaction.

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/adicipta/mom-mate

# Navigate to project directory
cd mom-mate

# Copy .env.example to .env
cp .env.example .env

# Create a Conda Environment
Open your terminal or Anaconda Prompt and create a new environment:
    conda create -n chatbot-env python=3.9
    conda activate chatbot-env

# Install dependencies
pip install -r requirements.txt

#Run the Streamlit Application**
streamlit run app.py

The application will open in your web browser.
```