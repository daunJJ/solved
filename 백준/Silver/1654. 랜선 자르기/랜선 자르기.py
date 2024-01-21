# K개의 각기 다른 랜선에서 N개의 길이가 같은 랜선을 만들고자 할때 랜선의 최대 길이
import sys

K, N = map(int, input().split())
K_length = [int(input()) for _ in range(K)]

start, end = 1, max(K_length)

while start <= end:
    
    mid = (start + end) // 2  
    cnt = 0 

    for length in K_length:
        cnt += length // mid

    if cnt < N:
        end = mid - 1  

    if cnt >= N:
        start = mid + 1  

print(end)