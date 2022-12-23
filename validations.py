def is_valid_name(name):
    import re
    pattern = r'^[a-zA-Z]{2,20}$'
    return bool(re.match(pattern, name))
def is_valid_phone_number(phone_number):
    if len(phone_number) != 11:
        return False

    if not phone_number.startswith('0'):
        return False

    if phone_number[1] not in ['3', '4', '5', '6']:
        return False
    return True
def is_valid_integer(price, precision=2):
    if not isinstance(price, str):
        return False

    if not all(c in '0123456789.' for c in price):
        return False

    if price.count('.') > 1:
        return False

    if '.' in price:
        if len(price.split('.')[1]) > precision:
            return False

    if price[0] == '-':
        return False

    return True
def is_valid_cnic(cnic):
    if len(cnic) != 13:
        return False

    if not (30000 <= int(cnic[:5]) <= 79999):
        return False

    if cnic[4] not in ['1', '2', '9', '0']:
        return False
    return True
def check_if_empty(value) :
    if not value:
        return False
    else:
        return True
def is_valid_email(email):
    import re
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None
def is_valid_bank_account(account_number):
    if len(account_number) not in (11, 12, 13):
        return False
    if not account_number.isdigit():
        return False
    return True





