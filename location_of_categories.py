import pandas as pd
df = pd.read_csv("train_cat.csv")
pd.read_csv("train_cat.csv")
indicies_news = df[df['categories for df']== 'news article'].index
indicies_social = df[df['categories for df']== 'social media post'].index
indicies_health = df[df['categories for df']== 'healthcare article'].index
df_of_social= pd.DataFrame({"social":indicies_social})
df_of_health= pd.DataFrame({"health":indicies_health})
df_of_news = pd.DataFrame({"news":indicies_news})
df_of_news.to_csv("news_indicies.csv")
df_of_social.to_csv("social_indicies.csv")
df_of_health.to_csv("health_indicies.csv")