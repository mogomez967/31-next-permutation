from itertools import permutations

def nextPermutation(nums):
    # given a array of ints, find the next possible rearrangment of ints
    # lexico greater than what was passed. EX: 123 -> 132 -> 213 -> 231
    result = list(permutations(nums))
    result.sort()
    magic = result.index(tuple(nums))
    answer = result[0]
    flag =True

    if magic < len(result)-1:
        while result[magic] <= tuple(nums):
            magic += 1
            if magic > len(result)-1:
                flag = False
                break
        if flag:
            answer = result[magic]
    
    nums.clear()
    for i in answer:
        nums.append(i)

nums = [5, 1, 1]
# print("answer ", nextPermutation(nums))
nextPermutation(nums)
print(nums)