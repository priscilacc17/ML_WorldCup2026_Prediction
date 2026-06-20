<div align="center">

<h1>⚽ FIFA World Cup 2026 Match Prediction System</h1>

<p>
Machine Learning project for predicting FIFA World Cup match outcomes using
<b>XGBoost</b>, <b>Elo Ratings</b>, and <b>Poisson Goal Modeling</b>.
</p>

<img src="https://i.pinimg.com/736x/07/80/fe/0780fe9858f6613bcfe21600d2b7d160.jpg" width="600"/>

<br><br>

<img src="https://img.shields.io/badge/Python-3.12-blue"/>
<img src="https://img.shields.io/badge/XGBoost-ML-green"/>
<img src="https://img.shields.io/badge/Streamlit-Dashboard-red"/>
<img src="https://img.shields.io/badge/Scikit--Learn-Modeling-orange"/>
<img src="https://img.shields.io/badge/License-MIT-lightgrey"/>

</div>

---

## 🌎 Overview

This project is an end-to-end Machine Learning system designed to predict international football matches with a specific focus on FIFA World Cup scenarios.

The pipeline combines:

<ul>
<li>Elo Rating calculations from historical international matches</li>
<li>XGBoost Poisson regression models for expected goals prediction</li>
<li>Poisson probability distributions for scoreline simulation</li>
<li>Interactive Streamlit dashboard for visualization</li>
</ul>

The model is trained using more than <b>49,000 historical international matches</b> and generates realistic tournament-style predictions including score probabilities and match outcome distributions.

---

## 🏆 Example Dashboard

<div align="center">

<img src="https://images.unsplash.com/photo-1517466787929-bc90951d0974?w=1200" align="right" alt="goal" />

</div>

The application provides:

<ul>
<li>Expected goals (xG)</li>
<li>Win / Draw / Loss probabilities</li>
<li>Most likely scoreline</li>
<li>Top 10 predicted results</li>
<li>Poisson goal matrix</li>
<li>Probability heatmaps</li>
</ul>

---

## ⚙️ Machine Learning Pipeline

```text
Historical International Matches
                │
                ▼
         Elo Calculation
                │
                ▼
      Feature Engineering
                │
                ▼
     XGBoost Goal Prediction
                │
                ▼
      Expected Goals (λ)
                │
                ▼
       Poisson Simulation
                │
                ▼
 Match Outcome Probabilities
                │
                ▼
      Interactive Dashboard
```

---

## 🧠 Model Features

<table>
<tr>
<th>Feature</th>
<th>Description</th>
</tr>

<tr>
<td>Elo Difference</td>
<td>Strength differential between national teams</td>
</tr>

<tr>
<td>Neutral Venue</td>
<td>World Cup style neutral-site adjustment</td>
</tr>

<tr>
<td>Official Match Flag</td>
<td>Differentiates official competitions from friendlies</td>
</tr>

<tr>
<td>World Cup Flag</td>
<td>Additional weighting for World Cup matches</td>
</tr>

</table>

---

## 📊 Technologies

<table>
<tr>
<td>Python</td>
<td>XGBoost</td>
<td>Scikit-Learn</td>
</tr>

<tr>
<td>Pandas</td>
<td>NumPy</td>
<td>SciPy</td>
</tr>

<tr>
<td>Streamlit</td>
<td>Matplotlib</td>
<td>Seaborn</td>
</tr>

<tr>
<td>Joblib</td>
<td>Elo Ratings</td>
<td>Poisson Models</td>
</tr>

</table>

---

## 📁 Project Structure

```text
worldcup_predictor/
│
├── app.py
├── predictor.py
├── train_model.py
├── requirements.txt
│
├── data/
│   └── results.csv
│
└── models/
    ├── home_model.pkl
    ├── away_model.pkl
    └── elo.pkl
```

---

## 🚀 Installation

```bash
git clone https://github.com/yourusername/worldcup-predictor.git

cd worldcup-predictor

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt
```

---

## 🏗️ Train Models

```bash
python train_model.py
```

Generated artifacts:

```text
models/
├── home_model.pkl
├── away_model.pkl
└── elo.pkl
```

---

## 📈 Launch Dashboard

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 🎯 Example Prediction Output

```text
England vs Argentina

Expected Goals:
England     1.42
Argentina   1.19

Win Probability:
England     41.3%
Draw        27.5%
Argentina   31.2%

Most Likely Score:
1 - 1
```

---

## 📉 Poisson Goal Matrix

<div align="center">

<img src="https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=1200" width="850"/>

</div>

The system generates a complete Poisson probability matrix for all realistic score combinations, allowing detailed match simulation and outcome analysis.

---

## 💼 Portfolio Relevance

This project demonstrates practical experience in:

<ul>
<li>Machine Learning Engineering</li>
<li>Feature Engineering</li>
<li>Predictive Modeling</li>
<li>Sports Analytics</li>
<li>Probabilistic Modeling</li>
<li>MLOps Fundamentals</li>
<li>Model Serialization and Deployment</li>
<li>Interactive Data Applications</li>
</ul>

---

## 📄 License

MIT License

---

<div align="center">

<b>Built with Python, XGBoost, Elo Ratings and Poisson Modeling ⚽</b>

</div>
