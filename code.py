binary_data = ""
with open("coverttext.txt", "r") as file:
    for singleline in file:
        for char in singleline:
            if char == ' ':
                binary_data += '0'
            elif char == '\t':
                binary_data += '1'
            else:
                binary_data += ' ' 


binary_values = [val for val in binary_data.split() if len(val) == 7]

print(binary_values)

message = "".join(chr(int(val, 2)) for val in binary_values)

print(message)