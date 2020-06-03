#WEEK7
##chapter7
##モデルのチューニング
#新しいデータに適合できない
#→過学習→ホールドアウト法、交差検証法
#モデルの良さの指標
#→混同行列、ROC曲線
#精度の良いモデルづくり
#→アンサンブル学習、バギンス、ブースティング

#ホールドアウト法
#教師データとテストデータを分ける
#交差検証法
#データをk分割→ｋ回学習（それぞれの学習で、1/kのデータが検証用
#実装
# 必要なライブラリ等のインポート
from sklearn.datasets import load_breast_cancer
from sklearn.tree import  DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

cancer = load_breast_cancer()
# 決定木クラスの初期化
tree = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=0)

# k分割交差検証の実行
scores = cross_val_score(tree, cancer.data, cancer.target, cv=5)
# 結果の表示
print('Cross validation scores: {}'.format(scores))
print('Cross validation scores: {:.3f}+-{:.3f}'.format(scores.mean(), scores.std()))

#ハイパーパラメータ
#→各モデルの最適パラメータを決めるもの
#グリッドサーチ(例　SVC)

# インポート
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
# 乳がんのデータを読み込み
cancer = load_breast_cancer()

# 訓練データとテストデータに分ける 
X_train, X_test, y_train, y_test = train_test_split(cancer.data,
                                                    cancer.target,
                                                    stratify = cancer.target,
                                                    random_state=0)

# ハイパーパラメータのすべての組み合わせでモデルを構築・検証
scores = {}
for gamma in np.logspace(-3, 2, num=6):
    for C in np.logspace(-3, 2, num=6):
        svm = SVC(gamma=gamma, C=C)
        svm.fit(X_train,y_train)
        scores[(gamma, C)] = svm.score(X_test, y_test)

# 検証結果をscoresに格納 
scores = pd.Series(scores)

# 表示
print('ベストスコア:{:.2f}'.format(scores.max()))
print('その時のパラメータ(gamma, C):{}'.format(scores.idxmax()))

# ヒートマップを表示。縦軸にgamma、横軸にCを表示
sns.heatmap(scores.unstack())

#パフォーマンスチューニング
#特徴量エンジニアリングが大切
#学習不足か過学習か
#モデル構築の際の注意
#→未知の情報や未来の情報が学習データに取り込まれている
#→大体正解率が高すぎるので疑うべき

#モデルの評価指標
#混同行列
#予測と実際の対応行列
#例　癌（かかっている　0　かかっていない　１）
#正解率　予測＝実際の確率
#適合率　癌であると予測したもののうち、正解だった確率
#再現率　実際の癌の人数のうち、どれくらいを予想できていたか
#適合率と再現率はトレードオフ
#F1スコア　適合率と資源率の調和平均
#↑どっちを優先？→場合による（迷惑メール、癌の予測）

#ROC曲線
#縦軸真陽性率（再現率）、横軸偽陽性率（実際が負の例を正の例としてしまった場合
#実装例
# インポート
from sklearn.linear_model import LogisticRegression

# 乳がんのデータを読み込み
cancer = load_breast_cancer()

# 訓練データとテストデータに分ける
X_train, X_test, y_train, y_test = train_test_split(cancer.data,
                                                    cancer.target,
                                                    stratify = cancer.target,
                                                    random_state=66)
# LogisticRegressionクラスの初期化と学習
model = LogisticRegression(random_state=0)
model.fit(X_train, y_train)

# テスト用データの予測確率を計算
results = pd.DataFrame(model.predict_proba(X_test), columns=cancer.target_names)

# 先頭の5行を表示
results.head()

#AUC→ROCに基づいた評価
#不均衡データにROCは強い

#アンサンブル学習
#バギング
#→元の学習データを重複ありで学習データ増やす
#実装例
# インポート
from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
# 乳がんのデータを読み込み
cancer = load_breast_cancer()
# 訓練データとテストデータに分ける
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, stratify = cancer.target, random_state=66)
# k-NNモデルとそのバギングの設定
models = {
    'kNN': KNeighborsClassifier(),
    'bagging': BaggingClassifier(KNeighborsClassifier(), n_estimators=100, random_state=0) 
}
# モデル構築
scores = {}
for model_name, model in models.items():
    model.fit(X_train, y_train)
    scores[(model_name, 'train_score')] = model.score(X_train, y_train)
    scores[(model_name, 'test_score')] = model.score(X_test, y_test)
# 結果を表示
pd.Series(scores).unstack()

#ぶースティング
#→よくわからないけどすごい
#実際は、ランダムフォレストか勾配ブースティングを使う



