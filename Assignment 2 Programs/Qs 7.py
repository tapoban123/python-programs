### Write a program that rotates the elements Of a list by a specified number Of positions to the left or right.

given_list = list(
    map(int, input("Enter the elements of the list separated by a space: ").split())
)
n = int(input("Enter number of elements to rotate: "))
left_or_right = input("Rotate elements to left or right? (L/R) ").lower()

pop_index = -1 if left_or_right == "r" else 0
insert_index = 0 if left_or_right == "r" else len(given_list)

for i in range(n):
    val = given_list[pop_index]
    given_list.insert(insert_index, val)
    given_list.pop(pop_index)

print(given_list)
