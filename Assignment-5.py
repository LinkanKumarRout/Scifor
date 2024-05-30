#1. Finding Mean, Median and Mode

nums = [3, 1, 2, 2, 3, 4, 5, 5, 5, 6]
# ---------- Mean -------------
mean = sum(nums) / len(nums)
print(f"Mean is = {mean}")

# ---------- Median ------------
sorted_nums = sorted(nums)
length = len(sorted_nums)

if length % 2 == 0:
  median = (sorted_nums[length // 2 - 1] + sorted_nums[length // 2]) / 2
else:
  median = sorted_nums[length // 2]

print(f"Median is = {median}")

# ---------- Mode ---------------
frequency = {}.fromkeys(set(nums), 0)
for num in nums:
  if num in frequency:
    frequency[num] += 1

max_freq_num = max(frequency.values())
for num in frequency:
  if frequency[num] == max_freq_num:
    mode = num

print(f"Mode is = {mode}")

#2. Program to find names start with 'A'

names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Ivy", "Jack", "Abhi","Katie", "Leo", "Mia", "Noah", "Olivia", "Peter", "Quinn", "arun", "Rachel", "Sam", "Taylor", "Uma", "agastya", "Victor", "Wendy", "Xander", "Yvonne", "Zane"]

for name in names:
  if name[0] in "aA":
    print(name)