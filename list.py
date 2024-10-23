#list comprehension
#creating a matrix without list comprehension
matrix = []
for i in range(5):
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)
print(matrix)
#creating a matrix using list comprehension
matrix2 = [[j for j in range(0,5)]for i in range(5)]
print(matrix2)
#filtering a nested list using list comprehension
matrix3 = [[1,2,3],[4,5,6],[7,8,9]]
odd_numbers = [element for row in matrix3 for element in row if element%2!=0]
print(odd_numbers)
#flattingng a list using list comprehension
matrix4 = [[1,2,3,],[4,5],[6,7,8,9,0]]
matrix5 = [k for i in matrix4 for k in i ]
print(matrix5)
matrix = [["apple", "banana", "cherry"],
		["date", "fig", "grape"],
		["kiwi", "lemon", "mango"]]

modified_matrix = [[fruit.capitalize() for fruit in row] for row in matrix]

print(modified_matrix)
# print(list[this one will the the sublist of the main list ][this would be the element inside that sublist])
matrix6 =[]
martix6 = [['name1',1],['name2',2],[['name3',3]]]
for students in matrix6:
    print(students[1])

#here in the for loop students takes the value (i.e. the first list) of the first list itself of the matrix 6
matrix7 = [12,3,4,5,6,6,7,8,9,9,4,4,3,3,]
print(set(matrix7))#the set() get's rid of duplicates
