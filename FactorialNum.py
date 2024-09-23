'''
Write a program to determine whether &#39;n&#39; is a factorial number or not. Factorial of a
number is the product of all positive numbers from 1 to &#39;n&#39;.
Input format:
The input containing an integer &#39;n&#39; which denotes the given number.
Output format:
If the given number is factorial, print &quot;Yes&quot;. Otherwise, print &quot;No&quot;.
Refer the sample output for formatting.
Sample Input:
6
Sample Output:
Yes
'''
Ans:
def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
def factorials_up_to_n(n):
    factorials={}
    for i in range(1, n+1):
        factorials[i] = factorial(i)
    return factorials
i=int(input("Enter a positive number: "))
result=factorials_up_to_n(n)
for num, fact in result.items():
    print("Factorial of {num} is {fact}")
