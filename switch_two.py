nums = []
for i in range(1, 11):
    nums.append(i)
print(nums)

A = int(input("První prvek který vyměníte "))
B = int(input("Druhý prvek který vyměníte "))

pom = nums[A]
nums[A] = nums[B]
nums[B] = pom

print(nums)