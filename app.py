import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Video Games Sales Dashboard",
    page_icon="🎮",
    layout="wide"
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    return pd.read_csv(
        "Video_Games_Sales_as_at_22_Dec_2016.csv"
    )


df = load_data()


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

st.sidebar.title("🎮 Dashboard Navigation")

st.sidebar.write(
    "Use this sidebar to explore the video game sales dashboard."
)

st.sidebar.markdown("---")

section = st.sidebar.selectbox(
    "Dashboard Sections",
    [
        "🏠 Project Overview",
        "📊 Sales Analysis",
        "🎮 Games & Platforms",
        "⭐ Ratings & Reviews",
        "📅 Release Trends",
        "🏆 Top Games & Publishers",
        "📌 Key Findings"
    ]
)


# ============================================================
# MAIN TITLE
# ============================================================

st.title("🎮 Video Games Sales Dashboard")

st.write(
    "This dashboard explores video game sales, platforms, genres, "
    "ratings, reviews, publishers, and release years using the "
    "Video Games Sales dataset."
)


# ============================================================
# 1. PROJECT OVERVIEW
# ============================================================

if section == "🏠 Project Overview":

    # --------------------------------------------------------
    # ABOUT THE PROJECT
    # --------------------------------------------------------

    st.header("About the Project")

    st.write(
        "This project analyzes video game sales data to explore "
        "patterns and differences in game sales, genres, platforms, "
        "ratings, reviews, release years, and publishers."
    )

    st.write(
        "The main purpose of this analysis is to understand how "
        "video game sales vary across different categories and "
        "to identify important patterns within the available data."
    )


    # --------------------------------------------------------
    # DATASET USED
    # --------------------------------------------------------

    st.subheader("Dataset Used")

    st.write(
        "The analysis is based on the Video Games Sales dataset "
        "using the file:"
    )

    st.code(
        "Video_Games_Sales_as_at_22_Dec_2016.csv"
    )

    st.write(
        "The dataset contains 16,719 video game records and "
        "16 columns."
    )


    # --------------------------------------------------------
    # MAIN DATASET VARIABLES
    # --------------------------------------------------------

    st.subheader("Main Variables in the Dataset")

    st.markdown("""
    - **Name** – Game title
    - **Platform** – Gaming platform
    - **Year of Release** – Release year
    - **Genre** – Game genre
    - **Publisher** – Game publisher
    - **NA Sales** – Sales in North America
    - **EU Sales** – Sales in Europe
    - **JP Sales** – Sales in Japan
    - **Other Sales** – Sales in other regions
    - **Global Sales** – Worldwide sales
    - **Critic Score** – Professional critic score
    - **Critic Count** – Number of critic reviews
    - **User Score** – User rating
    - **User Count** – Number of user reviews
    - **Developer** – Game developer
    - **Rating** – ESRB rating
    """)


    # --------------------------------------------------------
    # WHAT DOES THE ANALYSIS MEASURE?
    # --------------------------------------------------------

    st.subheader("What Does the Analysis Measure?")

    st.markdown("""
    **📊 Game Distribution**

    - Number of games by genre
    - Number of games by platform
    - Number of games by ESRB rating

    **💰 Sales Performance**

    - Total global sales
    - Average sales per game
    - Median sales per game
    - Sales by genre, platform, year, rating, and publisher

    **⭐ Reviews and Ratings**

    - Critic score distribution
    - User score distribution
    - Relationship between scores and global sales

    **📅 Release Trends**

    - Number of games released by year
    - Total sales by year
    - Average sales by year
    - Median sales by year

    **🏆 Top Performers**

    - Top 10 best-selling games
    - Publishers with the highest total sales
    - Publishers with the highest average sales per game
    """)


    # --------------------------------------------------------
    # DATA PREPARATION
    # --------------------------------------------------------

    st.subheader("Data Preparation")

    st.write(
        "Before performing the analysis, the dataset was checked "
        "and cleaned by examining missing values, duplicate records, "
        "data types, and numerical fields."
    )

    st.write(
        'The "User_Score" field was converted to a numeric format, '
        'and "tbd" values were treated as missing values.'
    )

    st.write(
        "The analysis uses the available data for each specific "
        "calculation without inventing or generating missing values."
    )


    # --------------------------------------------------------
    # DATASET OVERVIEW
    # --------------------------------------------------------

    st.header("Dataset Overview")

    total_games = len(df)
    total_columns = len(df.columns)
    total_global_sales = df["Global_Sales"].sum()
    average_global_sales = df["Global_Sales"].mean()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Games",
            f"{total_games:,}"
        )

    with col2:
        st.metric(
            "Total Columns",
            f"{total_columns:,}"
        )

    with col3:
        st.metric(
            "Total Global Sales",
            f"{total_global_sales:,.2f} M"
        )

    with col4:
        st.metric(
            "Average Global Sales",
            f"{average_global_sales:.2f} M"
        )


    # --------------------------------------------------------
    # DATASET PREVIEW
    # --------------------------------------------------------

    st.header("Dataset Preview")

    st.write(
        "This table shows the first 10 records from the original dataset."
    )

    preview_df = df.head(10)

    st.markdown(
        preview_df.to_html(index=False),
        unsafe_allow_html=True
    )


