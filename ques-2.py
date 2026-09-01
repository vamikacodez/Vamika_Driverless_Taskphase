'''Create a class with a function that does selection sort on a list of
strings. Input a list like Q1, call the function, print the output.'''

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


list = ["Banana", "Apple", "Cherry", "Mango", "Q1"]

# Instantiate the class and call the function
value = sort(list)
final = value.selection_sort()


print("Sorted list:", final)