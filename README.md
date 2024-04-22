# Cancer Incidence Analysis Project 🎗️
## Overview 📄🧐
This repository contains data, analysis scripts, and visualization tools used in the Cancer Incidence Analysis Project. The goal of this project is to explore the relationship between socioeconomic factors, healthcare coverage, and cancer incidence rates across different states in the U.S.

## Data 📄🤓
The dataset used in this project (cancer_reg.csv) includes various demographic, socioeconomic, and health-related metrics such as median income, population estimates, health insurance coverage percentages, and cancer incidence rates.
### Visualizations - Tableau Public https://public.tableau.com/app/profile/fernando.amaya7973/viz/CancerCasesAnalysis/Dashboard1
Created heatmaps, scatter plots, and bar charts using Tableau to visualize complex relationships in the data.
Added reference lines to scatter plots to compare individual states against the average incidence rate. 

## Process ⚙️
### Understanding the Data
Initial examination of the dataset to understand the variables and the structure of the data.
Checked for the completeness and consistency of the data across various fields.
### Cleaning the Data
Removed duplicate records to ensure the uniqueness of each entry.
Dropped unnecessary columns, specifically those with a high percentage of missing data.
Standardized column names for consistency and readability.
### Imputing Missing Values
Calculated the mean or median (where appropriate) for columns with missing values and imputed these to maintain the integrity of the dataset.
Ensured that the imputation did not introduce any bias or skew the data distribution.
### Checking for Inconsistencies
Validated that numeric data fell within logical ranges (e.g., age between 0 and 110).
Confirmed that categorical data entries matched the expected set of categories.
### Exploratory Data Analysis (EDA)
Visualized data distributions using histograms, box plots, and bar charts.
Identified and addressed outliers using statistical techniques.
### Adding New Columns
Extracted the state and county information from the geography field to allow for more granular analysis.
### Statistical Analysis
Calculated the incidence rate per 100,000 people to standardize across states with varying population sizes.
Analyzed the correlation between median income and cancer incidence rates using scatter plots and calculated Pearson correlation coefficients to quantify the relationships.

### Insights
Identified a positive correlation between median income and cancer incidence rates, suggesting higher diagnosis rates in wealthier states, potentially due to better access to healthcare or more comprehensive reporting.
Explored how public healthcare coverage may affect cancer detection rates.
### Repository Structure
/data: Contains the raw data and processed datasets.
/scripts: Includes all data preprocessing and analysis scripts.
/visualizations: Contains Tableau workbook files and other visualization outputs.
/docs: Documentation related to the project.
### How to Use This Repository
Clone the repository to your local machine.
Install the required dependencies as listed in requirements.txt.
Explore the datasets available in the /data directory.
Run the analysis scripts in /scripts to reproduce the findings.
Open the Tableau workbooks in /visualizations to view and interact with the visualizations.
### Contributing
We welcome contributions to this project! Please read through our contribution guidelines before making a pull request.

### License
This project is available under the MIT License.

### Contact
For any queries or discussions regarding the project, please open an issue in this repository.
