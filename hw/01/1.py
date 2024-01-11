# 有使用chatgpt並稍微修改

def ans(n):
    a = [1, 1]

    for i in range(2, n):
        b = a[-1] + a[-2]
        a.append(b)

    return a[:n]

n = int(input("輸入要計算的項數："))

result = ans(n)
print(f"{n} Result：{result}")