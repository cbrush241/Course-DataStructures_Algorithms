from random import randint

# inefficient algorithm to find max pair product of a list
def max_pairwise_product_naive(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product, numbers[first] * numbers[second])
    return max_product

# faster algorithm to find max pair product of a list
def max_pairwise_product_fast(numbers):
    n = len(numbers)
    index1 = 0
    for i in range(1, n):
        if numbers[i] > numbers[index1]:
            index1 = i
    if index1 == 0:
        index2 = 1
    else:
        index2 = 0
    for i in range(1, n):
        if i != index1 and numbers[i] > numbers[index2]:
            index2 = i
    return numbers[index1] * numbers[index2]

# automatically generate a list of numbers to confirm the fast/slow algos get same answers
def stress_test(N, M):
    A = []
    while True:
        n = randint(2, N)
        for i in range(1, n):
            A.append(randint(0, M))
        print(A)
        result1 = max_pairwise_product_naive(A)
        result2 = max_pairwise_product_fast(A)
        if result1 == result2:
            print('OK')
        else:
            print('Wrong answer:', result1, result2)
            return



if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product_fast(input_numbers))

