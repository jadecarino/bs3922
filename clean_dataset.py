import pandas as pd

year = 2023
convertedcomp_variable_name = "ConvertedCompYearly"

df = pd.read_csv("datasets/filtered/filtered_dataset_" + str(year) + ".csv")
df.describe()

# Drop all null values from the ConvertedComp/ConvertedCompYearly column
df.dropna(subset = [convertedcomp_variable_name], inplace = True)
df.reset_index(inplace = True)
print(str(year) + " Stack Overflow Developer Survey with null values removed from ConvertedComp/ConvertedCompYearly")
df.describe()

from scipy.stats import zscore

# Get the Z Score
z_scores = zscore(df[convertedcomp_variable_name])
print("The Z Scores:")
print(str(z_scores))

# Set the threshold for the Z Score to be 0.5
threshold = 0.5

# Remove all rows in the data frame if the Z Score is not in threshold
df_no_outliers = df[(abs(z_scores) < threshold)]

print(str(year) + " Stack Overflow Developer Survey with no outlier values for " + convertedcomp_variable_name)
df_no_outliers.describe()


# Save dataframe to CSV file now it has been cleaned
df_no_outliers.to_csv("datasets/cleaned/cleaned_dataset_" + str(year) + ".csv")
print("Cleaned dataset exported to datasets/cleaned/cleaned_dataset_" + str(year) + ".csv")