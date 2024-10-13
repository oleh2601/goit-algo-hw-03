import re


def normalize_phone(phone_number):
    #using regular expression to delete the symbols("-()\") 
    #any whitespaces chars and letters 
    phone_number = re.sub(r'[-()\s\\a-zA-Z]', '', phone_number)

    #handling the country code issue 

    phone_number = re.sub(r'^0', '+380', phone_number)
    phone_number = re.sub(r'^380', '+380', phone_number)

    """
    alternative more simplistic solution:

    if phone_number.startswith('0'):
        phone_number = '+380' + phone_number
    elif phone_number.startswith('380'):
        phone_number = '+' + phone_number
        
    """

    return phone_number

#input data from the example in the task
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]


sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

#output test
#print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
