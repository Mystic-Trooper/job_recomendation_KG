import pandas as pd
import numpy as np
dataset = pd.read_csv("Resume_Dataset/survey_results_public.csv")
resume_subset= dataset[['Respondent','Country','Student','CompanySize','Dependents','DevType','Gender','JobSatisfaction','LastNewJob','Salary','LanguageWorkedWith','LanguageDesireNextYear','DatabaseWorkedWith','DatabaseDesireNextYear','PlatformWorkedWith','PlatformDesireNextYear','FrameworkWorkedWith','FrameworkDesireNextYear','OperatingSystem','HypotheticalTools1','Age']]
df = pd.DataFrame(resume_subset)
df1 = df.dropna()
df1['skills'] = df1[df1.columns[10:17]].values.tolist()
print(df1['skills'])
df1['skills'] = df['skills'].apply(lambda x: list(set(x)))