# document.ai

Google Slides API:

API Documentation: https://developers.google.com/slides
Python Client Library: https://github.com/googleapis/google-api-python-client
Google Docs API:

API Documentation: https://developers.google.com/docs
Python Client Library: https://github.com/googleapis/google-api-python-client
OpenAI API:

API Documentation: https://beta.openai.com/docs/
Python Client Library: https://github.com/openai/openai-cookbook/blob/main/examples/How_to_generate_text_using_the_OpenAI_API.md
Project Structure:

```
    google_summary_project/
    │-- README.md
    │-- requirements.txt
    │-- main.py
    │-- credentials.json
    │-- summarizer.py
    │-- utils.py
    │-- data/
    │   │-- input_slides.pptx
    │   │-- input_doc.docx
    │-- venv/  (Virtual Environment - not included in the repository)

```
Regarding the summarization algorithm, since we're using OpenAI's GPT-3 model, the actual summarization will be handled by the model itself. Our task is to convert the document content into a format that can be passed to the model for summarization.

Here's a high-level overview of how the summarization process might look like:

Receive Attachment: The user attaches a document file using the UI.

Identify File Type: The application identifies the file type based on the file extension.

Read Document: Depending on the file type, the application uses the appropriate API (Google Slides or Google Docs API) to read the document and convert it to plain text.

Summarize Text: The application passes the plain text to the OpenAI API, which returns a summarized version of the text.

Display Summary: The summarized text is displayed on the UI.

The summarizer.py script will contain the function that interacts with the OpenAI API to generate the summary. The utils.py script can contain helper functions for identifying the file type, reading the document, and converting it to plain text. The main.py script will orchestrate the whole process and update the UI based on the results.


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
