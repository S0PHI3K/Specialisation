#Given an array of integers nums and an integer target, return two numbers inside that array such that they add up to target.
#You may assume that each input would have at least one solution, and you may not use the same element twice.
#You can return the answer in any order.
#Take into consideration Big O Time & Space Complexity

def twoSum(numbers, target):
    hashTable = {}
    for num in range(len(numbers)):
        match = target - numbers[num]
        if match in hashTable:
            print(numbers[num], match)
        hashTable[numbers[num]] = numbers[num]
    else:
        return []

numbers = [3,7,8,2,10,-1]
target = 10
twoSum(numbers, target)
