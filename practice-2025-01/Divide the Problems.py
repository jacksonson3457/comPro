N = int(input())
questions = list(map(int, input().split()))
sorted_questions = sorted(questions)

mid = N // 2
median = (questions[mid] + questions[mid-1]) // 2

def how_many_devide(mid1, mid2):
    if mid1 == mid2: return 0
    return mid2 - mid1

print(how_many_devide(sorted_questions[mid-1], sorted_questions[mid]))