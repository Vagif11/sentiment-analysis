# sentiment-analysis
sentiment classifier using logistic regression

# Sentiment Analysis on Movie Reviews

This project is a sentiment classifier that predicts whether a given movie review is **positive** or **negative**.

## 📌 Features

- Trains on labeled movie reviews (`True` for positive, `False` for negative)
- Uses `TfidfVectorizer` to convert text into numerical features
- Supports `Logistic Regression` (can be swapped with other classifiers)
- Simple, clean, and works with `.jsonlist` review files

## 🛠️ Tech Stack

- Python 3
- scikit-learn
- NLTK
- JSON for input data

## 🚀 How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/vagif11/sentiment-analysis.git
   cd sentiment-analysis
2. pip install -r requirements.txt
3. calcSentiment_train("reviews.jsonlist")
4.calcSentiment_test("This movie was absolutely amazing!")

HW3_AI/
│
├── sentiment_model.py      # main code
├── reviews.jsonlist        # training dataset
├── test_cases.txt          # (optional) manual test file
├── README.md               # you're reading this
└── ...
Vagif Asadov

NLP student | Deep learning explorer

LinkedIn ( (https://www.linkedin.com/in/asadovagif/) )
