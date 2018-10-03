num_1 = -1
num_2 = 1

num_3 = 0
n = int(input("Enter the number of terms : "))

fibo = []

for i in range(n):
    num_3 = num_1 + num_2
    num_1 = num_2
    num_2 = num_3
    
    fibo.append(num_3)

print("The Fibonaci Series is : ")
print(fibo)