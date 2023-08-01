import pandas as pd

train_df = pd.read_csv('./Dacon project/train.csv') # 나중에 상대 경로로 변경 필요

print(train_df)

train_df['기온(C)'].dropna()

print(train_df)