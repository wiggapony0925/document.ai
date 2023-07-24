# document.ai

Google Slides API:

API Documentation: https://developers.google.com/slides
Python Client Library: https://github.com/googleapis/google-api-python-client
Google Docs API:

API Documentation: https://developers.google.com/docs
Python Client Library: https://github.com/googleapis/google-api-python-client
NLTK (Natural Language Toolkit):

Official Website: https://www.nltk.org/
Documentation: https://www.nltk.org/api/nltk.html
BERT Extractive Summarizer:

GitHub Repository: https://github.com/dmmiller612/bert-extractive-summarizer
Google Text-to-Speech API:

API Documentation: https://cloud.google.com/text-to-speech
Python Client Library: https://github.com/googleapis/python-texttospeech

https://chat.openai.com/share/4531049b-dcdf-49ad-874f-86b63e3699b7 link to setup chat

google_summary_project/
│-- README.md
│-- requirements.txt
│-- main.py
│-- credentials.json
│-- summarizer.py
│-- text_to_speech.py
│-- utils.py
│-- data/
│   │-- input_slides.pptx
│   │-- input_doc.docx
│-- venv/  (Virtual Environment - not included in the repository)
```

Let's briefly go through each file and directory:

1. `README.md`: A markdown file containing information about your project, how to set it up, and how to use it.

2. `requirements.txt`: The file we created earlier that lists all the required Python libraries and their versions.

3. `main.py`: The main Python script that orchestrates the entire process of fetching content from Google Slides and Docs, generating the summary or letter, and, if needed, converting it to speech.

4. `credentials.json`: A file containing the API credentials for authenticating your application with Google APIs. You should obtain this file from the Google Developer Console when setting up the API credentials.

5. `summarizer.py`: A Python module that contains functions or classes responsible for text summarization using NLP techniques like sentence tokenization, summarization models, etc.

6. TKIR FOR UI

7. `utils.py`: A Python module that contains utility functions or helper functions that might be used across multiple parts of your project.

8. `data/`: A directory to store input files, such as Google Slides or Docs files, that you want to summarize.

9. `venv/`: The virtual environment directory where the Python virtual environment will be created. This directory is not included in the repository and is created when you set up the virtual environment.
