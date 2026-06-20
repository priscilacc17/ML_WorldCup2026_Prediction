import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from predictor import (
    predict_match,
    generate_poisson_matrix,
    elo_dict
)

st.set_page_config(
    page_title="World Cup 2026 Predictor",
    layout="wide"
)

st.title("⚽ FIFA World Cup 2026 Predictor")

teams = sorted(
    list(elo_dict.keys())
)

col1, col2 = st.columns(2)

with col1:
    home_team = st.selectbox(
        "Team A",
        teams
    )

with col2:
    away_team = st.selectbox(
        "Team B",
        teams
    )

if home_team == away_team:
    st.warning(
        "Select two different teams."
    )
    st.stop()

if st.button("Predict Match"):

    result = predict_match(
        home_team,
        away_team
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            f"{home_team} Win",
            f"{result['prob_victoria_local']:.1f}%"
        )

    with col2:
        st.metric(
            "Draw",
            f"{result['prob_draw']:.1f}%"
        )

    with col3:
        st.metric(
            f"{away_team} Win",
            f"{result['prob_away_win']:.1f}%"
        )

    st.divider()

    c1, c2 = st.columns(2)

    with c1:
        st.subheader("Expected Goals")

        st.write(
            f"{home_team}: {result['lambda_home']:.2f}"
        )

        st.write(
            f"{away_team}: {result['lambda_away']:.2f}"
        )

        st.success(
            f"Most Likely Score: {result['probable_score']}"
        )

    with c2:
        st.subheader("Top 10 Scores")

        st.dataframe(
            result["top_10"],
            use_container_width=True
        )

    st.divider()

    matrix = generate_poisson_matrix(
        result["lambda_home"],
        result["lambda_away"]
    )

    st.subheader(
        "Poisson Goal Matrix (%)"
    )

    fig, ax = plt.subplots(
        figsize=(10, 8)
    )

    sns.heatmap(
        matrix,
        annot=True,
        fmt=".1f",
        cmap="Blues",
        ax=ax
    )

    ax.set_xlabel(away_team)
    ax.set_ylabel(home_team)

    st.pyplot(fig)

    st.subheader(
        "Poisson Matrix Table"
    )

    st.dataframe(
        pd.DataFrame(matrix),
        use_container_width=True
    )