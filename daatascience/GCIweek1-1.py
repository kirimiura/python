##chapter1

##numpyの利用を宣言
import numpy as np

##numpyの配列を用意
x = np.array([1,3,5,2,4])
y = np.array([[1,3,4],[1,5,6]])
z=np.array([1,2,3,4,5])

##x,yの型、次元数、要素数を表示
print(x,y)
print(x.dtype,y.dtype)
print(x.ndim,y.ndim)
print(x.size,y.size)

##numpy配列同士の四則演算は、要素ごとに行われる。
print(x+z,x-z,x*z,x/z)

##要素を小さい順にソート
a=x.sort()
print(a)

##if関数の利用(ついでにinput関数も)
deta_list=[1,2,3,4,5]
key=int(input("key:"))

##変数を文字列に組み込ませる
if key in deta_list:
    print("{0}はデータリストにあります。".format(key))
else:
    print("{0}はデータリストにありません".format(key))

##for文を使う（例：要素全ての和を求める）
##初期値の設定
total = 0
##繰り返し処理の開始
for num in [1,2,3,4]:
    print("num",num)
    total=total+num
##for文終了
##結果表示
print("total",total)

##rangeの利用その１
for i in range(10):
    print(i)

##rangeの利用その2
for i in range(1,11,2):
    print(i)

########複雑な文と内包表記は省略########

##zip関数：2つのリストを同時に処理
for one,two in zip([1,2,3],[4,5,6]):
    print("要素は{0},{1}です。".format(one,two))

##while文を使った処理(例：１からの積を求める)
##初期値の設定
p=1
q=1
r=1

##繰り返し条件
while p < 6:
    r=p*r
    p = p+1
    q=q*p
##繰り返し終了    
print("最終的な値は{0}、積は{1}です".format(p,q))
print("rは{0}で、これはｑとは異なります".format(r))

##breakとcontinue
##break
h=1
while h < 10:
    h = h +1
    ##if文の挿入
    if h>5:
        print("５を超えました")
        ##ここで処理終了
        break
    else:
        ##処理続行
        pass


print("最後の値は{0}です。".format(h))

##continue
h=1
while h < 10:
    h = h +1
    ##if文の挿入
    if h>5:
        print("５を超えました")
        ##ここで処理続行
        continue
    else:
        ##処理続行
        pass


print("最後の値は{0}です。".format(h))

##関数(例：フィボナッチ数列)
def cal_fib(n):
    if n ==1 or n ==2:
        return 1
    else:
        return cal_fib(n-1)+cal_fib(n-2)

print(cal_fib(10))
#######もっと楽なアルゴリズムを考えよう#######

##無名関数とmap
##リストなどの要素に対して処理を実行したいときにlambdaを使う
print((lambda a,b: a*b)(3,10))

##mapを使えばさらに楽に
##リストの各要素を2倍したいとき
print(list(map(lambda x:2*x,[1,2,3,4])))

#######reduce関数、filter関数もある#######

##class
##新たな方を定義
class MyCalcClass:
    def __init__(self,x,y):
        self.x = x
        self.y = y

##この方の持つ関数を定義
    def calc_add1(self,a,b):
        return a+b
    
    def calc_add2(self):
        return self.x+self.y

    def culc_multi(self,a,b):
        return a*b

    def calc_print(self,a):
        print("deta:{0}ｙの値{1}".format(a,self.y))

##インスタンスを生成
instance_1=MyCalcClass(1,2)
instance_2=MyCalcClass(5,10)
##それぞれのインスタンスで処理を実行
print("2つの数字の足し算（新たに数字をセット:",instance_1.calc_add1(5,3))
print("2津の数字の足し算（インスタンス化の時の値:",instance_1.calc_add2())
print("2津の数字の掛け算:",instance_1.culc_multi(5,3))
instance_1.calc_print(5)

print("2つの数字の足し算（新たに数字をセット:",instance_2.calc_add1(5,3))
print("2津の数字の足し算（インスタンス化の時の値:",instance_2.calc_add2())
print("2津の数字の掛け算:",instance_2.culc_multi(5,3))
instance_2.calc_print(5)










