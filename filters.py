import string


def filter_digits_to_text(message):
    for digit, digit_text in [
            ('0', 'zero'),
            ('1', 'one'),
            ('2', 'two'),
            ('3', 'three'),
            ('4', 'four'),
            ('5', 'five'),
            ('6', 'six'),
            ('7', 'seven'),
            ('8', 'eight'),
            ('9', 'nine')]:
        message = message.replace(
            digit,
            ' %s ' % digit_text,
        )
    return message


def filter_remove_nonletters(message):
    char_whitelist = string.ascii_letters + ' '
    return ''.join([
        char
        if char in char_whitelist else ' '
        for char in message])
