# Zip Function

roll_no = [1,2,3]
name = ["Saad" , "Ali" , "Ahmed"]
record = list(zip(roll_no , name))
print(record)

# Adding 5 marks to each student using Zip Function
name = ["Saad" , "Ali" , "Ahmed", "Abdullah"]
marks = [45,46,43,42,32]

updated_marks = []        # For adding 5 marks to each student
lst = list(zip(name,marks))
for i in lst:
    for j in i:
        print(j , end=" ")
    print()
updated_marks = list(map(lambda x : x+5 , marks))
print(updated_marks)
# Can also be done like this down below
for i in marks:
    i = i+5
    updated_marks.append(i)
print(updated_marks)  