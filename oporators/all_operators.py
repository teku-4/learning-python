# Arithmetic Operators
number1 = 10
number2 = 5

addition_result = number1 + number2
subtraction_result = number1 - number2
multiplication_result = number1 * number2
division_result = number1 / number2
floor_division_result = number1 // number2
modulus_result = number1 % number2
exponentiation_result = number1 ** number2

print("Arithmetic Operators:")
print(f"{number1} + {number2} = {addition_result}")
print(f"{number1} - {number2} = {subtraction_result}")
print(f"{number1} * {number2} = {multiplication_result}")
print(f"{number1} / {number2} = {division_result}")
print(f"{number1} // {number2} = {floor_division_result}")
print(f"{number1} % {number2} = {modulus_result}")
print(f"{number1} ** {number2} = {exponentiation_result}")
print("\n")

# Comparison Operators
is_equal = number1 == number2
is_not_equal = number1 != number2
is_greater = number1 > number2
is_less = number1 < number2
is_greater_or_equal = number1 >= number2
is_less_or_equal = number1 <= number2

print("Comparison Operators:")
print(f"{number1} == {number2} -> {is_equal}")
print(f"{number1} != {number2} -> {is_not_equal}")
print(f"{number1} > {number2} -> {is_greater}")
print(f"{number1} < {number2} -> {is_less}")
print(f"{number1} >= {number2} -> {is_greater_or_equal}")
print(f"{number1} <= {number2} -> {is_less_or_equal}")
print("\n")

# Logical Operators
logical_and_result = (number1 > 0) and (number2 > 0)
logical_or_result = (number1 < 0) or (number2 > 0)
logical_not_result = not (number1 > number2)

print("Logical Operators:")
print(f"({number1} > 0) and ({number2} > 0) -> {logical_and_result}")
print(f"({number1} < 0) or ({number2} > 0) -> {logical_or_result}")
print(f"not ({number1} > {number2}) -> {logical_not_result}")
print("\n")

# Bitwise Operators
bitwise_and_result = number1 & number2
bitwise_or_result = number1 | number2
bitwise_xor_result = number1 ^ number2
bitwise_not_result = ~number1
left_shift_result = number1 << 1
right_shift_result = number1 >> 1

print("Bitwise Operators:")
print(f"{number1} & {number2} -> {bitwise_and_result}")
print(f"{number1} | {number2} -> {bitwise_or_result}")
print(f"{number1} ^ {number2} -> {bitwise_xor_result}")
print(f"~{number1} -> {bitwise_not_result}")
print(f"{number1} << 1 -> {left_shift_result}")
print(f"{number1} >> 1 -> {right_shift_result}")
print("\n")

# Assignment Operators
assign_value = number1
assign_value += number2
addition_assignment = assign_value

assign_value = number1
assign_value -= number2
subtraction_assignment = assign_value

assign_value = number1
assign_value *= number2
multiplication_assignment = assign_value

assign_value = number1
assign_value /= number2
division_assignment = assign_value

assign_value = number1
assign_value %= number2
modulus_assignment = assign_value

print("Assignment Operators:")
print(f"{number1} += {number2} -> {addition_assignment}")
print(f"{number1} -= {number2} -> {subtraction_assignment}")
print(f"{number1} *= {number2} -> {multiplication_assignment}")
print(f"{number1} /= {number2} -> {division_assignment}")
print(f"{number1} %= {number2} -> {modulus_assignment}")
print("\n")

# Identity Operators
is_same_object = (number1 is number2)
is_not_same_object = (number1 is not number2)

print("Identity Operators:")
print(f"{number1} is {number2} -> {is_same_object}")
print(f"{number1} is not {number2} -> {is_not_same_object}")
print("\n")

# Membership Operators
sample_list = [1, 2, 3, 4, 5]
is_in_list = number2 in sample_list
is_not_in_list = number1 not in sample_list

print("Membership Operators:")
print(f"{number2} in {sample_list} -> {is_in_list}")
print(f"{number1} not in {sample_list} -> {is_not_in_list}")
