# UFC Fight Predictor 🥊

A machine learning-powered web application to predict UFC fight outcomes using historical data and betting odds.

## 🔍 Overview

UFC Fight Predictor uses machine learning algorithms to forecast match results based on comprehensive fighter statistics, historical performance, and betting market data. The application helps MMA enthusiasts and bettors make more informed decisions by analyzing patterns across thousands of professional fights.

- **Goal**: Predict Red/Blue corner winner using fighter stats, rankings, and betting odds
- **Dataset**: 6,000+ fights with 70+ features (strikes, takedowns, odds, etc.)
- **Challenges**: Class imbalance (57% Red wins), sparse rankings data (95% missing)

## 🚀 Key Features

- **Predictive Models**: 65% accuracy with top predictive features being betting odds and strike accuracy
- **Fighter Comparison**: Side-by-side analysis of competing fighters
- **Betting Intelligence**: Confidence scores and historical trend analysis
- **Real-Time Predictions**: Up-to-date fight outcome probabilities

## 🛠️ Technology Stack

- **Machine Learning**: scikit-learn (Logistic Regression, Random Forest)
- **Backend**: Django (Python)
- **Frontend**: HTML/CSS with Bootstrap
- **Data Processing**: Pandas for preprocessing (imputation, undersampling)

## 📊 Model Performance

Our models currently achieve:
- 65% prediction accuracy
- Balanced precision and recall metrics
- Strong performance on main event fights

## 🗂️ Repository Structure

```
ufc-fight-predictor/
├── data/                # Processed datasets (CSV)
├── ml_model/            # Trained models & notebooks
├── ufc_app/             # Django app
│   ├── templates/       # HTML pages
│   ├── views.py         # Prediction logic
│   └── models.py        # Database schema
├── manage.py
└── requirements.txt     # Dependencies
```

## 🏃‍♂️ Getting Started

### Prerequisites

- Python 3.8+
- Django 4.0+
- scikit-learn, pandas, numpy

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/ufc-fight-predictor.git
cd ufc-fight-predictor
```

2. Create a virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Run migrations
```bash
python manage.py migrate
```

4. Start the development server
```bash
python manage.py runserver
```

5. Navigate to `http://127.0.0.1:8000/` in your browser

## 📚 Dataset & Model Training

For details on the dataset and model training process, visit:
[Octagon Oracle](https://github.com/0xPsyop/Octagon-Oracle)
