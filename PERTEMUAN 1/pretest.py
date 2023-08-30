# x=1
# print(x<<2)

# print(4 + 3 % 5)

# print(min(max(False,-3,-4), 2,7))

# print((2 + 3) ** 2)
# print(min(max(False,-3,-4), 2,7))
# A = 12
# a = 2

# print(A, a)

# print(2**(3+1))

# sys.version()


# i = 1
# while True:
#     if i%3 == 0:
#         break
#     print(i)
#     # i + = 1

# if 1:
#   print("1 is truthy!")
# else:
#   print("1 is not truthy!")

  
# a, b = 12, 5
# if a + b:
#   print(True)
# else:
#   print(False)

# x = 0
# a = 0
# b = -5
# if a > 0:
#   if b < 0:
#     x = x + 5
#   elif a > 5:
#     x = x + 4
#   else:
#     x = x + 3
# else:
#   x = x + 2
# print(x)


# def bar( z ):
#   i = 1
#   while ( i <= z ):
#     i *= 2
#   return i
#   print (i)
# print (bar( 7 ))

# if 'I am enjoying learning at DPhi':
#   print("Thank You DPhi")
# else:
# #   print("Sorry")

# i = 0
# while i < 3:
#   print('DPhi')
#   i = i+1

# x = ['data', 'science']
# for i in x:
#     i.upper()
# print(x)

# x = 'datascience'
# for i in range(10):
#     print(i
#     )

# x = 0
# while x < 100:
#     x += 2
# print(x)

# for num in range(2,-5,-1):
#   print(num, end = ",")

# numbers = [10, 20]
# items = ["Chair", "Table"]
 
# for x in numbers:
#   for y in items:
#     print(x, y)

# datathons = ['data sprint #1', 'data sprint #2', 'data sprint #3', 'data sprint #4', 'data sprint #5', 'data sprint #5', 'data sprint #6']
# print(list(enumerate(datathons)))

# dphi = 10
# for i in range(10):
#     for j in range(2, 10, 1):
#         if dphi % 2 == 0:
#             continue
#             dphi += 1
#     dphi+=1
# else:
#     dphi+=1
# print(dphi)

# for num in range(10, 14):
#     for i  in range(2, num):
#         if num % i == 1:
#             print(num)
#             break


# a= set([1,2,3,])
# b= set([2,3,4])
# # a.add(b)
# print('dphi' in 'dphidatasciencebootcamp')

# a = ['dphi', 'data', 'science', 'bootcamp', 'dphi', 'deep', 'learning', 'bootcamp']

# print(set(a))
# l = ['dphi', 'data', 'science', 'bootcamp', 'dphi', 'deep', 'learning', 'bootcamp']

# l_new = []

# for item in l:

#   if item in l_new:

#     break

#   else:    

#     l_new.append(item)  

# print(l_new)

# s = {'dphi', 'data', 'science', 'bootcamp', 'deep', 'learning'}
# s.discard('data science')
# print(s)

# bootcamp = {2}
# bootcamp1 = {'dphi', 'data', 'science', 'bootcamp'}
# bootcamp2 = {'dphi', 'deep', 'learning', 'bootcamp'}
# bootcamps = bootcamp1.union(bootcamp2)
# bc = bootcamp.union(bootcamps)
# print(bc)

# courses = {'Python Beginners', 'NumPy', 'Pandas', 'Matplotlib', 'EDA'}
# courses.update(['Python Intermediate', 'Maths'])
# print(courses)

# Import the necessary dependencies
# import math

# # Define the scores variable
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

# def is_A_student(score):
#     return score > 75

# over_75 = list(map(is_A_student, scores))
# print(over_75)

# numbers = [1, 2, 3]
# print(list(map(lambda x: x + 1, numbers)))

# func = lambda x: return x
# print(func(10))

# (lambda x: (x + 3) * 5 / 2)(5)
# my_string= "hello world"

# print([print(i) for i in my_string if i not in "aeiou"])

n = [2, 1, 2, 3, 4, 5, 6]
fn = filter(lambda x: x%2 == 0, n)
print(list(fn))