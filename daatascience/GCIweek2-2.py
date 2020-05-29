#色々インポート
import numpy as np
import numpy.random as random
import scipy as sp
import pandas as pd
from pandas import Series,DataFrame

import os
import zipfile
import requests
import io

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

#階層型インデックス（インデックスが複数)
frame1=DataFrame(
    np.arange(9).reshape((3,3)),
    index=[
        ["a","a","b"],
        [1,2,2]
    ],
    columns=[
        ["Osaka","Tokyo","Osaka"],
        ["Blue","Red","Red"]
    ]
)

#インデックスに名前を付ける
frame1.index.names=["key1","key2"]
frame1.columns.names=["city","color"]
print(frame1)

#カラムの絞り込み
print(frame1["Osaka"])

#インデックスを軸にした集計
print(frame1.sum(level="key1",axis=0))
print(frame1.sum(level="color",axis=1))

#要素の削除
print(frame1.drop(["a"]))

#データの結合
data1 = {
    'id': ['100', '101', '102', '103', '104', '106', '108', '110', '111', ' 113'],
    'city': ['Tokyo', 'Osaka', 'Kyoto', 'Hokkaido', 'Tokyo', 'Tokyo', 'Osaka', 'Kyoto', 'Hokkaido', 'Tokyo'],
    'birth_year': [1990, 1989, 1992, 1997, 1982, 1991, 1988, 1990, 1995, 1981],
    'name': ['Hiroshi', 'Akiko', 'Yuki', 'Satoru', 'Steeve', 'Mituru', 'Aoi', 'Tarou', 'Suguru', 'Mitsuo']
}
df1 = DataFrame(data1)
print(df1)
data2 = {
    'id': ['100', '101', '102', '105', '107'],
    'math': [50, 43, 33, 76, 98],
    'english': [90, 30, 20, 50, 30],
    'sex': ['M', 'F', 'F', 'M', 'M'], 
    'index_num': [0, 1, 2, 3, 4]
}
df2 = DataFrame(data2)
print(df2)

#内部結合
print(pd.merge(df1,df2,on="id"))
#全結合
print(pd.merge(df1,df2,how="outer"))
print(pd.merge(df1,df2,left_index=True,right_on="index_num"))
#左外部結合
print(pd.merge(df1,df2,how="left"))

#データの縦方向結合
data3 = {
    'id': ['117', '118', '119', '120', '125'],
    'city': ['Chiba', 'Kanagawa', 'Tokyo', 'Fukuoka', 'Okinawa'],
    'birth_year': [1990, 1989, 1992, 1997, 1982],
    'name': ['Suguru', 'Kouichi', 'Satochi', 'Yukie', 'Akari']
}
df3 = DataFrame(data3)
print(pd.concat([df1,df3]))

#ピポット操作
print(frame1)
print(frame1.stack())
print(frame1.stack().unstack())

#重複チェック、削除
dupli_data = DataFrame({
        'col1': [1, 1, 2, 3, 4, 4, 6, 6],
        'col2': ['a', 'b', 'b', 'b', 'c', 'c', 'b', 'b']
})
print(dupli_data.duplicated())
print(dupli_data.drop_duplicates())

#マッピング処理
city_map = {
    'Tokyo': 'Kanto',
    'Hokkaido': 'Hokkaido',
    'Osaka': 'Kansai',
    'Kyoto':'Kansai'
}

df1["region"]=df1["city"].map(city_map)
print(df1)

#lambda関数で応用
#birth_yearからageを取得
df1["age"]=df1["birth_year"].map(lambda x:2020-x)
print(df1)

#ビン分割
birth_year_bins=[1980,1985,1990,1995,2000]
df11=pd.cut(df1.birth_year,birth_year_bins)
print(df11)
#集計
print(pd.value_counts(df11))
#分割数指定可能
print(pd.cut(df1.birth_year,2))
#分位点分割
print(pd.value_counts(pd.qcut(df1.birth_year,5)))

#データの集約とグループ演算
print(df1)
#サイズ情報
print(df1.groupby("city").size())
#平均値
print(df1.groupby("city")["birth_year"].mean())
print(df1.groupby(["region","city"])["birth_year"].mean())
print(df1.groupby(["region","city"],as_index=False)["birth_year"].mean())

