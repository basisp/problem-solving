import sys
n=int(input())

cnt2=1
def fib2(n):
    global cnt2
    if n == 1 or n == 2:
        return 1
    
    else:
        cnt2+=1
        return (fib2(n - 1) + fib2(n - 2))
    
fib2(n)

f=[0]*41
cnt1=1
def fibonacci(n):
    global cnt1
    f[1] = f[2] = 1
    for i in range(3, n):
        cnt1+=1
        f[i] =f[i - 1] + f[i - 2]  # 코드2
    return f[n]

fibonacci(n)
print(cnt2,cnt1,sep=' ')