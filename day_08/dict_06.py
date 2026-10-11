"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
"""

nums = [1, 2, 3, 3]

# {1: 1, 2: 1, 3: 2}
# {1: [0], 2: [1], 3: [2, 3]}

# sample_dict = {}
# for num in nums:
#     sample_dict[num] = nums.count(num)

# print(sample_dict)


sample_dict = {}
for idx, num in enumerate(nums):
    sample_dict.setdefault(num, []).append(idx)

print(sample_dict)

# {}
# {1: [].append(0) -> [0]} -> {1: [0]}
# {1: [0], 2: [].append(1) -> [1]} -> {1: [0], 2: [1]}
# {1: [0], 2: [1], 3: [].append(2)} -> {1: [0], 2: [1], 3: [2]}
# {1: [0], 2: [1], 3: [2].append(3)} -> {1: [0], 2: [1], 3: [2, 3]}


# counter = 0
# for i in nums:
#     if nums.count(i) > 1:
#         print("duplicate found")
#         break
