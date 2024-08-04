# Speech-to-Text Resume Analyzer and Translator

This Python script allows users to speak their resume information, which is then transcribed, analyzed, categorized into ATS resume sections, and optionally translated into different languages.

## Features

- Speech recognition for resume input
- Text analysis and categorization into ATS resume sections using Google's Gemini Pro AI
- Translation of the analyzed resume into multiple languages

## Prerequisites

- Python 3.x
- Google Cloud credentials
- Google Gemini Pro API key

## Required Libraries

- speech_recognition
- google.generativeai
- googletrans

## Installation

1. Clone the repository or download the script.
2. Install the required libraries:
pip install SpeechRecognition google-generativeai googletrans==3.1.0a0
3. Set up Google Cloud credentials:
- Place your Google Cloud credentials JSON file in a secure location.
- Update the path in the script:
  ```python
  os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/path/to/your/credentials.json'
  ```

4. Set up Google Gemini Pro API:
- Replace the API key in the script:
  ```python
  genai.configure(api_key='YOUR_GEMINI_PRO_API_KEY')
  ```

## Usage

1. Run the script:
python resume_analyzer.py
2. When prompted, speak your resume information clearly into your microphone.

3. The script will transcribe your speech, analyze and categorize the content, and display the results.

4. Choose a language for translation:
- 1 for English
- 2 for Telugu
- 3 for Hindi

5. The script will display the translated resume content.

## Functions

- `record_audio()`: Records audio input from the microphone.
- `transcribe_audio(audio)`: Transcribes the recorded audio to text.
- `analyze_text(text)`: Analyzes and categorizes the transcribed text into ATS resume sections.
- `translate_text(text, lang_code)`: Translates the analyzed text into the chosen language.
- `get_language_choice()`: Prompts the user to select a language for translation.
- `main()`: Orchestrates the entire process.

## Notes

- Ensure you have a working microphone connected to your computer.
- Internet connection is required for speech recognition, AI analysis, and translation.
- The accuracy of speech recognition and translation may vary.

## License

MIT

## Contact

M Lohith - `mlohith1338@gmail.com`
This README provides an overview of script, its features, installation instructions, usage guide, and other relevant information. 
