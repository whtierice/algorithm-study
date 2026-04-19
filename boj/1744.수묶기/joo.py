import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

pos = sorted([x for x in nums if x > 1], reverse=True)  
ones = nums.count(1)
neg = sorted([x for x in nums if x < 0])                 
zeros = nums.count(0)

result = 0

# 양수: 큰 수끼리 묶기
for i in range(0, len(pos) - 1, 2):
    result += pos[i] * pos[i + 1]
if len(pos) % 2 == 1:
    result += pos[-1]

# 1은 그냥 더하기
result += ones

# 음수: 절댓값 큰 것끼리 묶기
for i in range(0, len(neg) - 1, 2):
    result += neg[i] * neg[i + 1]
if len(neg) % 2 == 1:
    if zeros == 0:
        result += neg[-1] 

print(result)
