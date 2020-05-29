##chapter2


##numpy:基本的な数列処理、数値計算
##scipy:numpyを強化、統計や信号計算
##pandas:データ加工
##matplotlib:データのグラフ化

##fromを使ったimport
from numpy import random

##色々インポートしておく
import numpy as np
import numpy.random as random
import scipy as sp
import pandas as pd
from pandas import Series, DataFrame

##可視化ライブラリ
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

##numpyの基礎(week1-1の内容除く)
##ソートする
deta=np.array([1,5,2,4,3])
print("ソート前",deta)
deta.sort()
print("ソート後",deta)

##最大最小合計積み上げ積み上げ割合
print("最小:",deta.min())
print("最大:",deta.max())
print("合計:",deta.sum())
print("積み上げ:",deta.cumsum())
print("積み上げ割合:",deta.cumsum()/deta.sum())

##乱数
##シードの設定
random.seed(0)

##乱数の発生（例、正規分布）
rnd_deta=random.randn(10)
print("乱数10個の配列",rnd_deta)

##データのランダムな抽出
x=np.array([1,2,3,4,5,6,7,8,9,10])
##復元抽出
print(random.choice(x,8))
##非復元抽出
print(random.choice(x,8,replace = False))

##行列を作る
array1=np.arange(1,10).reshape(3,3)
print(array1)
array2=np.arange(9,18).reshape(3,3)
print(array2)

##行列の掛け算
##”掛け算”と、”成分ごとの掛け算”の違い
print(np.dot(array1,array2))
print(array1*array2)

##要素が〇〇だけの行列を作る
print(np.zeros((2,3),dtype=np.int64))
print(np.ones((2,3),dtype=np.float64))


##scipyの基礎

##線形代数用のライブラリ、最適化計算ライブラリのインポート
import scipy.linalg as linalg
from scipy.optimize import minimize_scalar

##行列式と逆行列の計算
matrix=np.array([[1,-1,-1],[-1,1,-1],[-1,-1,1]])
#行列式
print("行列式")
print(linalg.det(matrix))

#逆行列
print("逆行列")
print(linalg.inv(matrix))

##確認してみよう
print(np.dot(matrix,linalg.inv(matrix)))
print(matrix.dot(linalg.inv(matrix)))

##固有値と固有ベクトル
value,vector = linalg.eig(matrix)
print("固有値")
print(value)
print("固有ベクトル")
print(vector)


##ニュートン法
def f(x):
    return x**2+2*x+1
##またはg=lambda x: x**2+2*x+1などと書く
from scipy.optimize import newton
print(newton(f,0))


##最小値を求める
print(minimize_scalar(f,method = "Brent"))




##pandasの基礎
##pandasは、データの加工処理に便利

#Seriesは1次元
samples_pandas_deta = pd.Series([0,10,20,30,40,50,60,70,80,90])
print(samples_pandas_deta)
print("インデックスの値",samples_pandas_deta.index)
print("データの値",samples_pandas_deta.values)

#インデックスを加える
samples_pandas_index_deta=pd.Series([0,1,2,3,4,5,6,7,8,9],index=["a","b","c","d","e","f","g","h","i","j"])
print(samples_pandas_index_deta)

#DataFrameは二次元
attri_deta={"Id":["100","101","102","103","104"],
"City":["Tokyo","Osaka","Kyoto","HOkkaido","Tokyo"],
"Name":["A","B","F","G","R"]}
frame1=DataFrame(attri_deta)
print(frame1)

#Seriesと同様、インデックスも使える
frame2 = DataFrame(attri_deta,index=["a","b","c","d","e"])
print(frame2)

#転置行列化
frame3=frame2.T
print(frame3)

#特定列のみ抽出
#1つ
print(frame1.City)
#転置行列にした後もいける
print(frame3.b)
#複数
print(frame1[["Id","Name"]])

##データの抽出
##基本的には、条件代入でよい
print(frame1[frame1["City"]=="Tokyo"])
print(frame1[frame1["Id"]>"101"])
#複数を選ぶ感じのもいける
print(frame1[frame1["City"].isin(["Tokyo","Osaka"])])
#さらに抽出もできる
print(frame1[frame1["City"].isin(["Tokyo","Osaka"])].Id)


#データの削除
print(frame1.drop(["City"],axis=1))

#データの結合
attri_detax={"Id":["103","104","107","108"],
"Math":["30","70","80","45"],
"English":["35","55","65","80"],
"Sex":["M","F","M","M"]}
frame1x=DataFrame(attri_detax)
print(pd.merge(frame1,frame1x))
frame1y=DataFrame(attri_detax,index=["p","q","r","s"])
print(frame1y)
#データの集計例（平均を求めてみる）
#よくわからないエラー出た
#print(frame1y.groupby("Sex")["Math"].mean())


#データのソート
#ぐちゃぐちゃのデータ
attri_data2 = {'ID':['100','101','102','103','104'],
'City':['Tokyo','Osaka','Kyoto','Hokkaido','Tokyo'],
'Birth_year':[1990,1989,1992,1997,1982],
'Name':['Hiroshi','Akiko','Yuki','Satoru','Steve']}
frame10 = DataFrame(attri_data2)
frame11 = DataFrame(attri_data2,index=['e','b','a','d','c'])
print(frame11)

#色々ソートしてみる
print(frame11.sort_index())
print(frame11.Birth_year.sort_values())
print(frame11.ID.sort_values())

#欠損データに対する対応
#True,Falseを見るやつ
print(frame11.isin(["Tokyo"]))

#nanとnullに応用
frame11["Name"]=np.nan
print(frame11)
print(frame11.isnull())

#合計値求める
print(frame11.isnull().sum())








###matplotlibの基礎

#散布図
import numpy.random as random
random.seed(1)
#軸データ
x=random.randn(30)
y=np.sin(x)+random.randn(30)
#大きさ指定
plt.figure(figsize=(10,3))
#グラフを書く
plt.plot(x,y,"o")
#タイトル
plt.title("Title name")
#x座標名前
plt.xlabel("X")
#y座標名前
plt.ylabel("Y")
#grid
plt.grid(True)

##グラフの分割
plt.figure(figsize=(10,3))
#2行1列グラフの一つ目
plt.subplot(2,1,1)
x=np.linspace(-10,10,100)
plt.plot(x,np.sin(x))
plt.grid(True)
#2つ目
plt.subplot(2,1,2)
y=np.linspace(-10,10,100)
plt.plot(y,np.sin(2*y))
plt.grid(True)
#plt.show()

#関数の描写
def h(x):
    return x**2+2*x+1

plt.figure(figsize=(10,3))
x=np.arange(-10,10)
plt.plot(x,h(x))
plt.grid(True)

#ヒストグラムの作成
random.seed(3)
plt.figure(figsize=(10,3))
plt.hist(random.randn(10**5))
plt.show()

