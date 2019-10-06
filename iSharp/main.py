import sys

sys.stdin = open("./data/input.txt")
s = input()
s = s[:-1]
my = s.split(" ")
value_type = my[0]
s = s[len(value_type):]
split = s.split(",")
for split_value in split:
    out_str = value_type
    value_name = ""
    reference_count = 0
    array_count = 0
    pointer_count = 0
    temp_str = split_value.strip()
    oh_str = ""
    for temp_str_idx in range(len(temp_str)):
        temp_str_value = temp_str[temp_str_idx]
        if temp_str_value == "*":
            oh_str = "*" + oh_str

        elif temp_str_value == "[":
            oh_str = "[]" + oh_str

        elif temp_str_value == "]":
            continue
        elif temp_str_value == "&":
            oh_str = "&" + oh_str
        else:
            value_name += temp_str_value

    out_str += oh_str + " " + value_name + ";"
    print(out_str)
