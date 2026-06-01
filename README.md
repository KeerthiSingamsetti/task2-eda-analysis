# task2-eda-analysis
Task 2 of AI & ML Internship - Exploratory Data Analysis (EDA) using Pandas, Matplotlib, Seaborn, and Plotly on the Titanic dataset.

# Task 2 - Exploratory Data Analysis (EDA)

## Objective
Understand the dataset using statistics and visualizations to find patterns, trends, and relationships between features.

## Tools Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly

## Project Structure

task2-eda-analysis/

├── titanic.csv              
├── eda_task2.py             
├── README.md                

## Steps Performed

### Step 1 - Load Dataset
- Loaded the Titanic dataset using Pandas
- Displayed first few rows for initial understanding

### Step 2 - Basic Data Understanding
- Checked shape of dataset
- Checked data types of features
- Identified missing values
- Generated summary statistics using describe()

### Step 3 - Summary Statistics Analysis
- Calculated mean, median, and standard deviation for numerical features
- Helped understand data distribution

### Step 4 - Data Visualization (Histograms)
- Plotted histograms for all numerical features
- Observed distribution patterns of data

### Step 5 - Boxplots (Outlier Detection)
- Created boxplots for numerical features
- Identified presence of outliers in Age and Fare columns

### Step 6 - Correlation Analysis
- Generated correlation heatmap
- Identified relationships between numerical features

### Step 7 - Pairplot Analysis
- Used pairplot to visualize relationships between Age, Fare, Pclass, and Survived

### Step 8 - Interactive Visualization (Plotly)
- Created interactive histogram for Age vs Survival

## Dataset
- Source: Titanic Dataset
- Rows: 891
- Columns: 12

## Key Insights

- Most passengers are in the age range of 20–40
- Female passengers had higher survival rates than males
- Higher fare passengers had better chances of survival
- Age distribution is slightly right-skewed
- Some features like Pclass and Fare show correlation with survival

## Output
- Visual insights generated using histograms, boxplots, heatmap, and pairplot
- Interactive Plotly visualization for better understanding of data patterns
