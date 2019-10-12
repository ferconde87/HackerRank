# Without using zip
# N, X = map(int, input().split())
# marks = [0]*N #marks[i] total marks of student 'i'
# for _ in range(X):
#     cur = list(map(float, input().split()))
#     for i in range(N):
#         marks[i] += cur[i]
# for total in marks:
#     print(total/X)

# With tuples + zip just for fun
# N, X = map(int, input().split())
# list_of_marks = []
# for subject in range(X):
#     t = ()
#     for x in list(map(float,input().split())):
#         t += (x,)    
#     list_of_marks.append(t)

# for student_marks in zip(*list_of_marks):
#     print(sum(student_marks)/X)

N, X = map(int, input().split())
list_of_marks = []
for subject in range(X):
    list_of_marks += [map(float,input().split())]

for student_marks in zip(*list_of_marks):    
    print(sum(student_marks)/X)
