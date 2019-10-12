import sys

sys.stdin = open("./data/input.txt")
n = int(input())
my_str = input()
number_stack = []
operation_stack = []
is_continue = False
for my_str_index in range(len(my_str)):
    if is_continue:
        is_continue = False
        continue
    my_str_value = my_str[my_str_index]
    if my_str_value.isdigit():
        number_stack.append(int(my_str_value))
    else:
        if my_str_value == "*":
            is_continue = True
            number_stack[-1] *= int(my_str[my_str_index + 1])
        else:
            operation_stack.append(my_str_value)
while True:
    if len(operation_stack) == 0:
        break
    operation = operation_stack.pop()
    number = number_stack.pop()
    if operation == "+":
        number_stack[-1] += number
    elif operation == "-":
        number_stack[-1] -= number
result = number_stack[0]
print()
