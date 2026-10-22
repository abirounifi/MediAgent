# MediAgent — AI-Powered Biomedical Assistant

## Overview

MediAgent is an intelligent multi-agent biomedical assistant designed to analyze user-reported symptoms and provide structured health-related guidance. It relies on the collaboration of three specialized agents to analyze symptoms, retrieve medical information, and generate health recommendations through an interactive web interface.

## Features

- **Symptom Analysis:** Analyzes symptoms described by the user.
- **Medical Information Retrieval:** Retrieves relevant medical information.
- **Health Recommendations:** Generates structured health-related guidance.
- **Multi-Agent Collaboration:** Coordinates three specialized agents to process user input.
- **Interactive Interface:** Provides a user-friendly interface for interacting with the system.

## Technologies

- Python 3.11
- Streamlit
- LangChain
- Groq API — LLaMA 3.3
- python-dotenv

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/MediAgent.git
   ```

2. Navigate to the project directory:

   ```bash
   cd MediAgent
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and configure your Groq API key:

   ```env
   GROQ_API_KEY=your_api_key_here
   ```

5. Run the application:

   ```bash
   streamlit run app.py
   ```

*Note: Adapt the filenames and installation commands if your project uses a different structure.*

## How It Works

1. The user describes their symptoms.
2. The symptom analysis agent processes the input.
3. The medical agent retrieves relevant medical information.
4. The recommendation agent generates health-related guidance.
5. The results are displayed through the web interface.

## Disclaimer

MediAgent is an educational project and does not replace professional medical advice, diagnosis, or treatment. Its outputs should not be considered a definitive medical diagnosis.

## Author

Biomedical Engineering Student
