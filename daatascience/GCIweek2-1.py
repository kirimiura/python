#色々インポート
import numpy as np
from numpy import random
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib as plt



###numpy応用

#インデックス参照
sample=np.arange(10)
sample2=sample[0:5]
sample2[0:3]=10
print(sample)

#コピー機能
sample_copy=np.copy(sample)
sample_copy[3:6]=15
print(sample)
print(sample_copy)

#ブール参照
print(sample==10)
data=np.random.randn(10,10)
print(data[sample==10])

#where制御
bool_data=np.array([True,False,True])
a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.where(bool_data,a,b))

#要素の重複削除
print(np.unique(bool_data))

#ユニバーサル関数:全ての要素に適用できる関数
a=np.arange(10)
print("全ての要素の平方根",np.sqrt(a))
print("全ての要素の指数関数",np.exp(a))

#行列の最大などの表示
a=np.arange(9).reshape(3,3)
print("最大値",a.max())
print("最小値",a.min())
print("平均",a.mean())
print("合計",a.sum())

#行、列ごとの合計
print(a)
print("行の合計",a.sum(axis=1))
print("列の合計",a.sum(axis=0))

#真偽値の計算
bool_data=np.array([True,True,False])
print("一つでもTrueがあるか",bool_data.any())
print("一つもFalseがないか",bool_data.all())

#対角成分の計算
a=np.arange(9).reshape(3,3)
print(a)
print("対角成分",np.diag(a))
print("対角成分の和",np.trace(a))

#行列の結合
a=np.arange(6).reshape(2,3)
b=np.array([[6,7,8],[9,10,11]])
#行方向
print(np.concatenate([a,b],axis=0))
print(np.vstack((a,b)))
#列方向
print(np.concatenate([a,b],axis=1))
print(np.hstack((a,b)))

#行列の分解
c=np.vstack((a,b))
f,s,t=np.split(c,[1,3])
print("一番目",f)
print("二番目",s)
print("三番目",t)
#繰り返し処理
print(f.repeat(3))

#ブロードキャストは便利
a=np.arange(10)
print(a+3)




###scipyの応用
