''' Write a function for matrix multiplication. It should support any
dimensions and print errors where multiplication is impossible.'''
import numpy as np
def matrix_multiplication():
    r_a= int(input("enter the number of rows in matrix A:"))
    c_a= int(input("enter the number of columns in matrix A:"))
    r_b= int(input("enter the number of rows in matrix B:"))
    c_b= int(input("enter the number of columns in matrix B:"))
    
    if(c_a!=r_b):
        print("alas! matrix multiplication is not possible :(")
        return
    else:
        print("congratulations! matrix multiplication is possible :)\n")
        
    print("enter elements of matrix A:")
    a = []
    for i in range(r_a):
        row = []
        for j in range(c_a):
            num = int(input("enter element: "))
            row.append(num)
        a.append(row)

    print("enter elements of matrix B:")
    b = []
    for i in range(r_b):
        row = []
        for j in range(c_b):
            num = int(input("enter element: "))
            row.append(num)
        b.append(row)

    result = []
    for i in range(r_a):
        row = []
        for j in range(c_b):
            row.append(0)
        result.append(row)

    for i in range(r_a):
        for j in range(c_b):
            for k in range(c_a):
                result[i][j] = result[i][j] + a[i][k] * b[k][j]

    print("result:")
    for row in result:
        print(row)

#method 2 using numpy arrays 
def matrix_multiplication_numpy():
    r_a = int(input("enter the number of rows in matrix A:"))
    c_a = int(input("enter the number of columns in matrix A:"))
    r_b = int(input("enter the number of rows in matrix B:"))
    c_b = int(input("enter the number of columns in matrix B:"))

    if c_a != r_b:
        print("alas! matrix multiplication is not possible :(")
        return

    print("congratulations! matrix multiplication is possible :)")

    print("enter elements of matrix A:")
    a = []
    for i in range(r_a):
        row = []
        for j in range(c_a):
            num = int(input("enter element: "))
            row.append(num)
        a.append(row)

    print("enter elements of matrix B:")
    b = []
    for i in range(r_b):
        row = []
        for j in range(c_b):
            num = int(input("enter element: "))
            row.append(num)
        b.append(row)

    a = np.array(a)
    b = np.array(b)

    result = np.matmul(a, b)

    print("result:")
    print(result)

def menu():
    print("this is a menu driven program to do following:")
    print(" 1. do matrix multiplication generally")
    print("2. do matrix multiplication using numpy")
    
    choice= int(input("enter the choice as either 1 or 2: "))
    if (choice==1):
        matrix_multiplication()
    elif (choice==2):
        matrix_multiplication_numpy()
    else:
        print("invalid input")

menu()