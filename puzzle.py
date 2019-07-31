import pandas as pd

puzzle_df = pd.read_csv('data/puzzle.csv', index_col=0)

puzzle_df['A'] = puzzle_df['A'] * 2
puzzle_df.iloc[2, 'F'] = 99
puzzle_df[puzzle_df.loc[:, 'B':'E'] < 80] = 0
puzzle_df[puzzle_df.loc[:, 'B':'E'] >= 80] = 1


print(puzzle_df)


