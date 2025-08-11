# Credit card validator by Ahum Maitra

credit_card_number = input("Enter your credit card number : \n>")
sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Replace any '-' with an empty string
temp_credit_card_number = credit_card_number
temp_credit_card_number = temp_credit_card_number.replace("-", "")
temp_credit_card_number = temp_credit_card_number.replace(" ", "")
temp_credit_card_number = temp_credit_card_number[::-1]


# Add all digits in the odd places from right to left
# temp_credit_card_number = list(map(int , str(temp_credit_card_number)))
temp_credit_card_number = [int(digit) for digit in temp_credit_card_number]

for index, digit in enumerate(temp_credit_card_number):
    if index % 2 == 0:
        sum_odd_digits += digit

    # no3 step
    else:
        doubled = digit * 2
        if doubled > 9:
            doubled -= 9
        sum_even_digits += doubled


# no4 step

total = sum_even_digits + sum_odd_digits

# no5 step
if total % 10 == 0:
    print("Valid")
else:
    print("Invalid")
