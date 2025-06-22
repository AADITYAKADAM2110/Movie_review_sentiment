# 🎬 Movie Review Analyzer & Recommendation System

A Machine Learning + NLP project that performs sentiment analysis on movie reviews and recommends similar movies based on user input and review content.

---

## 🎯 Objective

- Analyze the **sentiment** (positive/negative) of a given movie review.
- Recommend **similar movies** using NLP techniques like TF-IDF and cosine similarity.

---

## 🧠 Technologies

- **Language**: Python
- **Libraries**: scikit-learn, pandas, numpy, nltk, matplotlib, seaborn
- **ML Models**: Logistic Regression, Naive Bayes
- **NLP Techniques**: TF-IDF, cosine similarity, text preprocessing
- **Deployment (optional)**: Streamlit or Flask
- **Version Control**: Git, GitHub

---

## 📦 Dataset

- Source: [Kaggle - IMDB Dataset of 50K Movie Reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
- Columns:
  - `review`: Text of the movie review
  - `sentiment`: Label (`positive` or `negative`)

---

## 🗂️ Project Structure

movie_recommender_sentiment/
├── data/ → Raw and processed datasets
├── models/ → Trained sentiment models
├── notebooks/ → Jupyter exploration notebooks
├── src/
│ ├── preprocess.py → Text cleaning and vectorization
│ ├── train_sentiment.py → Sentiment model training
│ └── recommender.py → Movie similarity and recommendation
├── app/ → Web app (Streamlit or Flask)
├── output/ → Predictions, logs, visual results
├── README.md → Project documentation
└── .gitignore → Ignored files for version control


---


