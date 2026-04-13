#import pandas

import pandas as pd
import openpyxl
import os

def save_to_excel(data):

    PATH = "weather_data.xlsx"

    try:
        new_df = pd.DataFrame(data)
        if os.path.exists(PATH):
            current = pd.read_excel(PATH)
            concat_data = pd.concat([current, new_df], ignore_index=True)
            concat_data.to_excel(PATH, index=False)
        else:
            new_df.to_excel(PATH, index=False)

    except Exception as e:
        print(e)









# def save_to_excel(data):
#     try:
#         df = pd.DataFrame(data)
#         df.to_excel("weather_data.xlsx")
#     except Exception as e:
#         print(e)