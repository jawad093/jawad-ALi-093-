def validate_card(card_number):   
    
    check_digit = card_number[-1]
    card_number = card_number[:-1] 
    

    reversed_number = card_number[::-1]
    
    processed_digits = []
    
   
    for index, digit in enumerate(reversed_number):
        num = int(digit)
        if index % 2 == 0:
            num *= 2
            if num > 9:  
                num -= 9
        processed_digits.append(num)
    
   
    total_sum = sum(processed_digits) + int(check_digit)
    

    if total_sum % 10 == 0:
        return "Valid card"
    else:
        return "Invalid card"

card_number = input("Enter your 16-digit card number: ")

if len(card_number) != 16 or not card_number.isdigit():
    print("Invalid input. Card number must be exactly 16 digits.")
else:
    print(validate_card(card_number))
