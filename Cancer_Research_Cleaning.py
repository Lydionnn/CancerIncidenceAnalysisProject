import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Load the dataset
data = pd.read_csv(r'C:\Users\Fernando\pyproj\my_env\cancer_reg.csv')

# Display basic information and the first few rows of the dataset
# data_info = data.info()
# data_head = data.head()

#data_info, data_head

# Check for duplicated rows
duplicates = data.duplicated().sum()

# Remove duplicates if any
if duplicates > 0:
    data_cleaned = data.drop_duplicates()
else:
    data_cleaned = data.copy()



# Calculate the percentage of missing values in each column
missing_data = data_cleaned.isnull().mean() * 100

# Filter columns with missing values to see their percentages
missing_columns = missing_data[missing_data > 0].sort_values(ascending=False)

#--------Given the missing values in 'pctsomecol18_24' being almost 75%, I will remove it

# Remove the column with over 70% missing data
data_cleaned.drop('pctsomecol18_24', axis=1, inplace=True)


# Check the distribution of the remaining columns with missing values
distribution_private_coverage_alone = data_cleaned['pctprivatecoveragealone'].describe()
distribution_employed_over = data_cleaned['pctemployed16_over'].describe()


#-----Also checking for the type of distribution on the other 2 columns showing missing values
#      to assess what would be the best way to impute missing values with either the mean or median I will check for the type of distribution on those



# Attempt to plot histograms for both columns to visually assess the distribution
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

# Plot for pctprivatecoveragealone
data_cleaned['pctprivatecoveragealone'].dropna().hist(ax=axes[0], bins=30, color='blue', alpha=0.7)
axes[0].set_title('Distribution of pctprivatecoveragealone')

# Plot for pctemployed16_over
data_cleaned['pctemployed16_over'].dropna().hist(ax=axes[1], bins=30, color='green', alpha=0.7)
axes[1].set_title('Distribution of pctemployed16_over')
#plt.show()


# Impute missing values in 'pctprivatecoveragealone' with the mean
mean_private_coverage_alone = data_cleaned['pctprivatecoveragealone'].mean()
data_cleaned.loc[:, 'pctprivatecoveragealone'] = data_cleaned['pctprivatecoveragealone'].fillna(mean_private_coverage_alone)



# Verify the imputation by checking for any remaining missing values in the column
remaining_missing_private_coverage = data_cleaned['pctprivatecoveragealone'].isnull().sum()

#print(remaining_missing_private_coverage)
#This code ^ outputs 0 confirming that we were able to impute the missing data correctly



# Plot histogram for 'pctemployed16_over'
data_cleaned['pctemployed16_over'].hist(bins=30)
plt.title('Distribution of pctemployed16_over')
plt.xlabel('Percentage Employed 16 Over')
plt.ylabel('Frequency')
#plt.show()


# Imputing mean for the missing data as well on this column-  due to the normal distribution on this column as well
# Impute missing values with mean or median based on the distribution

mean_employed16_over = data_cleaned['pctemployed16_over'].mean()  # or .median()
# Impute missing values and assign back to the column
data_cleaned['pctemployed16_over'] = data_cleaned['pctemployed16_over'].fillna(mean_employed16_over)

#checking for remaining missing values
#Prints 0 therefore I am good to go
remaining_missing = data_cleaned['pctemployed16_over'].isnull().sum()
#print("Remaining missing values in 'pctemployed16_over':", remaining_missing)
pd.set_option('display.max_columns', None)
#print(data_cleaned.describe()



#upon further review here overall in the columns I found a discrepancy in the 'medianage' column
#print(data_cleaned['medianage'].describe())
#----Diving deeper in this to understand further


# # Box Plot
# ---- Clearly some values are way above 110 so I will get rid of those and replace with the mean
# plt.figure(figsize=(10, 5))
# sns.boxplot(x=data_cleaned['medianage'])
# plt.title('Box Plot of Median Age')
# plt.xlabel('Median Age')
# plt.show()



# 1. Filter out and identify values over 110
valid_age_data = data_cleaned[data_cleaned['medianage'] <= 110]

# 2. Calculate the mean of the valid data
mean_valid_age = valid_age_data['medianage'].mean()

# 3. Replace values over 110 with the mean of valid ages
data_cleaned.loc[data_cleaned['medianage'] > 110, 'medianage'] = mean_valid_age

# Optional: Verify the operation
print(data_cleaned['medianage'].describe())

#----Visually confirming again
# plt.figure(figsize=(10, 5))
# sns.boxplot(x=data_cleaned['medianage'])
# plt.title('Box Plot of Median Age')
# plt.xlabel('Median Age')
# plt.show()

#One last thing that can help with the analysis will be extracting the state from the geography column and creating a new column by state.


# Split the 'geography' column at the comma and expand to two separate columns
data_cleaned[['county', 'state']] = data_cleaned['geography'].str.split(',', expand=True)

# Optionally, you can trim any leading or trailing whitespace from the 'state' column
data_cleaned['state'] = data_cleaned['state'].str.strip()

# Verify the changes by displaying the first few rows of the dataframe
print(data_cleaned[['geography', 'county', 'state']].head())

# Display the frequency of each county and state
county_counts = data_cleaned['county'].value_counts().sort_index()
state_counts = data_cleaned['state'].value_counts().sort_index()

# Print the counts for all counties and specifically for Washington if present
print("County Frequencies (Ordered Alphabetically):\n", county_counts)
print("\nState Frequencies (Ordered Alphabetically):\n", state_counts)




#Converting into csv clean file to work on analysis
#Save the DataFrame to a CSV file
data_cleaned.to_csv(r'C:\Users\Fernando\pyproj\my_env\Cleaned_files\cancer_cleaned_data.csv', index=False)

























