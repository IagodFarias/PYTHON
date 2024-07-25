'''
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 
1
2
+
2
2
+
2
2
=
9
1 
2
 +2 
2
 +2 
2
 =9.

'''

number = [3, 4, 3]
def solution(number):
    sum = 0
    for c in number:
        sum += c**2
    return sum
    



