# Pypy 3 Solution

def print_formatted(number):
    result = ""
    dec_shift = get_shift_amount(number, 10) + 1
    oct_shift = get_shift_amount(number, 8) + 1
    hex_shift = get_shift_amount(number, 16) + 1
    bin_shift = get_shift_amount(number, 2) + 1

    for num in range(1, number + 1):
        oct_num = oct(num)[2:]
        hex_num = hex(num)[2:]
        bin_num = bin(num)[2:]
        result += " " * (bin_shift - dec_shift)
        result += f"{str(num).rjust(dec_shift)}"
        result += " " * (bin_shift - oct_shift + 1)
        result += f"{oct_num.rjust(oct_shift)}"
        result += " " * (bin_shift - hex_shift + 1)
        result += f"{hex_num.rjust(hex_shift).upper()}"
        result += " "
        result += f"{bin_num.rjust(bin_shift)}"

        if (num != number):
            result += "\n"

    print(result)
        

def get_shift_amount(num, num_level):
    count = 0
    while num >= num_level:
        count += 1
        num //= num_level

    return count

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)