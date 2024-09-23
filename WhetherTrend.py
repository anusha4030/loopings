'''
Write a program to check whether the given number is a trendy number or not. A number
is said to be a trendy number if and only if it has 3 digits and the middle digit is divisible by
3.
Input format:
The input containing an integer &#39;n&#39; which denotes the given number
Output format:
If the given number is a trendy number, then print &quot;Trendy Number&quot;. Otherwise, print &quot;Not a
Trendy Number&quot;.
Refer the sample output for formatting.
Sample Input:
791
Sample Output:
Trendy Number
'''
Ans:
def is_trendy_number(num):
    if num<100 or num>999:
        return False
    middle_digit=(num//10)%10
    return middle_digit%3==0
number=int(input("Enter a three-digit number: "))
if is_trendy_number(number):
    print("{number} is a trendy number.")
else:
    print("{number} is not a trendy number.")
