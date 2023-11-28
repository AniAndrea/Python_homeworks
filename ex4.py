'''
Print the following pattern
1 
2 2 
3 3 3 
'''

rows=4
for number in range(rows):
    for j in range(number):
        print(number, end=" ")
    print(" ")
