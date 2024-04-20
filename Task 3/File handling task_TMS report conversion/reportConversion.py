import pandas as pd

# read the xlsx file
df = pd.read_excel('2023-11-07_sampleProject_Metrics.xlsx')
# read the csv file
df2 = pd.read_csv('mySampleReport.csv')
# Update the target locale column
df2['Target Locale'] = df['Target language']
df2['Asset'] = df['File']
# Update the total word count of the csv file
df2['Total'] = df['Words total count']
# Update the ICE Match column
df2['ICE Match'] = df['ICE Match']
# Update the 100-90% match column
df2['100-90%'] = df['Words 95-99 fuzzy match']
# Update the 90-80% match column
df2['90-80%'] = df['Words 85-94 fuzzy match']
# Update the 80-70% match column
df2['80-70%'] = df['Words 75-84 fuzzy match']
# Update the 60-0% match column
df2['60-0%'] = df['Words no matching']
# Update the repetition column
df2['Repetition'] = df['Words repeat']
# Save a copy of the updated csv file
df2.to_csv('mySampleReport_updated.csv', index=False)
