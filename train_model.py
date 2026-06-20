import pandas as pd
import numpy as np
from collections import defaultdict
from xgboost import XGBRegressor
import joblib
import warnings

warnings.filterwarnings("ignore")

print("Loading data...")

results = pd.read_csv("data/results.csv")

print(f"✓ Load data: {results.shape[0]} games")

results["date"] = pd.to_datetime(results["date"])


def calculate_elo(df, K=20):

    elo = defaultdict(lambda: 1500)

    df = df.copy()

    df["home_elo"] = 0.0
    df["away_elo"] = 0.0

    for idx, row in df.iterrows():

        home = row["home_team"]
        away = row["away_team"]

        home_elo = elo[home]
        away_elo = elo[away]

        df.at[idx, "home_elo"] = home_elo
        df.at[idx, "away_elo"] = away_elo

        expected_home = 1 / (
            1 + 10 ** ((away_elo - home_elo) / 400)
        )

        expected_away = 1 - expected_home

        if row["home_score"] > row["away_score"]:
            actual_home = 1
            actual_away = 0

        elif row["home_score"] < row["away_score"]:
            actual_home = 0
            actual_away = 1

        else:
            actual_home = 0.5
            actual_away = 0.5

        importance = 1.0

        tournament = str(row.get("tournament", "")).lower()

        if "world cup" in tournament:
            importance = 1.8
        elif "euro" in tournament:
            importance = 1.5
        elif "copa américa" in tournament:
            importance = 1.5
        elif "nations league" in tournament:
            importance = 1.3
        elif "qualif" in tournament:
            importance = 1.2

        elo[home] += K * importance * (
            actual_home - expected_home
        )

        elo[away] += K * importance * (
            actual_away - expected_away
        )

    return df, elo


print("Calculating Elo...")

results, elo_dict = calculate_elo(results)

print("✓ Calculated Elo")

results["elo_diff"] = (
    results["home_elo"] - results["away_elo"]
)

results["neutral"] = (
    results["neutral"]
    .astype(int)
)

results["world_cup_match"] = (
    results["tournament"]
    .fillna("")
    .str.contains("World Cup", case=False)
    .astype(int)
)

results["official_match"] = (
    ~results["tournament"]
    .fillna("")
    .str.contains("Friendly", case=False)
).astype(int)

features = [
    "elo_diff",
    "neutral",
    "official_match",
    "world_cup_match"
]

train = results[
    results["date"] < "2024-01-01"
]

test = results[
    results["date"] >= "2024-01-01"
]

print(f"✓ Train: {len(train)} games")
print(f"✓ Test: {len(test)} games")

X_train = train[features]

y_home_train = train["home_score"]
y_away_train = train["away_score"]

xgb_params = {
    "objective": "count:poisson",
    "n_estimators": 500,
    "max_depth": 5,
    "learning_rate": 0.03,
    "subsample": 0.9,
    "colsample_bytree": 0.9,
    "random_state": 42,
    "verbosity": 0
}

print("Training local model...")

home_model = XGBRegressor(**xgb_params)

home_model.fit(
    X_train,
    y_home_train
)

print("✓ Trained local model")

print("Training visitor model...")

away_model = XGBRegressor(**xgb_params)

away_model.fit(
    X_train,
    y_away_train
)

print("✓ Trained visiting model")

joblib.dump(
    home_model,
    "models/home_model.pkl"
)

joblib.dump(
    away_model,
    "models/away_model.pkl"
)

joblib.dump(
    dict(elo_dict),
    "models/elo.pkl"
)

print("\n✓ Saved models")