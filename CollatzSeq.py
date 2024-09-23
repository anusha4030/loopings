'''
4)The rules for generating Collatz Sequence are:
If n is even: n = n / 2
If n is odd: n = 3n + 1
For example, if the starting number is 5 the sequence is:
5 -&gt; 16 -&gt; 8 -&gt; 4 -&gt; 2 -&gt; 1
It has been proved for almost all integers, the repeated application of the above rule will
result in a sequence that ends at 1.
Input format:
The input containing an integer &#39;n&#39; which denotes the given number

Output format:
Print the numbers in the sequence and also print the number of times the rule has to be
applied in order to reach 1.
Refer the sample output for formatting.
Sample Input:
5
Sample Output:
5
16
8
4
2
1
5
'''
Ans:
def collatz_sequence(n):
    s=0
    sequence=[]

    while n!=1:
        sequence.append(n)
        if n%2==0:
            n=n//2
        else:
            n=3*n+1
        s+=1
    sequence.append(1)  
return sequence, s
n=int(input("Enter a positive number: "))
sequence,s=collatz_sequence(n)
print("Collatz sequence: {sequence}")
print("Number of steps to reach 1: {s}")
