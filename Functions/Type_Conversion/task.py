
def convert_integer(number):
    print(type(number))  # Print type of variable "number"
    float_number = float(number)
    print(type(float_number))  # Print type of variable "float_number"
    print(float_number)  # Print its value
    return float_number


def convert_float(float_number):
    print(type(float_number))  # Print type of variable "float_number"
    int_number = int(float_number)
    print(type(int_number))  # Print type of variable "converted_float_number"
    print(int_number)  # Print its value
    return int_number
