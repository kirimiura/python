#色々インポート
import numpy as np
import scipy as sp
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
sns.set()
np.random.seed(0)
#線形解析ライブラリ
from sklearn import linear_model
# webからデータを取得したり、zipファイルを扱うためのライブラリ
import requests, zipfile
from io import StringIO
import io

#urlからデータを絞り込む一連の流れ
# データがあるurlの指定
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00356/student.zip'
# データをurlから取得する
r = requests.get(url, stream=True)
# zipfileを読み込み展開する
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

#データの読み込み
student_data_math = pd.read_csv('student-mat.csv', sep=';')

# すべてのカラムの情報等チェック
print(student_data_math.info())
#最初だけ見る
print(student_data_math['absences'].head())
#軸別の平均値
print(student_data_math.groupby('sex')['age'].mean())

#中央値外れ値からの影響を受けにくい
print('中央値：', student_data_math['absences'].median())
#最頻値：最も頻度が多い値
print('最頻値：', student_data_math['absences'].mode())
# 分散
print(student_data_math['absences'].var())
# 標準偏差 σ
print(student_data_math['absences'].std())
# 要約統計量(おおよその統計値)
print(student_data_math['absences'].describe())
# 四分位範囲(75%タイル ー 25%タイル)
print(student_data_math['absences'].describe()[6] - student_data_math['absences'].describe()[4])
# 要約統計量まとめて計算
print(student_data_math.describe())
# 箱ひげ図：G1
plt.boxplot(student_data_math['G1'])
plt.grid(True)
plt.show()
# 変動係数：標準偏差/平均
print(student_data_math['absences'].std() / student_data_math['absences'].mean())
#共分散
print(np.cov(student_data_math['G1'], student_data_math['G3']))
#相関係数
print(sp.stats.pearsonr(student_data_math['G1'], student_data_math['G3']))
#相関行列
print(np.corrcoef([student_data_math['G1'], student_data_math['G3']]))

#単回帰分析
from sklearn import linear_model

# 線形回帰のインスタンスを生成
reg = linear_model.LinearRegression()
# 説明変数に "一期目の数学の成績" を利用
# locはデータフレームから、行と列を指定して取り出す。loc[:, ['G1']]は、G1列のすべての列を取り出すことをしている
# valuesに直しているので、注意
X = student_data_math.loc[:, ['G1']].values
# 目的変数に "最終の数学の成績" を利用
Y = student_data_math['G3'].values
# 予測モデルを計算、ここでa,bを算出
reg.fit(X, Y)
# 回帰係数
print('回帰係数:', reg.coef_)
# 切片 
print('切片:', reg.intercept_)
#散布図にかき出し
plt.scatter(X, Y)
plt.xlabel('G1 grade')
plt.ylabel('G3 grade')
# その上に線形回帰直線を引く
plt.plot(X, reg.predict(X))
plt.grid(True)
plt.show()
# 決定係数、寄与率とも呼ばれる(どれくらい回帰が正しかったか)
print('決定係数:', reg.score(X, Y))
