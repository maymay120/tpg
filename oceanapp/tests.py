import random
final = ''
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
while len(final) < 6:
    pick = random.choice(nums)
    final+=pick

print(final)