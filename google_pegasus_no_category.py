from transformers import pipeline
from datasets import load_dataset
from itertools import islice
from dotenv import load_dotenv
import os
import pandas as pd
summarizer = pipeline("summarization", model="google/pegasus-cnn_dailymail", device=0, use_fast=False, tokenizer="google/pegasus-cnn_dailymail")
prompt = "Please give a summary of this article"
dataset = pd.read_csv("dev.csv")
""" batched_df takes in a pandas dataframe and yeilds a dataa frame based on batch size"""
def batched_df(df, batch_size):
    for start in range(0, len(df), batch_size):
        yield df.iloc[start:start + batch_size]
""" summarize_no_context is a method that is used to summarize the post given no categorical context"""
def summarize_no_context():
    load_dotenv('bart.env')
    sunmmary_lst = []
    write_file = os.getenv('WRITE_TO_FILE')
    for example in batched_df(dataset, 4):
        prompt = [f"Summarize this text: {row['post']}" for _, row in example.iterrows()]
        print(prompt)       
        summaries = summarizer(prompt, truncation=True)
        for summary in summaries:
            sunmmary_lst.append({"summary": summary["summary_text"] })
            with open(write_file, 'a') as file:
                file.write(summary["summary_text"] + "\n")          
    summary_df = pd.DataFrame(sunmmary_lst)
    summary_df.to_csv("output_of_summaries.csv", index=False)

def main():
    summarize_no_context()

if __name__ == "__main__":
    main()
