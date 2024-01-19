import pandas as pd
import re

# Load the Excel file
df = pd.read_excel('prepped_translated.xlsx')

# Assume that "source_text" column contains the original text
# and "trans_text" column contains the translated text
for i, row in df.iterrows():
    source_text = row['en-US']
    trans_text = row['zh-CN']
    
    # Extract numbers from the original text
    original_numbers = re.findall(r"(\d+\.\d+)", source_text)
    
    # Replace placeholders with original numbers
    for j in range(len(original_numbers)):
        trans_text = trans_text.replace(f'[{j}]', str(original_numbers[j]))
    
    # Update the cell with the replaced text
    df.at[i, 'zh-CN'] = trans_text

# Save the dataframe back to Excel
df.to_excel('prepped_replaced.xlsx', index=False)