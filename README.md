# ⚽ FIFA World Cup 2026 Match Prediction System

[![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-ML-green?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://xgboost.readthedocs.io/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Modeling-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

> Machine Learning project for predicting FIFA World Cup match outcomes using **XGBoost**, **Elo Ratings**, and **Poisson Goal Modeling**

<div align="center">
![Football Analytics](https://i.pinimg.com/736x/07/80/fe/0780fe9858f6613bcfe21600d2b7d160.jpg?w=800)
</div>

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@priscilacc17](https://github.com/priscilacc17/priscilacc17)
- Email: carrascalpriscila@gmail.com

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Dashboard Features](#-example-dashboard)
- [ML Pipeline](#️-machine-learning-pipeline)
- [Model Features](#-model-features)
- [Installation](#-installation--usage)
- [Example Output](#-example-prediction-output)
- [Poisson Matrix](#-poisson-goal-matrix)
- [Portfolio Value](#-portfolio-relevance)

---

## 🌎 Overview

This project is an **end-to-end Machine Learning system** designed to predict international football matches with a specific focus on FIFA World Cup scenarios.

### 🎯 Key Components

The pipeline combines:

- **Elo Rating calculations** from historical international matches
- **XGBoost Poisson regression models** for expected goals prediction
- **Poisson probability distributions** for scoreline simulation
- **Interactive Streamlit dashboard** for visualization

### 📊 Dataset

Trained using **49,000+ historical international matches** and generates realistic tournament-style predictions including:
- Score probabilities
- Match outcome distributions
- Confidence metrics

---

## 🏆 Example Dashboard

The interactive Streamlit application provides comprehensive match analysis:

| Feature | Description |
|---------|-------------|
| ⚡ **Expected Goals (xG)** | Predicted scoring output for each team based on historical patterns |
| 📊 **Win/Draw/Loss Probabilities** | Complete probability distribution for all possible match outcomes |
| 🎯 **Most Likely Scoreline** | Statistically most probable final score using Poisson modeling |
| 🏅 **Top 10 Predicted Results** | Ranked list of the most probable score combinations |
| 📈 **Poisson Goal Matrix** | Complete probability distribution for every realistic score combination |
| 🌡️ **Probability Heatmaps** | Visual representation of scoring probabilities and match dynamics |

---

## ⚙️ Machine Learning Pipeline

```
Historical International Matches
            ↓
     Elo Calculation
            ↓
   Feature Engineering
            ↓
  XGBoost Goal Prediction
            ↓
   Expected Goals (λ)
            ↓
    Poisson Simulation
            ↓
Match Outcome Probabilities
            ↓
   Interactive Dashboard
```

---

## 🧠 Model Features

| Feature | Description |
|---------|-------------|
| ⚡ **Elo Difference** | National team strength differential based on historical performance |
| 🌍 **Neutral Venue** | World Cup style neutral-site adjustment |
| 🏆 **Official Match Flag** | Distinguishes official competitions from friendly matches |
| ⭐ **World Cup Weighting** | Additional importance assigned to FIFA World Cup matches |
| 📈 **Expected Goals** | XGBoost-based prediction of team scoring output |
| 🎯 **Poisson Simulation** | Full probability distribution for every realistic scoreline |

---

## 🚀 Installation & Usage

### Prerequisites

- Python 3.12+
- pip (Python package manager)
- Git

### Clone Repository

```bash
git clone https://github.com/yourusername/worldcup-predictor.git
cd worldcup-predictor
```

### Create Virtual Environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Train Models

```bash
python train_model.py
```

This will:
- Load historical match data
- Calculate Elo ratings for all teams
- Engineer features for model training
- Train XGBoost models
- Save model artifacts

### Launch Interactive Dashboard

```bash
streamlit run app.py
```

The application will automatically open in your browser at:

```
http://localhost:8501
```

---

## 🎯 Example Prediction Output

### England vs Argentina

```
Expected Goals:
  England       1.42
  Argentina     1.19

Win Probability:
  England       41.3%
  Draw          27.5%
  Argentina     31.2%

Most Likely Score:
  1 - 1
```

---

## 📉 Poisson Goal Matrix

![Football Analytics](https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=1200)

The system generates a **complete probability matrix** for every realistic score combination, enabling:

- ✅ Detailed tournament simulations
- ✅ Match outcome analysis
- ✅ Confidence interval estimation
- ✅ Risk assessment for betting scenarios
- ✅ Strategic team analysis

---

## 💼 Portfolio Relevance

This project demonstrates expertise in:

### Machine Learning & AI
- 🤖 **Machine Learning Engineering** - XGBoost, model optimization, hyperparameter tuning
- 📊 **Predictive Analytics** - Probabilistic forecasting, confidence intervals
- 🧠 **Feature Engineering** - Domain-specific feature creation, Elo calculations

### Data Science
- 🔬 **Data Science** - Data cleaning, exploratory analysis, statistical modeling
- 📈 **Probabilistic Modeling** - Poisson distributions, probability theory applications
- ⚽ **Sports Analytics** - Domain expertise in football analytics

### Engineering & Deployment
- 🚀 **Model Deployment** - Streamlit applications, interactive dashboards
- 🏗️ **End-to-End ML Pipelines** - Data ingestion to production prediction
- 🔄 **Reproducible ML** - Version control, documentation, testing

---

## 📁 Project Structure

```
worldcup-predictor/
├── README.md
├── requirements.txt
├── data/
│   ├── matches.csv          # Historical match data
│   └── elo_ratings.csv      # Calculated Elo ratings
├── models/
│   ├── xgboost_home.pkl     # Home team goals model
│   └── xgboost_away.pkl     # Away team goals model
├── src/
│   ├── elo.py               # Elo calculation logic
│   ├── features.py          # Feature engineering
│   ├── models.py            # Model training
│   └── predictions.py       # Prediction functions
├── train_model.py           # Training script
└── app.py                   # Streamlit dashboard
```

---

## 🔧 Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Python 3.12** | Primary programming language |
| **XGBoost** | Gradient boosting for goal prediction |
| **Scikit-Learn** | Machine learning utilities and preprocessing |
| **Pandas** | Data manipulation and analysis |
| **NumPy** | Numerical computing |
| **Streamlit** | Interactive web dashboard |
| **Matplotlib/Seaborn** | Data visualization |

---

## 📈 Model Performance Metrics

The models achieve strong predictive performance through:

- ✅ **Cross-validation** - K-fold cross-validation for robustness
- ✅ **Hyperparameter Optimization** - Grid/Random search tuning
- ✅ **Feature Importance** - SHAP values for interpretability
- ✅ **Calibration** - Probability calibration for accurate confidence intervals

---

## 🎮 Interactive Features

### Dashboard Capabilities

- 🔍 **Match Search** - Find any international match prediction
- 🗓️ **Tournament Mode** - Simulate full tournament brackets
- 📊 **Statistical Analysis** - Detailed match breakdowns
- 🌍 **Team Comparison** - Head-to-head team analysis
- 📈 **Historical Trends** - Team form and Elo evolution
- 💾 **Export Results** - Download predictions as CSV

---

## 🚀 Quick Start Example

```python
from src.predictions import predict_match
from src.elo import load_elo_ratings

# Load team ratings
elo_ratings = load_elo_ratings()

# Predict a match
prediction = predict_match(
    home_team="England",
    away_team="Argentina",
    elo_ratings=elo_ratings,
    neutral_venue=True
)

# Access results
print(f"Home xG: {prediction['home_xg']:.2f}")
print(f"Away xG: {prediction['away_xg']:.2f}")
print(f"Win Probability: {prediction['home_win_prob']:.1%}")
print(f"Draw Probability: {prediction['draw_prob']:.1%}")
print(f"Loss Probability: {prediction['away_win_prob']:.1%}")
```

---

## 📚 References & Resources

- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [Poisson Distribution in Sports](https://en.wikipedia.org/wiki/Poisson_regression)
- [Elo Rating System](https://en.wikipedia.org/wiki/Elo_rating_system)
- [FIFA World Cup History](https://www.fifa.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

## 🤝 Contributing

Contributions are welcome! Please feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⭐ Show Your Support

Give a ⭐️ if this project helped you or you find it interesting!

---

## 🏆 Built with

**Python** • **XGBoost** • **Elo Ratings** • **Poisson Modeling** • **Streamlit** • **Machine Learning**

**FIFA World Cup 2026 Prediction System** ⚽

---

<div align="center">

![Football](https://images.unsplash.com/photo-1431324155629-1a6deb1dec8d?w=1200)

**Bringing Advanced Analytics to Football Predictions** 🎯

</div>
