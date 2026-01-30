# TASK 2

students = [("Ali", 85), ("Saad", 95), ("Ahmed", 70), ("Usman", 60), ("Abdullah", 90)]
top_2_students = sorted(students , key = lambda x: x[1])[-2:]
name , marks = list(zip(*students))
pass_students = [x for x in students if x[1] >= 70]
fail_students = [x for x in students if x[1] < 70]
print(f"""
Top 2 Students:
{top_2_students}

Pass Students:
{pass_students}

Fail Students:
{fail_students}
""")

