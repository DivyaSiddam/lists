def is_sorted_ascending(lst):
    return lst == sorted(lst)
numbers = [1, 2, 3, 4, 5]
print("list  is sorted?", is_sorted_ascending(numbers)) 
