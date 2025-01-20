# -*- coding: utf-8 -*-
"""lostark_api.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AePqiiSNyd4DKONmEdze48dOhBsKl7PV
"""

import requests
import pandas as pd
from google.colab import userdata

# 사용자 데이터에서 API 키 가져오기

def lost():
  API_KEY = userdata.get("lostark_api")
  ITEM_ID = '65203905'
  url = f'https://developer-lostark.game.onstove.com/markets/items/{ITEM_ID}'

  headers = {
      'Authorization': f'bearer {API_KEY}',
      'accept': 'application/json'
  }
  response = requests.get(url, headers=headers)
  data = response.json()

  all_stats = []
  for item in data:
      for stat in item["Stats"]:
          stat["Name"] = item["Name"]
          all_stats.append(stat)

  df = pd.DataFrame(all_stats)
  df = df[df['AvgPrice'] != 0]
  df = df.reset_index()
  df = df.drop(columns=['index'])
  return df