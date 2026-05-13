def format_name(first_name: str, last_name: str) -> str | None:
    """Take a first and last name and format it 
    to return the title case version of the name."""
    
    if first_name == '' or last_name == '':
        return
    
    return (first_name + ' ' + last_name).title()


def function_1(text: str) -> str:
    return text + text


def function_2(text: str) -> str:
    return text.title()


print(format_name(input('What\'s your first name? '), input('What\'s your last name? ')))

print(function_2(function_1("hello")))