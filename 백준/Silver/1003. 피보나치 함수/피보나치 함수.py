# 피보나치 호출 시 fib(0)과 fib(1)이 호출되는 횟수 구하기
# 피보나치를 메모이제이션으로 구현 & [zero 호출 수,  one 호출 수]로 구성 
def fibonacci(n):
    if fib[n] == []:
        if n == 0:
            fib[0] = [1,0]  # zero 수, one 수
        elif n == 1:
            fib[1] = [0,1]  # zero 수, one 수
        else:
            fib[n] = [fibonacci(n-2)[0] + fibonacci(n-1)[0],  fibonacci(n-2)[1] + fibonacci(n-1)[1]]  # zero 덧셈, one 덧셈
    return fib[n]  # 리스트에 존재하면 중단하고 바로 return 

# 테스트 케이스 개수 T개 받기
T = int(input())

# fibonacci(n)에서 호출되는 0, 1 개수 구하기 
for i in range(T):
    n = int(input())
    # fib 초기화
    fib = [[]] * (n+1)
    print(fibonacci(n)[0],fibonacci(n)[1])