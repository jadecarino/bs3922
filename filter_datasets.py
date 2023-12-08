import pandas as pd

year = 2023

# Import the dataset
df = pd.read_csv("datasets/survey_results_public_" + str(year) + ".csv")

# Keep only relevant columns in the data frame
if year == 2019:
    df = df[["Respondent", "MainBranch", "EdLevel", "YearsCode", "YearsCodePro",
                   "OrgSize", "DevType", "ConvertedComp", "WorkRemote", "LanguageWorkedWith"]]

if year == 2020:
    df = df[["Respondent", "MainBranch", "ConvertedComp", "DevType", "EdLevel",
                   "LanguageWorkedWith", "OrgSize", "YearsCode", "YearsCodePro"]]

if year == 2021:
    df = df[["ResponseId", "MainBranch", "EdLevel", "LearnCode", "YearsCode", "YearsCodePro",
                       "DevType", "OrgSize", "LanguageHaveWorkedWith", "ConvertedCompYearly"]]

if year == 2022:
    df = df[["ResponseId", "MainBranch", "RemoteWork", "EdLevel", "LearnCode", "YearsCode",
                   "YearsCodePro", "DevType", "OrgSize", "LanguageHaveWorkedWith", "ConvertedCompYearly"]]

if year == 2023:
    df = df[["ResponseId", "MainBranch", "RemoteWork", "EdLevel", "LearnCode", "YearsCode",
                   "YearsCodePro", "DevType", "OrgSize", "LanguageHaveWorkedWith", "ConvertedCompYearly"]]

# Remove responses where the respondent is not a developer by profession as irrelevant to research aim
wanted_mainbranch_value = "I am a developer by profession"
df = df[df["MainBranch"] == wanted_mainbranch_value]

df.to_csv("datasets/filtered/filtered_dataset_" + str(year) + ".csv")
print("Filtered dataset exported to datasets/filtered_dataset_" + str(year) + ".csv")