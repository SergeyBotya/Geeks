import re

def mail(arg):
    email_parse_dict = {'username': '', 'domain': ''}
    RE_PARSE = re.compile(r'[a-zA-Z0-9]+[.-_]*[a-zA-Z0-9]+@[a-zA-Z0-9-]+(\.[A-Z|a-z]{2,})')
    RE_NAME = re.compile(r'@')
    try:
        assert RE_PARSE.fullmatch(arg)
        name_list = RE_NAME.split(arg)
        email_parse_dict['username'] = name_list[0]
        email_parse_dict['domain'] = name_list[1]
        print(email_parse_dict)
    except AssertionError as ValueError:
        print(f'ValueError: wrong email: {arg}')
        raise ValueError

mail('botyas13@gmail.com')