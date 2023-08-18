import pandas as pd

if __name__ == "__main__":
    train_df = pd.read_csv('./Dacon project/train.csv') 
    test_df = pd.read_csv('./Dacon project/test.csv')
    build_df = pd.read_csv('./Dacon project/building_info.csv')
    sample_df = pd.read_csv('./Dacon project/sample_submission.csv')