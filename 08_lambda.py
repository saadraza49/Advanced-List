# Lambda Function

add = lambda a,b : a+b
print(add(10,20))
# Lambda Function with filter
numbers = [1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda x : x%2 == 0 , numbers))
print(even)
# Lambda Function with map
numbers = [1,2,3,4,5,6,7,8,9,10]
squared = list(map(lambda x : x*x , numbers))
print(squared)