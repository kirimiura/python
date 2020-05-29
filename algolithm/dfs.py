#自分で１から実装してみました
"""
変数はlist(頂点),map(マップの形状),initial(初期位置),goal(目標到達地点)とする
loop開始
今いる場所から(訪れたものリストになければ)frange生成
frangeがない→解なしで終了
frangeの先頭に移動
移動先をfrangeから削除
移動先を訪れたリストに追加
goalなら解を出力、終了、解じゃないならループ
"""
import random
def graph_search_depth(list,map,initial,goal):
    #initialはgoalではないとする
    state=initial
    print("初期位置は{0}です。目標は{1}です".format(state,goal))
    visited=[state]
    frange=[state]
    while True:
        #visitedされてないものをfrange生成
        for s in map[state]:
            if s not in visited:
                frange.append(s)
        #frangeがない→解なしで終了
        if len(frange)==0:
            print("failure")
            exit()
        #frangeの先頭(末尾)にstate移動し、移動先をfrangeから削除(深さ優先の実現)
        state=frange.pop(len(frange)-1)
        print("現在{0}にいます".format(state))
        #移動先を訪れたリストに追加
        visited.append(state)
        #goalなら解を出力、終了
        if goal==state:
            break
    return state      
list1=[0,1,2,3,4,5,6,7,8,9]
map1=[[1,2,3],[0,2,4],[5,6,9],[6,7],[8],[2,6,8,9],[5,8],[0,8,9],[4],[6,8]]
initial1=0
goal1=random.randrange(1,10)
print(graph_search_depth(list1,map1,initial1,goal1))
#一度訪れたところは二度と訪れないようになっている.