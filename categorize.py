# This script is used to take each data set and categorize it
# To use this script set the env file variable to what data set you would like to categorize
#
#
from together import Together
import pandas as pd
import os
import re
from dotenv import load_dotenv
def env_vars():
    load_dotenv("categorize.env")
def shorten_post(post, max_chars=4000):
    if isinstance(post, str) and len(post) > max_chars:
        return post[:max_chars] + "..."
    return post
def together_setup():
    env_vars()
    api_key = os.getenv("API_KEY")
    client = Together(api_key=api_key)
    data_set_file = os.getenv("DATASET")
    df_post_claims = pd.read_csv(data_set_file)
    categories = ["healthcare article", "social media post", "news article"]
    with open("test_cat.csv", "w") as file:
        file.write("categories for df\n")
    for post in df_post_claims.values:
        category_found = False
        shortened_post = shorten_post(post)
        response = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
            messages=[{"role": "user", 
                    "content": f"Classify the following post into ONE of these categories: healthcare article, social media post, news article.\n\nRespond with ONLY the category name.\n\nPost: {shortened_post}"}]
        )
        raw_output = response.choices[0].message.content
        # print(raw_output)
        # print(raw_output.strip().lower())
        last_line = raw_output.splitlines()[-1].strip()
        for category in categories:
            if category in last_line:
                category_found=True
                with open("test_cat.csv", "a") as file:
                    file.write(f"{category}\n")
        if category_found == False:
            with open("test_cat.csv", "a") as file:
                file.write("NONE")

def main():
    env_vars()
    together_setup()
if __name__ == "__main__":
    main()