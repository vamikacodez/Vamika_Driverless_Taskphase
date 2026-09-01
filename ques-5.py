'''Learn open hashing. Implement a hash table using 2D lists. Input n
integers. Every number where 
num % 10 == 0 goes in sublist 0, 
== 1 goes in sublist 1, and so on. Print the hash table.
num % 10'''
def hashing():
    hash_table = []
    for i in range(10):
        hash_table.append([])

    n = int(input("enter how many numbers you want to insert: "))

    for i in range(n):
        num = int(input("enter number: "))
        index = num % 10
        hash_table[index].append(num)

    print("hash table:")
    for i in range(10):
        print(i, "~", hash_table[i])


hashing()