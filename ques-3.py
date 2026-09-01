'''Create a class with a function that does binary search in a list of strings.
Input a list like Q1, sort it using your Q2 function, input a string, search for it.'''
class sort:
    def __init__(self, l):
        self.l = l

    def selection_sort(self):
        n = len(self.l)
        for i in range(n):
            min = i
            for j in range(i + 1, n):
                if self.l[j] < self.l[min]:
                    min = j
            
            self.l[i], self.l[min] = self.l[min], self.l[i]
        return self.l

    def binary_search(self, target):
        low = 0
        high = len(self.l) - 1

        while low <= high:
            mid = (low + high) // 2

            if self.l[mid] == target:
                return mid
            elif self.l[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1


list = input("Enter strings separated by spaces: ").split(" ")

value = sort(list)
final = value.selection_sort()
print(final)

target = input("Enter the string to search for: ")
result = value.binary_search(target)

if result != -1:
    print(target, "found at index", result)
else:
    print(target, "not found")