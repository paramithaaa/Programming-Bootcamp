"""
In this code, we are trying to display the number int the list.
To do that, we declare a function called list_to_integer. In the function, we declare a
variable called 'result' which will store the end result. Then we iterate through each
digit from left to right in the list. We use for loop because the loop should end when
it has reached all digits in the list. In the loop, we multiply the current result by
10 and add the digit to the result.

The logic behind this code:
- The position of each digit in the list determine its value. The first element will be
the thousands (largest value), 2nd element is the hundreds, 3rd element is the tens, and 
4th element is the ones.
- What we need to do is to add the digit to the 'result' variable, shift the postition
to the left (ones to tens, tens to hundreds, and so on and so forth), then add the next 
digit. 
- We realise that thousands, hundreds, tens, and ones, they all differ by a factor of 
10 (ones multiplied by 10 becomes tens, and so on and so forth). Hence, we do it by 
iterating through each element of the list, store it to the 'result' variable, then
multiply by 10 to shift it to the left.

Example:
lst1 = [8,3,5,1]

iteration 1:
result = 0*10+8=8

iteration 2:
result = 8*10+3=83

iteration 3:
result = 83*10+5=835

iteration 4:
result = 835*1018=8351 (this is the final result)
"""

def list_to_integer(lst):
    result = 0 #declaring the variable to store result
    for i in lst: #iterating through each element of the list
        result = i + (result*10) # formula to execute the logic
    return result

#testcases
lst1 = [8,3,5,1]
lst2 = [1,2,3,4]
lst3 = [1,3,5,7]

print(list_to_integer(lst1))
print(list_to_integer(lst2))
print(list_to_integer(lst3))