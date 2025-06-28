import pandas as pd
df_news = pd.read_csv("news_indicies.csv")
df_social = pd.read_csv("social_indicies.csv")
df_health = pd.read_csv("health_indicies.csv")
lst_of_indexs_news = df_news["news"].to_list()
lst_of_indexs_social = df_social["social"].to_list()
lst_of_indexs_health = df_health["health"].to_list()
results_lst = ["t5_meteor.csv", "t5_meteor_cat.csv", "google_meteor.csv", "google_meteor_cat.csv", "falconsai_meteor_cat.csv", "falconsai_meteor.csv"]
for meteor_results in results_lst:
    df_to_load = pd.read_csv(meteor_results)
    # print(lst_of_indexs_news)
    news_meteor = df_to_load.iloc[lst_of_indexs_news]
    social_meteor = df_to_load.iloc[lst_of_indexs_social]
    health_meteor = df_to_load.iloc[lst_of_indexs_health]
    news_metor_score = 0 
    for _,n_m in news_meteor.iterrows():
        news_metor_score+=n_m['metor']
    avg_meteor_score_for_news = news_metor_score/len(lst_of_indexs_news)
    social_meteor_score=0
    for _, social in social_meteor.iterrows():
        social_meteor_score+=social['metor']
    avg_meteor_score_for_social = social_meteor_score/len(lst_of_indexs_social)
    health_meteor_score = 0
    for _, health in health_meteor.iterrows():
        health_meteor_score+=health['metor']
    avg_meteor_score_for_health = health_meteor_score/len(lst_of_indexs_health)
    print(f"result {meteor_results}\nhealth: {avg_meteor_score_for_health},\nsocial: {avg_meteor_score_for_social},\nnews: {avg_meteor_score_for_news}\n\n")