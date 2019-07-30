import pandas as pd

fix_dt = pd.read_csv('data/body_imperial2.csv', index_col=0)

fix_dt['비만도'] = '정상'
fix_dt.loc[:10, 'Gender'] = 'Male'
fix_dt.loc[11:, 'Gender'] = 'Female'

print(fix_dt)

