import re

def validate_date(date_string):
    pattern = r'(\d{1,2})\s([а-яА-Я]+)\s(\d{4})'
    if re.match(pattern, date_string):
        return True
    else:
        return False

date = '12 Августа 2023'
is_valid = validate_date(date)
print(is_valid)  # Возвращает значение True, если дата действительна; в противном случае - значение False.