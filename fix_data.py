import pandas as pd

fix_df = pd.read_csv('data/body_imperial1.csv', index_col=0)

fix_df.iloc[[1,3]] = 200
fix_df.drop(21, axis='index',inplace=True)  # row delete
fix_df.loc[20] = [70, 200]   # add information

print(fix_df)