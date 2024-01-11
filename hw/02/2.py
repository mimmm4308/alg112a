# 方法 1
def power2n_1(n):
    return 2**n

# 方法 2a：用遞迴
def power2n_2a(n):
    if n == 0:
        return 1
    else:
        return power2n_2a(n-1) + power2n_2a(n-1)

# 方法 2b：用遞迴
def power2n_2b(n):
    if n == 0:
        return 1
    else:
        return 2 * power2n_2b(n-1)

# 方法 3：用遞迴+查表
def power2n_3(n, memo={}):
    if n == 0:
        return 1
    elif n in memo:
        return memo[n]
    else:
        result = power2n_3(n-1, memo) + power2n_3(n-1, memo)
        memo[n] = result
        return result

# 輸入
n = int(input("輸入n："))

# 輸出結果
print(f"方法 1  結果：{power2n_1(n)}")
print(f"方法 2a 結果：{power2n_2a(n)}")
print(f"方法 2b 結果：{power2n_2b(n)}")
print(f"方法 3  結果：{power2n_3(n)}")