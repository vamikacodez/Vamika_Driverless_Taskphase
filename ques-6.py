'''Improve Q5. Insert each new number so the sublist stays sorted. Do not
sort after insertion. Hint, find the insertion index using binary search.'''
def find_position(sublist, num):
    low = 0
    high = len(sublist) - 1

    while low <= high:
        mid = (low + high) // 2

        if sublist[mid] == num:
            return mid
        elif sublist[mid] < num:
            low = mid + 1
        else:
            high = mid - 1

    return low


def hashing():
    hash_table = []
    for i in range(10):
        hash_table.append([])

    n = int(input("enter how many numbers you want to insert: "))

    for i in range(n):
        num = int(input("enter number: "))
        index = num % 10
        pos = find_position(hash_table[index], num)
        hash_table[index].insert(pos, num)

    print("hash table:")
    for i in range(10):
        print(i, "->", hash_table[i])


hashing()