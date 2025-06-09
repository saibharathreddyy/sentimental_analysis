import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Download NLTK data if not already present
nltk.download("punkt", quiet=True)

# Sample training data (expand for better accuracy)
train_texts = [
    "I love this product, it's amazing!",  # positive
    "This is the best thing ever!",        # positive
    "I hate this, it's terrible.",         # negative
    "This is the worst purchase I've made.", # negative
    "It's okay, not great but not bad.",   # neutral
    "Nothing special, just average.",      # neutral
]
train_labels = [
    "positive",
    "positive",
    "negative",
    "negative",
    "neutral",
    "neutral"
]

# Vectorize text
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(train_texts)

# Train classifier
classifier = MultinomialNB()
classifier.fit(X_train, train_labels)

def predict_sentiment(text):
    X_test = vectorizer.transform([text])
    pred = classifier.predict(X_test)
    return pred[0]

def main():
    print("Simple Sentiment Analysis Tool")
    print("Type your sentence and press enter (type 'exit' to quit):")
    while True:
        user_input = input("> ")
        if user_input.lower() == "exit":
            break
        sentiment = predict_sentiment(user_input)
        print(f"Sentiment: {sentiment}")

if __name__ == "__main__":
    main()
