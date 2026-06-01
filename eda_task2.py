import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# ================================
# STEP 1 - LOAD DATA
# ================================
def step1_load():
    print("="*50)
    print("STEP 1 - LOADING DATA")
    print("="*50)

    df = pd.read_csv("titanic.csv")
    print(df.head())
    return df


# ================================
# STEP 2 - BASIC UNDERSTANDING
# ================================
def step2_understand(df):
    print("\nSTEP 2 - BASIC INFO")

    print("\nShape:", df.shape)
    print("\nInfo:")
    print(df.info())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nStatistics:")
    print(df.describe())

    return df


# ================================
# STEP 3 - SUMMARY STATISTICS INSIGHTS
# ================================
def step3_stats(df):
    print("\nSTEP 3 - STATISTICS ANALYSIS")

    print("\nMean values:")
    print(df.mean(numeric_only=True))

    print("\nMedian values:")
    print(df.median(numeric_only=True))

    print("\nStandard deviation:")
    print(df.std(numeric_only=True))


# ================================
# STEP 4 - HISTOGRAMS
# ================================
def step4_histograms(df):
    print("\nSTEP 4 - HISTOGRAMS")

    df.hist(figsize=(10,6))
    plt.suptitle("Feature Distributions")
    plt.show()


# ================================
# STEP 5 - BOXPLOTS (OUTLIERS VIEW)
# ================================
def step5_boxplots(df):
    print("\nSTEP 5 - BOXPLOTS")

    numeric_cols = df.select_dtypes(include=np.number).columns

    for col in numeric_cols:
        plt.figure()
        sns.boxplot(x=df[col])
        plt.title(f"Boxplot of {col}")
        plt.show()


# ================================
# STEP 6 - CORRELATION MATRIX
# ================================
def step6_correlation(df):
    print("\nSTEP 6 - CORRELATION MATRIX")

    plt.figure(figsize=(10,6))
    sns.heatmap(df.corr(numeric_only=True),
                annot=True,
                cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()


# ================================
# STEP 7 - PAIRPLOT
# ================================
def step7_pairplot(df):
    print("\nSTEP 7 - PAIRPLOT")

    sns.pairplot(df[['Age', 'Fare', 'Pclass', 'Survived']])
    plt.show()


# ================================
# STEP 8 - PLOTLY VISUAL (OPTIONAL BONUS)
# ================================
def step8_plotly(df):
    print("\nSTEP 8 - INTERACTIVE PLOT")

    fig = px.histogram(df, x="Age", color="Survived")
    fig.show()


# ================================
# STEP 9 - INSIGHTS
# ================================
def step9_insights():
    print("\nSTEP 9 - INSIGHTS")

    print("""
    1. Most passengers are in age range 20–40
    2. Females have higher survival rate
    3. Higher fare passengers survived more
    4. Age distribution is slightly right-skewed
    5. Some features are strongly correlated
    """)


# ================================
# MAIN PIPELINE
# ================================
def main():
    df = step1_load()
    df = step2_understand(df)
    step3_stats(df)
    step4_histograms(df)
    step5_boxplots(df)
    step6_correlation(df)
    step7_pairplot(df)
    step8_plotly(df)
    step9_insights()

    print("\n✅ TASK 2 COMPLETED")


main()