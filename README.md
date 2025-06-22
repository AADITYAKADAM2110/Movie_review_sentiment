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

## 📅 Development Timeline (15 Days)

| Day        | Task                                       |
|------------|--------------------------------------------|
| Day 1      | Project setup, Git, dataset exploration    |
| Days 2-4   | Preprocess text data, TF-IDF vectorization |
| Days 5-6   | Train sentiment classifier (LogReg/NB)     |
| Day 7      | Model evaluation and tuning                |
| Days 8-9   | Build similarity engine using TF-IDF       |
| Day 10     | Combine sentiment + recommendation logic   |
| Days 11-12 | Optional web app using Streamlit           |
| Day 13     | Visualization, output logs                 |
| Day 14     | Create PPT and document findings           |
| Day 15     | Final polish and presentation              |

---

## 🌱 Future Improvements

- Add mood/genre filters to refine recommendations
- Use BERT for contextual similarity
- Deploy fully using Streamlit Cloud / Render / HuggingFace Spaces

---
