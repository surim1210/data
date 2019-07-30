import pandas as pd

toeic_df = pd.read_csv('data/toeic.csv')

total = toeic_df['LC'] + toeic_df['RC'] > 600
both = (toeic_df['LC'] >= 250) & (toeic_df['RC'] >= 250)

toeic_df['합격여부'] = total & both

print(toeic_df)