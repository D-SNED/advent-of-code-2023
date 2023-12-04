def calibrate_values():
    with open("advent_of_code/day1/day1.txt", "r") as file:
        data = file.read()
        data = data.split("\n")

    # iterate over each element in the array
        # iterate over each character in the element
            # if that element is a digit
                # add it to a string
        # if string length is 1
            # add that value + that value to a total
        # add first and last number to total

        total = 0

        for string in data:
            number_substring = ""
            for char in string:
                if char.isdigit():
                    number_substring += char
            if len(number_substring) > 0:
                if len(number_substring) == 1:
                    total += (int(number_substring[0] + number_substring[0]))
                else:
                    total += (int(number_substring[0] + number_substring[-1]))

        return total

print(calibrate_values())
