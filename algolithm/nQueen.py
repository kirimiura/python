"""
自力でわからず、以下を参考にしました。
"""

def nQueen(n, example=False):
    place = [-1 for i in range(n)]
    result = n_queen(n, place, 0, 0, example)
    return result

def n_queen(n, place, iter_n, count, example):
    if iter_n == n:
        count += 1
        # show examples of placement
        if example:
            print(place)

    else:
        for i in range(n):
            if queen_placeable(place, iter_n, i):
                place[iter_n] = i
                count = n_queen(n, place, iter_n+1, count, example)

    return count

def queen_placeable(place, iter_n, col):
    for i in range(iter_n):
        #すでに置かれている場所と縦横一致はだめ
        if col == place[i]:
            return False

        #斜めもだめ 
        if col + (iter_n - i) == place[i] or col - (iter_n - i) == place[i]:
            return False

    return True

print(nQueen(8))
