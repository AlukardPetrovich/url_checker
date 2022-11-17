from pprint import pprint
import requests
import validators


def check_methods(url: str):
    """
    Сюда можно добавить все необходимые методы.
    Для проверки работы кода останавливаемся на 5 методах.
    """
    url_result = {}
    status_code_get = requests.get(url).status_code
    if status_code_get != 405:
        url_result['GET'] = status_code_get
    status_code_post = requests.post(url).status_code
    if status_code_post != 405:
        url_result['POST'] = status_code_post
    status_code_delete = requests.delete(url).status_code
    if status_code_delete != 405:
        url_result['DELETE'] = status_code_delete
    status_code_options = requests.options(url).status_code
    if status_code_options != 405:
        url_result['OPTIONS'] = status_code_options
    status_code_trace = requests.options(url).status_code
    if status_code_trace != 405:
        url_result['TRACE'] = status_code_trace
    return url_result


def validate(string: str):
    if validators.url(string):
        return check_methods(string)
    return f'Строка "{string}" не является ссылкой'


def main(path: str):
    with open(path) as file:
        line = file.readline().rstrip('\n')
        result = {}
        while line:
            result[line] = validate(line)
            line = file.readline().rstrip('\n')
        pprint(result)
        return result


if __name__ == '__main__':
    main('urls.txt')
