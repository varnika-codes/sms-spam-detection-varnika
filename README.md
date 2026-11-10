# SMS Shield - Intelligent SMS Spam Detection

SMS Shield is an NLP-based application that detects whether an SMS message is Spam or Ham using Machine Learning.

## Tech Stack

- Python
- FastAPI
- Streamlit
- Scikit-learn
- TF-IDF
- Multinomial Naive Bayes
- Pandas

## Project Architecture

- Backend: FastAPI handles SMS prediction requests.
- Frontend: Streamlit provides the user interface.
- ML Model: TF-IDF + Multinomial Naive Bayes.

## Project Structure

```text
SMS-Shield/
├── backend/
│   ├── main.py
│   ├── model/
│   └── requirements.txt
├── frontend/
│   ├── app.py
│   └── requirements.txt
├── data/
├── notebooks/
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd SMS-Shield
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Backend

```bash
uvicorn backend.main:app --reload
```

API documentation:

http://127.0.0.1:8000/docs

## Run Frontend

Open another terminal:

```bash
streamlit run frontend/app.py
```

## Features

- SMS spam detection
- REST API using FastAPI
- Interactive Streamlit interface
- Machine Learning-based classification

## Dataset

UCI SMS Spam Collection Dataset.

https://archive.ics.uci.edu/dataset/228/sms+spam+collection
