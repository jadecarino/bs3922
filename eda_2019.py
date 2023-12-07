# Importing packages
import pandas as pd
from ydata_profiling import ProfileReport


# Exploratory Data Analysis 2019 Survey
df_2019 = pd.read_csv('survey_results_public_2019.csv')

# Get relevant columns
df_2019 = df_2019[["Respondent", "MainBranch", "EdLevel", "YearsCode", "YearsCodePro",
                   "OrgSize", "DevType", "ConvertedComp", "WorkRemote", "LanguageWorkedWith"]]

print(df_2019.head())

# Find and print all unique values in the EdLevel column
ed_level_values = df_2019["EdLevel"].unique()
print(ed_level_values)

# Assign an order to the EdLevel column
order_ed_level = ["I never completed any formal education",
                  "Primary/elementary school",
                  "Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)",
                  "Some college/university study without earning a degree",
                  "Bachelor’s degree (BA, BS, B.Eng., etc.)",
                  "Master’s degree (MA, MS, M.Eng., MBA, etc.)",
                  "Professional degree (JD, MD, etc.)",
                  "Other doctoral degree (Ph.D, Ed.D., etc.)' nan 'Associate degree"]

df_2019["EdLevel"] = pd.Categorical(df_2019["EdLevel"], categories=order_ed_level, ordered=True)

df_2019_sorted_ed_level = df_2019.sort_values(by = "EdLevel")

print(df_2019_sorted_ed_level.head())

profile = ProfileReport(df_2019, title="2019 Stack Overflow Developer Survey Profiling Report")
profile.to_file('report_2019_1.html')