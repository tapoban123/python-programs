### Write a program that removes duplicate elements from a list and make a new list with only the unique elements.

given_list = list(map(int, input("Enter the elements separated by space: ").split()))

new_list = []

for item in given_list:
    if new_list.count(item) == 0:
        new_list.append(item)

print(f"The given list: {given_list}")
print(f"The new list after removing duplicates: {new_list}")
