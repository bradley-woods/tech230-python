# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

n = input("Enter a number: ")

nn = n + n
nnn = n + n + n

ans = int(n) + int(nn) + int(nnn)
print(ans)
