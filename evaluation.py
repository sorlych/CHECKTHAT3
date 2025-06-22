from nltk import meteor, word_tokenize
from nltk.translate.meteor_score import meteor_score
import pandas as pd
import numpy as np
def calculate_metor():
    df_dataset = pd.read_csv("train.csv")
    df_summaries = pd.read_csv("t5_summaires.csv")
    # df_summaries_context
    df_dataset_summaries = pd.concat([df_dataset, df_summaries], axis=1)
    print(df_dataset_summaries.head())
    print(df_dataset_summaries.columns)
    # df_dataset_summaries_context
    score = 0
    for _,row in df_dataset_summaries.iterrows():
        print(row["normalized claim"],"\n",row["summary"])
        print("\n\n",row["summary"] )
        if pd.isna(row["summary"]):
            print("not a filled row!")
        else:
            score += meteor_score([word_tokenize(row["normalized claim"])], word_tokenize(row["summary"]))
    avg = round(score/1285, 5)
    print(avg)    


def main():
    calculate_metor()
if __name__ == "__main__":
    main()

