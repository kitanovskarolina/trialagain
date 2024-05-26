def swap_numbers(a, b):
    def number_to_string(n):
        if n == 0:
            return "zero"
        elif n == 1:
            return "one"
        elif n == 2:
            return "two"
        elif n == 3:
            return "three"
        else:
            return "Invalid number"

    a_str = number_to_string(a)
    b_str = number_to_string(b)

    return a_str, b_str
