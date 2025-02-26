
######### Sum of Digits of a Number #######
def sum_of_numbers(num):
    return sum(int(digit) for digit in str(abs(num)))

print(sum_of_numbers(2451))