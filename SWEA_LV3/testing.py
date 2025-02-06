import sys
sys.stdin = open("sample_input.txt", "r")

T_input= int(input())

for T in range(1, T_input+1):
    N, M = map(int, input().split())
    
    answer = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_score = 0
    min_score = 5000
    
    for i in range(N):
        scores = [0]*M
        for j in range(M):
            if arr[i][j] == answer[j]:
                scores[j] = 1
                if j > 0 and arr[i][j-1] == answer[j-1]:
                    scores[j] = scores[j-1] + 1
        
        score = sum(scores)

        if max_score < score:
            max_score = score

        if min_score > score:
            min_score = score

    print(f"#{T} {max_score-min_score}")
