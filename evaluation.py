from nltk import meteor, word_tokenize
from nltk.translate.meteor_score import meteor_score
import pandas as pd
import numpy as np
import argparse

def calculate_metor(results, write):
    
    df_dataset = pd.read_csv("train.csv")
    df_summaries = pd.read_csv(results)
    # df_summaries_context
    df_dataset_summaries = pd.concat([df_dataset, df_summaries], axis=1)
    print(df_dataset_summaries.head())
    print(df_dataset_summaries.columns)
    # df_dataset_summaries_context
    score = 0
    lst_of_scores = []
    for _,row in df_dataset_summaries.iterrows():
        # print(row["normalized claim"],"\n",row["summary"])
        # print("\n\n",row["summary"] )
        if pd.isna(row["summary"]):
            print("not a filled row!")
        else:
            metor_score = meteor_score([word_tokenize(row["normalized claim"])], word_tokenize(row["summary"]))
            score += metor_score
            lst_of_scores.append(metor_score)
    df_of_scores = pd.DataFrame(data={"metor":lst_of_scores})
    df_of_scores.to_csv(write)
    avg = round(score/11374, 5)
    print(avg)    


def main():
    parser = argparse.ArgumentParser(prog="evaluation.py")
    parser.add_argument('-summaries')
    parser.add_argument('--write-to')
    args = parser.parse_args()
    print(args.summaries, args.write_to)
    calculate_metor(results=args.summaries, write=args.write_to)
if __name__ == "__main__":
    main()

