from transformers import pipeline
from datasets import load_dataset
from itertools import islice
from dotenv import load_dotenv
import os
import pandas as pd
# summarizer = pipeline("summarization", model="facebook/bart-large-cnn"  )
summarizer = pipeline("summarization", model="google/pegasus-cnn_dailymail", device=0)
prompt = "Please give a summary of this article"
dataset = pd.read_csv("dev.csv")
# dataset = load_dataset("csv", data_files="dev.csv", streaming=True)
def batched_df(df, batch_size):
    for start in range(0, len(df), batch_size):
        yield df.iloc[start:start + batch_size]
def summarize_no_context():
    load_dotenv('bart.env')
    write_file = os.getenv('WRITE_TO_FILE')
    for example in batched_df(dataset, 4):
        prompt = [f"Summarize this text: {row['post']}" for _, row in example.iterrows()]
        print(prompt)       
        summaries = summarizer(prompt)
        for summary in summaries:
            with open(write_file, 'a') as file:
                file.write(summary["summary_text"] + "\n")          
# def summarize_context():
#     load_dotenv('bart.env')
#     write_file = os.getenv('WRITE_TO_FILE')
#     categories_file = os.getenv('CATEGORY_FILE')
#     df_cat = pd.read_csv(categories_file)

#     for example, category in batched(dataset, 8), batched(df_cat, 8):
#         prompt = [f"Summarize this : {item['document']}" for item in example]
#         summaries = summarizer(prompt)
#         for summary in summaries:
#             #####
#             with open(write_file, 'a') as file:
#                 file.write(summary)   
def main():
    summarize_no_context()
if __name__ == "__main__":
    main()
