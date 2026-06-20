import joblib
import pandas as pd
import numpy as np
from scipy.stats import poisson

home_model = joblib.load("models/home_model.pkl")
away_model = joblib.load("models/away_model.pkl")
elo_dict = joblib.load("models/elo.pkl")


def predict_match(
    home_team,
    away_team,
    home_model=home_model,
    away_model=away_model,
    elo=elo_dict,
    neutral=True,
    max_goals=10
):

    home_elo = elo[home_team]
    away_elo = elo[away_team]

    elo_diff = home_elo - away_elo

    match = pd.DataFrame({
        "elo_diff": [elo_diff],
        "neutral": [1],
        "official_match": [1],
        "world_cup_match": [1]
    })

    lambda_home = max(
        0.01,
        float(home_model.predict(match)[0])
    )

    lambda_away = max(
        0.01,
        float(away_model.predict(match)[0])
    )

    world_cup_factor = 0.90

    lambda_home *= world_cup_factor
    lambda_away *= world_cup_factor

    scores = []

    for i in range(max_goals + 1):
        for j in range(max_goals + 1):

            prob = (
                poisson.pmf(i, lambda_home)
                * poisson.pmf(j, lambda_away)
            )

            scores.append({
                "score": f"{i}-{j}",
                "prob": prob,
                "home_goals": i,
                "away_goals": j
            })

    scores_df = pd.DataFrame(scores)

    scores_df = scores_df.sort_values(
        "prob",
        ascending=False
    )

    prob_home_win = scores_df[
        scores_df["home_goals"] >
        scores_df["away_goals"]
    ]["prob"].sum()

    prob_draw = scores_df[
        scores_df["home_goals"] ==
        scores_df["away_goals"]
    ]["prob"].sum()

    prob_away_win = scores_df[
        scores_df["home_goals"] <
        scores_df["away_goals"]
    ]["prob"].sum()

    probable_score = (
        scores_df.iloc[0]["score"]
    )

    top_10 = (
        scores_df[["score", "prob"]]
        .head(10)
        .copy()
    )

    top_10["prob"] *= 100

    return {
        "lambda_home": lambda_home,
        "lambda_away": lambda_away,
        "prob_victoria_local": prob_home_win * 100,
        "prob_draw": prob_draw * 100,
        "prob_away_win": prob_away_win * 100,
        "probable_score": probable_score,
        "top_10": top_10,
        "scores_df": scores_df
    }


def generate_poisson_matrix(
    lambda_home,
    lambda_away,
    max_goals=10
):

    matrix = np.zeros(
        (max_goals + 1, max_goals + 1)
    )

    for i in range(max_goals + 1):
        for j in range(max_goals + 1):

            matrix[i, j] = (
                poisson.pmf(i, lambda_home)
                * poisson.pmf(j, lambda_away)
            ) * 100

    return matrix