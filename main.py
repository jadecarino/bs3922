# Importing packages
import pandas as pd
from ydata_profiling import ProfileReport

# # Exploratory Data Analysis 2019 Survey
# df_2019 = pd.read_csv('survey_results_public_2019.csv')
#
# df_2019 = df_2019[["Respondent", "MainBranch", "ConvertedComp", "DevType", "EdLevel",
#                    "LanguageWorkedWith", "OrgSize", "YearsCode", "YearsCodePro", ]]
#
# profile = ProfileReport(df_2019, title="2019 Stack Overflow Developer Survey Profiling Report")
# profile.to_file('report_2019.html')
#
# # Exploratory Data Analysis 2020 Survey
# df_2020 = pd.read_csv('survey_results_public_2020.csv')
#
# df_2020 = df_2020[["Respondent", "MainBranch", "ConvertedComp", "DevType", "EdLevel",
#                    "LanguageWorkedWith", "OrgSize", "YearsCode", "YearsCodePro", ]]
#
# profile = ProfileReport(df_2020, title="2020 Stack Overflow Developer Survey Profiling Report")
# profile.to_file('report_2020.html')
#
# # Exploratory Data Analysis 2021 Survey
# df_2021 = pd.read_csv('survey_results_public_2021.csv')
#
# df_2021 = df_2021[["ResponseId", "MainBranch", "EdLevel", "LearnCode", "YearsCode", "YearsCodePro",
#                    "DevType", "OrgSize", "LanguageHaveWorkedWith", "ConvertedCompYearly"]]
#
# profile = ProfileReport(df_2021, title="2021 Stack Overflow Developer Survey Profiling Report")
# profile.to_file('report_2021.html')
#
# # Exploratory Data Analysis 2022 Survey
# df_2022 = pd.read_csv('survey_results_public_2022.csv')
#
# df_2022 = df_2022[["ResponseId", "MainBranch", "RemoteWork", "EdLevel", "LearnCode", "YearsCode",
#                    "YearsCodePro", "DevType", "OrgSize", "LanguageHaveWorkedWith", "ConvertedCompYearly"]]
#
# profile = ProfileReport(df_2022, title="2022 Stack Overflow Developer Survey Profiling Report")
# profile.to_file('report_2022.html')
#
# # Exploratory Data Analysis 2023 Survey
# df_2023 = pd.read_csv('survey_results_public_2023.csv')
#
# df_2023 = df_2023[["ResponseId", "MainBranch", "RemoteWork", "EdLevel", "LearnCode", "YearsCode",
#                    "YearsCodePro", "DevType", "OrgSize", "LanguageHaveWorkedWith", "ConvertedCompYearly"]]
#
# profile = ProfileReport(df_2023, title="2023 Stack Overflow Developer Survey Profiling Report")
# profile.to_file('report_2023.html')

# Transformed
# df_2023_transformed = pd.read_csv('survey_results_public_trimmed_2_developers_only.csv')
#
# profile = ProfileReport(df_2023_transformed, title="Demo report")
# profile.to_file('test.html')