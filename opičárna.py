nums = []
for i in range(1, 11):
    nums.append(i)
print(nums)
while True:
    A = int(input("První prvek který vyměníte "))
    B = int(input("Druhý prvek který vyměníte "))

    if A!=B and A>=0 and B>=0 and A < len(nums) and B < len(nums):
        break

pom = nums[A]
nums[A] = nums[B]
nums[B] = pom

print(nums)