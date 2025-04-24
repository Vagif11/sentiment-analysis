"""
Author: Stephen Steinle
Date: 3/3/2025
Use Case: Bad Sentiment Analysis Example for Intro to AI CAI4002

Sentiment Analysis Implementation using a dictionary-based approach.
This module provides functionality to train a sentiment model from labeled data
and use it to classify the sentiment of new text as positive or negative.
"""
import json
import nltk    
import string                          
from nltk.corpus import stopwords      
from sklearn.feature_extraction.text import TfidfVectorizer  # Vectorizer
from sklearn.linear_model import LogisticRegression           # Classifier
from nltk.stem import WordNetLemmatizer

# Download required NLTK data packages if needed
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')


# Global dictionary to store word sentiment scores
sentimentModel = {}
# Initialize lemmatizer for word normalization
lemmatizer = WordNetLemmatizer()

_model = None
_vectorizer = None

# This function reads training data from the file
def load_training_data(trainFile):
    reviews = []  # List to save all reviews (text)
    labels = []   # List to save all labels (True/False)

    # Open the file. Each line has one review and label.
    with open(trainFile, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)  # Read one line and change it from text to Python dictionary
            text = preprocess(data["review"])  # Clean the review text (make it better for model)
            label = data["sentiment"]           # Get the label (True = positive, False = negative)
            reviews.append(text)                # Save the cleaned review
            labels.append(label)                # Save the label

    return reviews, labels  # After finishing all lines, give back reviews and labels


# This function cleans the text (make it simple and ready for model)
def preprocess(text):
    lemmatizer = WordNetLemmatizer()  # Tool that changes words to base form (ex: "running" -> "run")
    stop_words = set(stopwords.words('english'))  # List of common words to remove (like "the", "is")

    # Make all letters small and remove punctuation (like commas, dots)
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = text.split()  # Split the text into individual words

    # Remove stopwords and lemmatize each word
    cleaned = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    
    return ' '.join(cleaned)  # Join the words back into one cleaned sentence


def calcSentiment_train(trainingFile):
    """
    Train the sentiment model using labeled data from a JSON Lines file.
    
    Args:
        trainingFile (str): Path to the training file in JSONL format.
                            Each line should contain a review and its sentiment label (True/False).
    """

    global _model, _vectorizer  # These will save the model and vectorizer to use later when testing

    # Load the training data: get list of cleaned reviews and list of labels
    reviews, labels = load_training_data(trainingFile)

    # Create a tool that changes text into numbers
    _vectorizer = TfidfVectorizer(
        max_features=10000,  # Only keep up to 10,000 most important words or phrases
        ngram_range=(1, 2),  # Look at single words (1) and pairs of words (2) like "not good"
    )

    # Learn the important words from the reviews and change reviews into numbers (matrix)
    X = _vectorizer.fit_transform(reviews)

    # Create the model (Logistic Regression) to learn sentiment
    _model = LogisticRegression(max_iter=200)  # Model will try up to 200 times to get better (training cycles)
    
    # Train the model: it learns from X (features) and labels (True/False)
    _model.fit(X, labels)


    
def calcSentiment_test(text):
    """
    Classify the sentiment of input text using the trained model.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        bool: True if sentiment is positive, False if negative
    """
    global _model, _vectorizer

    if _model is None or _vectorizer is None:
        raise ValueError("Model not trained. Call calcSentiment_train first.")

    # Preprocess the input review
    cleaned_text = preprocess(text)

    # Convert to vector (must be wrapped in a list)
    X = _vectorizer.transform([cleaned_text])

    # Predict and return the result
    prediction = _model.predict(X)[0]
    return bool(prediction)
