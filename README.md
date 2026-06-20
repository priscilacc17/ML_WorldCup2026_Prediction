<div align="center">

<h1>⚽ FIFA World Cup 2026 Match Prediction System</h1>

<p>
Machine Learning project for predicting FIFA World Cup match outcomes using
<b>XGBoost</b>, <b>Elo Ratings</b>, and <b>Poisson Goal Modeling</b>

</p>

<br><img src="https://img.shields.io/badge/Python-3.12-blue"/>
<img src="https://img.shields.io/badge/XGBoost-ML-green"/>
<img src="https://img.shields.io/badge/Streamlit-Dashboard-red"/>
<img src="https://img.shields.io/badge/Scikit--Learn-Modeling-orange"/>
<img src="https://img.shields.io/badge/License-MIT-lightgrey"/></br>

<img src="https://i.pinimg.com/736x/07/80/fe/0780fe9858f6613bcfe21600d2b7d160.jpg" width="800"/>

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

<div align="center">
  
<div align="center">

# 🧠 Model Features

<br>

<table>
<tr>
<th>Feature</th>
<th>Description</th>
</tr>

<tr>
<td>⚡ Elo Difference</td>
<td>National team strength differential based on historical performance</td>
</tr>

<tr>
<td>🌍 Neutral Venue</td>
<td>World Cup style neutral-site adjustment</td>
</tr>

<tr>
<td>🏆 Official Match Flag</td>
<td>Distinguishes official competitions from friendly matches</td>
</tr>

<tr>
<td>⭐ World Cup Weighting</td>
<td>Additional importance assigned to FIFA World Cup matches</td>
</tr>

<tr>
<td>📈 Expected Goals</td>
<td>XGBoost-based prediction of team scoring output</td>
</tr>

<tr>
<td>🎯 Poisson Simulation</td>
<td>Full probability distribution for every realistic scoreline</td>
</tr>

</table>

</div>

---

<div align="center">

# 🚀 Installation & Usage
</div>

```bash
git clone https://github.com/yourusername/worldcup-predictor.git

cd worldcup-predictor

python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

pip install -r requirements.txt
```

### Train Models

```bash
python train_model.py
```

### Launch Dashboard

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

<div align="center">

# 🎯 Example Prediction Output

</div>

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

<div align="center">

# 📉 Poisson Goal Matrix

<br>

<img src="https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=1200" width="850"/>

<br><br>

The system generates a complete probability matrix for every realistic score combination,
allowing detailed tournament simulations and match outcome analysis.

</div>

---

<div align="center">

# 💼 Portfolio Relevance

<br>

<table>
<tr>
<td>🤖 Machine Learning Engineering</td>
<td>📊 Predictive Analytics</td>
</tr>

<tr>
<td>⚽ Sports Analytics</td>
<td>🧠 Feature Engineering</td>
</tr>

<tr>
<td>📈 Probabilistic Modeling</td>
<td>🚀 Model Deployment</td>
</tr>

<tr>
<td>🔬 Data Science</td>
<td>🏗️ End-to-End ML Pipelines</td>
</tr>

</table>

</div>

---

<div align="center">

# 📄 License

MIT License

<br><br>

<img src="https://images.unsplash.com/photo-1431324155629-1a6deb1dec8d?w=1200" width="900"/>

<br><br>

<h2>⚽ Built with Python, XGBoost, Elo Ratings & Poisson Modeling</h2>

<h3>FIFA World Cup 2026 Prediction System</h3>

</div>