# ============================================================
# 2. SALES ANALYSIS
# ============================================================

elif section == "📊 Sales Analysis":

    st.header("Sales Analysis")

    st.write(
        "This section examines the distribution and performance "
        "of global video game sales across different genres."
    )


    # --------------------------------------------------------
    # GLOBAL SALES DISTRIBUTION
    # --------------------------------------------------------

    st.header("Global Sales Distribution")

    st.write(
        "This histogram shows how global video game sales "
        "are distributed across the games in the dataset."
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.hist(
        df["Global_Sales"],
        bins=50
    )

    ax.set_title("Distribution of Global Sales")
    ax.set_xlabel("Global Sales (Millions)")
    ax.set_ylabel("Number of Games")

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


    # --------------------------------------------------------
    # TOTAL SALES BY GENRE
    # --------------------------------------------------------

    st.header("Total Global Sales by Genre")

    st.write(
        "This chart compares the total global sales generated "
        "by games in each genre."
    )

    genre_sales = (
        df.groupby("Genre")["Global_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    genre_sales.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Total Global Sales by Genre")
    ax.set_xlabel("Genre")
    ax.set_ylabel("Global Sales (Millions)")

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


    # --------------------------------------------------------
    # AVERAGE SALES BY GENRE
    # --------------------------------------------------------

    st.header("Average Global Sales per Game by Genre")

    st.write(
        "This chart shows the average global sales generated "
        "by an individual game within each genre."
    )

    genre_avg_sales = (
        df.groupby("Genre")["Global_Sales"]
        .mean()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    genre_avg_sales.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Average Global Sales per Game by Genre")
    ax.set_xlabel("Genre")
    ax.set_ylabel("Average Global Sales (Millions)")

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


    # --------------------------------------------------------
    # MEDIAN SALES BY GENRE
    # --------------------------------------------------------

    st.header("Median Global Sales per Game by Genre")

    st.write(
        "This chart shows the median global sales per game "
        "for each genre, reducing the influence of extreme values."
    )

    genre_median_sales = (
        df.groupby("Genre")["Global_Sales"]
        .median()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    genre_median_sales.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Median Global Sales per Game by Genre")
    ax.set_xlabel("Genre")
    ax.set_ylabel("Median Global Sales (Millions)")

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


# ============================================================
# 3. GAMES & PLATFORMS
# ============================================================

elif section == "🎮 Games & Platforms":

    st.header("Games & Platforms")

    st.write(
        "This section examines the distribution of games and "
        "their sales across different gaming platforms."
    )


    # --------------------------------------------------------
    # GENRE DISTRIBUTION
    # --------------------------------------------------------

    st.header("Genre Distribution")

    st.write(
        "This chart shows the number of video games available "
        "in the dataset for each genre."
    )

    genre_counts = (
        df["Genre"]
        .value_counts()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    genre_counts.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Number of Games by Genre")
    ax.set_xlabel("Genre")
    ax.set_ylabel("Number of Games")

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


    # --------------------------------------------------------
    # PLATFORM DISTRIBUTION
    # --------------------------------------------------------

    st.header("Platform Distribution")

    st.write(
        "This chart shows how many video games are available "
        "for each gaming platform in the dataset."
    )

    platform_counts = (
        df["Platform"]
        .value_counts()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(12, 6))

    platform_counts.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Number of Games by Platform")
    ax.set_xlabel("Platform")
    ax.set_ylabel("Number of Games")

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


    # --------------------------------------------------------
    # TOTAL SALES BY PLATFORM
    # --------------------------------------------------------

    st.header("Total Global Sales by Platform")

    st.write(
        "This chart compares the total global sales associated "
        "with each gaming platform."
    )

    platform_sales = (
        df.groupby("Platform")["Global_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(12, 6))

    platform_sales.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Total Global Sales by Platform")
    ax.set_xlabel("Platform")
    ax.set_ylabel("Global Sales (Millions)")

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


    # --------------------------------------------------------
    # AVERAGE SALES BY PLATFORM
    # --------------------------------------------------------

    st.header("Average Global Sales per Game by Platform")

    st.write(
        "This chart compares the average global sales per game "
        "across different gaming platforms."
    )

    platform_avg_sales = (
        df.groupby("Platform")["Global_Sales"]
        .mean()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(12, 6))

    platform_avg_sales.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Average Global Sales per Game by Platform")
    ax.set_xlabel("Platform")
    ax.set_ylabel("Average Global Sales (Millions)")

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


    # --------------------------------------------------------
    # MEDIAN SALES BY PLATFORM
    # --------------------------------------------------------

    st.header("Median Global Sales per Game by Platform")

    st.write(
        "This chart shows the median global sales per game "
        "for each platform and is less affected by extreme sales values."
    )

    platform_median_sales = (
        df.groupby("Platform")["Global_Sales"]
        .median()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(12, 6))

    platform_median_sales.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Median Global Sales per Game by Platform")
    ax.set_xlabel("Platform")
    ax.set_ylabel("Median Global Sales (Millions)")

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


# ============================================================
# 4. RATINGS & REVIEWS
# ============================================================

elif section == "⭐ Ratings & Reviews":

    st.header("Ratings & Reviews")

    st.write(
        "This section examines critic scores, user scores, "
        "and ESRB ratings and their relationship with sales."
    )


    # --------------------------------------------------------
    # CRITIC SCORE DISTRIBUTION
    # --------------------------------------------------------

    st.header("Critic Score Distribution")

    st.write(
        "This histogram shows the distribution of critic scores "
        "available for games in the dataset."
    )

    critic_scores = (
        pd.to_numeric(
            df["Critic_Score"],
            errors="coerce"
        )
        .dropna()
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.hist(
        critic_scores,
        bins=20
    )

    ax.set_title("Distribution of Critic Scores")
    ax.set_xlabel("Critic Score")
    ax.set_ylabel("Number of Games")

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


    # --------------------------------------------------------
    # USER SCORE DISTRIBUTION
    # --------------------------------------------------------

    st.header("User Score Distribution")

    st.write(
        "This histogram shows the distribution of user scores "
        "available for games in the dataset."
    )

    user_scores = (
        pd.to_numeric(
            df["User_Score"],
            errors="coerce"
        )
        .dropna()
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.hist(
        user_scores,
        bins=20
    )

    ax.set_title("Distribution of User Scores")
    ax.set_xlabel("User Score")
    ax.set_ylabel("Number of Games")

    ax.set_xticks(
        range(0, 11, 1)
    )

    ax.set_xlim(
        0,
        10
    )

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


    # --------------------------------------------------------
    # CRITIC SCORE VS GLOBAL SALES
    # --------------------------------------------------------

    st.header("Critic Score vs Global Sales")

    st.write(
        "This scatter plot examines the relationship between "
        "critic scores and global sales for games with available scores."
    )

    critic_sales = df[
        ["Critic_Score", "Global_Sales"]
    ].dropna()

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.scatter(
        critic_sales["Critic_Score"],
        critic_sales["Global_Sales"],
        alpha=0.5
    )

    ax.set_title("Critic Score vs Global Sales")
    ax.set_xlabel("Critic Score")
    ax.set_ylabel("Global Sales (Millions)")

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


    # --------------------------------------------------------
    # USER SCORE VS GLOBAL SALES
    # --------------------------------------------------------

    st.header("User Score vs Global Sales")

    st.write(
        "This scatter plot examines the relationship between "
        "user scores and global sales for games with available scores."
    )

    user_sales = df[
        ["User_Score", "Global_Sales"]
    ].copy()

    user_sales["User_Score"] = pd.to_numeric(
        user_sales["User_Score"],
        errors="coerce"
    )

    user_sales = user_sales.dropna()

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.scatter(
        user_sales["User_Score"],
        user_sales["Global_Sales"],
        alpha=0.5
    )

    ax.set_title("User Score vs Global Sales")
    ax.set_xlabel("User Score")
    ax.set_ylabel("Global Sales (Millions)")

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


    # --------------------------------------------------------
    # ESRB RATING DISTRIBUTION
    # --------------------------------------------------------

    st.header("ESRB Rating Distribution")

    st.write(
        "This chart shows the number of games associated with "
        "each available ESRB rating."
    )

    rating_counts = (
        df["Rating"]
        .dropna()
        .value_counts()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    rating_counts.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Number of Games by ESRB Rating")
    ax.set_xlabel("ESRB Rating")
    ax.set_ylabel("Number of Games")

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


    # --------------------------------------------------------
    # TOTAL SALES BY ESRB RATING
    # --------------------------------------------------------

    st.header("Total Global Sales by ESRB Rating")

    st.write(
        "This chart compares the total global sales of games "
        "for each available ESRB rating."
    )

    rating_sales = (
        df.dropna(subset=["Rating"])
        .groupby("Rating")["Global_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    rating_sales.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Total Global Sales by ESRB Rating")
    ax.set_xlabel("ESRB Rating")
    ax.set_ylabel("Global Sales (Millions)")

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


    # --------------------------------------------------------
    # AVERAGE SALES BY ESRB RATING
    # --------------------------------------------------------

    st.header("Average Global Sales per Game by ESRB Rating")

    st.write(
        "This chart compares the average global sales per game "
        "for each ESRB rating."
    )

    rating_avg_sales = (
        df.dropna(subset=["Rating"])
        .groupby("Rating")["Global_Sales"]
        .mean()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    rating_avg_sales.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Average Global Sales per Game by ESRB Rating")
    ax.set_xlabel("ESRB Rating")
    ax.set_ylabel("Average Global Sales (Millions)")

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


    # --------------------------------------------------------
    # MEDIAN SALES BY ESRB RATING
    # --------------------------------------------------------

    st.header("Median Global Sales per Game by ESRB Rating")

    st.write(
        "This chart shows the median global sales per game "
        "for each ESRB rating and reduces the influence of extreme values."
    )

    rating_median_sales = (
        df.dropna(subset=["Rating"])
        .groupby("Rating")["Global_Sales"]
        .median()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    rating_median_sales.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Median Global Sales per Game by ESRB Rating")
    ax.set_xlabel("ESRB Rating")
    ax.set_ylabel("Median Global Sales (Millions)")

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


# ============================================================
# 5. RELEASE TRENDS
# ============================================================

elif section == "📅 Release Trends":

    st.header("Release Trends")

    st.write(
        "This section examines how game releases and global sales "
        "changed across the release years available in the dataset."
    )


    # --------------------------------------------------------
    # TOTAL SALES BY YEAR
    # --------------------------------------------------------

    st.header("Total Global Sales by Year")

    st.write(
        "This chart shows the total global sales recorded in the "
        "dataset for each release year with available year information."
    )

    year_sales = (
        df.dropna(subset=["Year_of_Release"])
        .assign(
            Year_of_Release=lambda x:
            x["Year_of_Release"].astype(int)
        )
        .groupby("Year_of_Release")["Global_Sales"]
        .sum()
        .sort_index()
    )

    fig, ax = plt.subplots(figsize=(12, 6))

    year_sales.plot(
        kind="line",
        marker="o",
        ax=ax
    )

    ax.set_title("Total Global Sales by Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Global Sales (Millions)")

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


    # --------------------------------------------------------
    # NUMBER OF GAMES BY YEAR
    # --------------------------------------------------------

    st.header("Number of Games Released by Year")

    st.write(
        "This chart shows the number of games in the dataset "
        "for each release year with available year information."
    )

    year_counts = (
        df.dropna(subset=["Year_of_Release"])
        .assign(
            Year_of_Release=lambda x:
            x["Year_of_Release"].astype(int)
        )
        .groupby("Year_of_Release")
        .size()
        .sort_index()
    )

    fig, ax = plt.subplots(figsize=(12, 6))

    year_counts.plot(
        kind="line",
        marker="o",
        ax=ax
    )

    ax.set_title("Number of Games Released by Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Games")

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


    # --------------------------------------------------------
    # AVERAGE SALES BY YEAR
    # --------------------------------------------------------

    st.header("Average Global Sales per Game by Year")

    st.write(
        "This chart shows the average global sales per game "
        "for each release year with available year information."
    )

    year_avg_sales = (
        df.dropna(subset=["Year_of_Release"])
        .assign(
            Year_of_Release=lambda x:
            x["Year_of_Release"].astype(int)
        )
        .groupby("Year_of_Release")["Global_Sales"]
        .mean()
        .sort_index()
    )

    fig, ax = plt.subplots(figsize=(12, 6))

    year_avg_sales.plot(
        kind="line",
        marker="o",
        ax=ax
    )

    ax.set_title("Average Global Sales per Game by Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Average Global Sales (Millions)")

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


    # --------------------------------------------------------
    # MEDIAN SALES BY YEAR
    # --------------------------------------------------------

    st.header("Median Global Sales per Game by Year")

    st.write(
        "This chart shows the median global sales per game "
        "for each release year and reduces the effect of extreme values."
    )

    year_median_sales = (
        df.dropna(subset=["Year_of_Release"])
        .assign(
            Year_of_Release=lambda x:
            x["Year_of_Release"].astype(int)
        )
        .groupby("Year_of_Release")["Global_Sales"]
        .median()
        .sort_index()
    )

    fig, ax = plt.subplots(figsize=(12, 6))

    year_median_sales.plot(
        kind="line",
        marker="o",
        ax=ax
    )

    ax.set_title("Median Global Sales per Game by Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Median Global Sales (Millions)")

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


# ============================================================
# 6. TOP GAMES & PUBLISHERS
# ============================================================

elif section == "🏆 Top Games & Publishers":

    st.header("Top Games & Publishers")

    st.write(
        "This section highlights the best-selling games and "
        "publishers based on the available global sales data."
    )


    # --------------------------------------------------------
    # TOP 10 GAMES
    # --------------------------------------------------------

    st.header("Top 10 Best-Selling Games")

    st.write(
        "This table lists the ten games with the highest recorded "
        "global sales in the dataset."
    )

    top_games = (
        df[
            [
                "Name",
                "Platform",
                "Year_of_Release",
                "Genre",
                "Publisher",
                "Global_Sales"
            ]
        ]
        .sort_values(
            "Global_Sales",
            ascending=False
        )
        .head(10)
        .copy()
    )

    st.markdown(
        top_games.to_html(index=False),
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # TOTAL SALES BY PUBLISHER
    # --------------------------------------------------------

    st.header("Total Global Sales by Publisher")

    st.write(
        "This chart shows the publishers with the highest total "
        "global sales across their games in the dataset."
    )

    publisher_sales = (
        df.dropna(subset=["Publisher"])
        .groupby("Publisher")["Global_Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig, ax = plt.subplots(figsize=(12, 6))

    publisher_sales.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Top 10 Publishers by Total Global Sales")
    ax.set_xlabel("Publisher")
    ax.set_ylabel("Global Sales (Millions)")

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


    # --------------------------------------------------------
    # AVERAGE SALES BY PUBLISHER
    # --------------------------------------------------------

    st.header("Average Global Sales per Game by Publisher")

    st.write(
        "This chart compares average global sales per game among "
        "publishers with at least 20 games in the dataset."
    )

    publisher_stats = (
        df.dropna(subset=["Publisher"])
        .groupby("Publisher")["Global_Sales"]
        .agg(["mean", "count"])
    )

    publisher_avg_sales = (
        publisher_stats[
            publisher_stats["count"] >= 20
        ]["mean"]
        .sort_values(ascending=False)
        .head(10)
    )

    fig, ax = plt.subplots(figsize=(12, 6))

    publisher_avg_sales.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title(
        "Top 10 Publishers by Average Global Sales per Game "
        "(Minimum 20 Games)"
    )

    ax.set_xlabel("Publisher")
    ax.set_ylabel("Average Global Sales (Millions)")

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


# ============================================================
# 7. KEY FINDINGS
# ============================================================

elif section == "📌 Key Findings":

    st.header("Key Findings Summary")

    st.write(
        "The following points summarize the main descriptive findings "
        "identified from the dataset."
    )


    # --------------------------------------------------------
    # BASIC DATASET INFORMATION
    # --------------------------------------------------------

    total_games = len(df)

    total_columns = len(df.columns)

    missing_years = int(
        df["Year_of_Release"].isna().sum()
    )

    missing_ratings = int(
        df["Rating"].isna().sum()
    )


    # --------------------------------------------------------
    # GENRE FINDINGS
    # --------------------------------------------------------

    genre_counts_summary = (
        df["Genre"]
        .value_counts()
    )

    most_common_genre = (
        genre_counts_summary
        .idxmax()
    )

    most_common_genre_count = int(
        genre_counts_summary
        .max()
    )

    genre_total_sales_summary = (
        df.groupby("Genre")["Global_Sales"]
        .sum()
    )

    highest_sales_genre = (
        genre_total_sales_summary
        .idxmax()
    )

    highest_sales_genre_value = (
        genre_total_sales_summary
        .max()
    )

    genre_average_sales_summary = (
        df.groupby("Genre")["Global_Sales"]
        .mean()
    )

    highest_avg_genre = (
        genre_average_sales_summary
        .idxmax()
    )

    highest_avg_genre_value = (
        genre_average_sales_summary
        .max()
    )


    # --------------------------------------------------------
    # PLATFORM FINDINGS
    # --------------------------------------------------------

    platform_counts_summary = (
        df["Platform"]
        .value_counts()
    )

    most_common_platform = (
        platform_counts_summary
        .idxmax()
    )

    most_common_platform_count = int(
        platform_counts_summary
        .max()
    )

    platform_total_sales_summary = (
        df.groupby("Platform")["Global_Sales"]
        .sum()
    )

    highest_sales_platform = (
        platform_total_sales_summary
        .idxmax()
    )

    highest_sales_platform_value = (
        platform_total_sales_summary
        .max()
    )


    # --------------------------------------------------------
    # GLOBAL SALES STATISTICS
    # --------------------------------------------------------

    mean_global_sales = (
        df["Global_Sales"]
        .mean()
    )

    median_global_sales = (
        df["Global_Sales"]
        .median()
    )

    max_global_sales = (
        df["Global_Sales"]
        .max()
    )


    # --------------------------------------------------------
    # TOP GAME
    # --------------------------------------------------------

    top_game = (
        df.loc[
            df["Global_Sales"].idxmax(),
            "Name"
        ]
    )


    # --------------------------------------------------------
    # PUBLISHER
    # --------------------------------------------------------

    publisher_total_sales_summary = (
        df.dropna(subset=["Publisher"])
        .groupby("Publisher")["Global_Sales"]
        .sum()
    )

    top_publisher = (
        publisher_total_sales_summary
        .idxmax()
    )


    # --------------------------------------------------------
    # CRITIC SCORE CORRELATION
    # --------------------------------------------------------

    critic_sales_corr = (
        df[
            ["Critic_Score", "Global_Sales"]
        ]
        .dropna()
        .corr()
        .loc[
            "Critic_Score",
            "Global_Sales"
        ]
    )


    # --------------------------------------------------------
    # USER SCORE CORRELATION
    # --------------------------------------------------------

    user_corr_df = df[
        ["User_Score", "Global_Sales"]
    ].copy()

    user_corr_df["User_Score"] = pd.to_numeric(
        user_corr_df["User_Score"],
        errors="coerce"
    )

    user_sales_corr = (
        user_corr_df
        .dropna()
        .corr()
        .loc[
            "User_Score",
            "Global_Sales"
        ]
    )


    # --------------------------------------------------------
    # ESRB
    # --------------------------------------------------------

    rating_counts_summary = (
        df["Rating"]
        .dropna()
        .value_counts()
    )

    most_common_rating = (
        rating_counts_summary
        .idxmax()
    )

    most_common_rating_count = int(
        rating_counts_summary
        .max()
    )


    # --------------------------------------------------------
    # YEAR
    # --------------------------------------------------------

    year_sales_summary = (
        df.dropna(
            subset=["Year_of_Release"]
        )
        .assign(
            Year_of_Release=lambda x:
            x["Year_of_Release"].astype(int)
        )
        .groupby(
            "Year_of_Release"
        )["Global_Sales"]
        .sum()
    )

    highest_sales_year = (
        year_sales_summary
        .idxmax()
    )

    highest_sales_year_value = (
        year_sales_summary
        .max()
    )

    year_release_counts = (
        df.dropna(
            subset=["Year_of_Release"]
        )
        .assign(
            Year_of_Release=lambda x:
            x["Year_of_Release"].astype(int)
        )
        .groupby(
            "Year_of_Release"
        )
        .size()
    )

    highest_release_year = (
        year_release_counts
        .idxmax()
    )

    highest_release_count = int(
        year_release_counts
        .max()
    )


    # --------------------------------------------------------
    # DISPLAY SUMMARY
    # --------------------------------------------------------

    st.write(
        f"• The dataset contains {total_games:,} games "
        f"across {total_columns} columns."
    )

    st.write(
        f"• {missing_years:,} games have missing release-year "
        f"information, and {missing_ratings:,} games have "
        f"missing ESRB ratings."
    )

    st.write(
        f"• {most_common_genre} is the most represented genre, "
        f"with {most_common_genre_count:,} games."
    )

    st.write(
        f"• {highest_sales_genre} has the highest total global "
        f"sales, with {highest_sales_genre_value:,.2f} million."
    )

    st.write(
        f"• The {highest_avg_genre} genre has the highest average "
        f"global sales per game, at "
        f"{highest_avg_genre_value:.2f} million."
    )

    st.write(
        f"• {most_common_platform} is the most represented platform, "
        f"with {most_common_platform_count:,} games."
    )

    st.write(
        f"• {highest_sales_platform} has the highest total platform "
        f"sales, with {highest_sales_platform_value:,.2f} million."
    )

    st.write(
        f"• Global sales have a mean of "
        f"{mean_global_sales:.2f} million and a median of "
        f"{median_global_sales:.2f} million."
    )

    st.write(
        f"• The highest recorded global sales value is "
        f"{max_global_sales:.2f} million for {top_game}."
    )

    st.write(
        f"• The Pearson correlation between critic score and "
        f"global sales is {critic_sales_corr:.3f}."
    )

    st.write(
        f"• The Pearson correlation between user score and "
        f"global sales is {user_sales_corr:.3f}."
    )

    st.write(
        f"• {most_common_rating} is the most common ESRB rating, "
        f"with {most_common_rating_count:,} games."
    )

    st.write(
        f"• {highest_sales_year} has the highest total recorded "
        f"global sales among years with available year information, "
        f"at {highest_sales_year_value:,.2f} million."
    )

    st.write(
        f"• {highest_release_year} has the highest number of games "
        f"in the dataset, with {highest_release_count:,} releases."
    )

    st.write(
        f"• {top_publisher} has the highest total global sales "
        f"among publishers with available publisher information."
    )

    st.write(
        "• Overall, the analysis shows substantial differences "
        "in sales across genres, platforms, years, ratings, and "
        "publishers. Total sales, average sales, and median sales "
        "provide different views of the dataset."
    )
