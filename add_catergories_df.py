import os
import pandas as pd
import numpy as np
from dotenv import load_dotenv

def concat():
    load_dotenv('add_categories_df.env')
    data_set = os.getenv('DATASET')
    categories = os.getenv('CATEGORY_CSV')
    out_put = os.getenv("OUTPUT")
    data = pd.read_csv(data_set)
    category = pd.read_csv(categories)
    data_with_categories:pd.DataFrame = pd.concat([data,category],axis=1)
    data_with_categories.to_csv(out_put)
    print(data_with_categories)
def main():
    concat()
if __name__ == '__main__':
    main()