input_str = input("Enter a dictionary: ")
input_list = eval(input_str)

def unique(d_list):
    values = []
    for d in d_list:
        values.extend(d.values())
    return list(set(values))

result = unique(input_list)

print("Unique Values: ", result)

#Example 
# Enter a dictionary: [{"V": "S001"},{"V": "S002"},{"VI": "S001"},{"VII": "S005"},{"VIII": "S005"},{"V": "S009"},{"VIII": "S007"}]
# Unique Values:  ['S009', 'S005', 'S007', 'S001', 'S002']