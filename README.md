# Sentiment Analysis CLI Tool

A simple command-line Python tool that classifies input text as positive, negative, or neutral sentiment using scikit-learn and NLTK.

## Features

- Trains a basic sentiment classifier on a sample dataset.
- Takes user input from the command line.
- Predicts and displays the sentiment.

## Setup

1. Clone the repository.
2. (Recommended) Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

```bash
python sentiment_analysis.py
```

Enter your text when prompted.

## Extending

- Add more training data to improve accuracy.
- Integrate with a web framework (e.g., Flask) for a web app.
- Use pre-trained models or external datasets.

## License

MIT License.
