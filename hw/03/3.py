def generate_permutations(elements):
    if len(elements) == 0:
        return [[]]

    result = []
    for i in range(len(elements)):
        current_element = elements[i]
        remaining_elements = elements[:i] + elements[i+1:]
        for perm in generate_permutations(remaining_elements):
            result.append([current_element] + perm)

    return result

# 生成指定長度的排列
def generate_permutations_of_length(n):
    elements = list(range(n))
    permutations = generate_permutations(elements)
    return permutations

# 測試並輸出結果
test_lengths = [2, 3, 4]

for length in test_lengths:
    permutations = generate_permutations_of_length(length)
    print(f"排列長度 {length}：")
    for perm in permutations:
        print(perm)
    print()
