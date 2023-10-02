N = int(input())
print(sum(n for n in range(2, 1000000) if n == sum(int(i) ** N for i in str(n))))
