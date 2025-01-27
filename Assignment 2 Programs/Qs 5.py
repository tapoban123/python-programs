### Write a program that finds the intersection and union of two lists.

list1 = list(
    map(int, input("Enter the elements of first list separated by a space: ").split())
)
list2 = list(
    map(int, input("Enter the elements of second list separated by a space: ").split())
)

intersection = [x for x in list1 if x in list2]
union = [*list1, *list2]

print(f"Intersection = {list(set(intersection))}")
print(f"Union = {list(set(union))}")
