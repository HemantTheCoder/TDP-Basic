# Titanic Dataset Preprocessing
This repository provides a Python script for preprocessing the Titanic dataset. The Titanic dataset is a classic dataset often used for machine learning and data analysis projects. The script in this repository performs various preprocessing steps to handle missing values and prepare the data for further analysis.

# Dataset Overview
The Titanic dataset contains information about passengers aboard the Titanic, including details such as age, class, ticket fare, and whether the passenger survived or not. The dataset is loaded into a pandas DataFrame, and different preprocessing techniques are applied to clean and enhance the data.

# Preprocessing Steps
Exploratory Data Analysis (EDA): Initial exploration of the dataset is performed, providing insights into the structure and characteristics of the data.

# Handling Missing Values:

Rows with missing values are removed in one copy of the dataset.
Columns with missing values are dropped in another copy of the dataset.

# Imputing Missing Values:

Missing values in the "Age" column are replaced with a specific value in one copy of the dataset.
Missing values in the "Age" column are replaced with the mean value, and missing values in the "Cabin" and "Embarked" columns are replaced with the mode in another copy.

# Conditional Imputation:
Missing values in the "Age" column are replaced with the mean value based on conditions, such as whether the passenger survived or not.

# Usage

**Clone the repository:**

git clone https://https://github.com/HemantTheCoder/TDP-Basic

**Navigate to the project directory:**
cd TDP-Basic

**Run the preprocessing script:**
python missing_data_correction.py

Feel free to use and adapt the code to suit your needs. 
**Contributions and feedback are encouraged!**
~~
# Dependencies
    Python 3
    pandas
    numpy
    statistics

# License
This project is licensed under the MIT License.
