def define_data_type_and_calculate(type, value):
    result = 0
    if type == 'int':
        result = int(value) * 2
    elif type == 'real':
        result = float(value) * 1.5
    elif type == 'string':
        result = '$' + value + '$'

    return result


value_type = input()
input_value = input()

result_from_calculations = define_data_type_and_calculate(value_type, input_value)

if type(result_from_calculations) == float:
    print(f'{result_from_calculations:.2f}')
else:
    print(result_from_calculations)