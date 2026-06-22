from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Paste your OpenRouter API key here
API_KEY = "paste your API key here"

API_URL = "https://openrouter.ai/api/v1/chat/completions"


def get_summary(text):

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",

        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant that summarizes text in simple language."
            },
            {
                "role": "user",
                "content": f"Summarize the following text in 5-6 lines:\n\n{text}"
            }
        ],

        "temperature": 0.5,
        "max_tokens": 300
    }

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json=payload
        )

        if response.status_code == 200:
            data = response.json()
            return data["choices"][0]["message"]["content"]

        else:
            return f"Error {response.status_code}: {response.text}"

    except Exception as e:
        return f"Error: {str(e)}"


@app.route("/", methods=["GET", "POST"])
def home():

    summary = ""

    if request.method == "POST":
        text = request.form["text"]

        if text.strip():
            summary = get_summary(text)

    return render_template("index.html", summary=summary)


if __name__ == "__main__":
    app.run(debug=True)