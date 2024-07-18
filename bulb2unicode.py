# Week 0: 0000000000000000010000110101001100110101001100000000000000000000
# Week 1: 0011001000100000010001100100111101010010001000000011001000000000
# Week 2: 0100010001010000010100110101001101000110010001000101010100000000

def main():
    bulbs = input("Enter the bulbs using 1's and 0's: ")
    byte_dictionary = {}
    # iterate over list in intervals of 8
    for i in range(0, 64, 8):
        byte_name = f"byte_{i // 8 + 1}"
        # i + j is used because i will be 0 then 8 then 16... becasye of the intervals of 8
        byte_list = [bulbs[i + j] for j in range(8)]
        # each iteration makes a new byte name as key and assings the list as the value
        byte_dictionary[byte_name] = byte_list

    # for name, byte in byte_dictionary.items():
    #     print(f"{name} : {byte}")

    # Convert each byte list into decimal values, then sum them together. I also added conversion from the number to corresponding unicode
    number_dictionary = {}
    letters = ""
    for byte_name, byte_list in byte_dictionary.items():
        value_name = f"decimal_values{byte_name}"
        dec_digits = []
        for index, value in enumerate(reversed(byte_list)):
            if value == "1":
                dec_digits.append(2**index)
            else:
                dec_digits.append(0)
            number_dictionary[value_name] = dec_digits
            total = sum(number_dictionary[value_name])
            letter = chr(total)
        letters = letters + letter
        print(f"{byte_name} = {total} = {letter}")
    print(f"This week's lightbulb message is: {letters}")


if __name__ == "__main__":
    main()

# Step-by-step --> inefficient
# byte1 = [bulb for bulb in bulbs[0:8]]
# byte2 = [bulb for bulb in bulbs[8:16]]
# print(byte1)
# print(byte2)
