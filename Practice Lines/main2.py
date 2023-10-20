import pandas as pd

df = pd.read_csv('devSurvey.csv')
years_code_list = df['YearsCode'].dropna()
print(years_code_list)