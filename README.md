
# AI Text Summarizer

A simple web application built using **Flask** that allows users to paste text and generate a concise summary using an AI model.

## Features

* Paste any text into the input box.
* Generate a short and clear summary.
* Simple and user-friendly interface.
* Built with Flask and integrated with AI.

## Tech Stack

* Python
* Flask
* HTML
* CSS
* OpenRouter API

## AI Model Used

This project uses the following AI model through OpenRouter:

**NVIDIA: Nemotron 3 Nano Omni (Free)**

Model ID:

```text
nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free
```

## Getting the API Key

1. Visit [https://openrouter.ai](https://openrouter.ai)
2. Create an account or sign in.
3. Navigate to the **Keys** section from your dashboard.
4. Generate a new API key.
5. Copy the generated API key and paste it into the `app.py` file.

Example:

```python
API_KEY = "your_openrouter_api_key"
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <project-folder>
```

Install the required dependencies:

```bash
pip install flask requests
```

## Run the Project

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Project Structure

```text
project-folder/
│
├── app.py
├── templates/
│   └── index.html

```



