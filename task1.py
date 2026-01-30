
# TASK 1
grocery = [120, 50, 75, 200, 30]
new_grocery = list(map(lambda x: x - (x*0.1) , grocery))
over_50 = list(filter(lambda x: x > 50 , new_grocery))
print(sorted(over_50))
