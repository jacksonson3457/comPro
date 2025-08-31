N = int(input())
s_list = list(input())

def main():
    #多分だけど、交換後のA,Bの位置をシュミレートしていく必要はない
    #Aの出現位置を調べて全部を奇数位置か偶数位置に持ってくには何回かを調べれば、Bは勝手に上手いところに収まる気がする
    pos_A = []
    for i in range(2 * N):
        if s_list[i] == 'A':
            pos_A.append(i)
    
    #偶数の場合
    even_count = 0
    for i in range(N):
        now_pos = pos_A[i]
        abs_a = abs(now_pos - 2 * i)
        even_count += abs_a

    #奇数の場合
    odd_count = 0
    for i in range(N):
        now_pos = pos_A[i]
        abs_a = abs(now_pos - (2 * i + 1))
        odd_count += abs_a
    
    return min(even_count, odd_count)

print(main())
