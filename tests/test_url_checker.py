import pytest

from url_checker import check_methods, main, validate


def test_check_methods():
    assert check_methods('https://habr.com') == {
                                                 'DELETE': 200,
                                                 'GET': 200,
                                                 'OPTIONS': 200,
                                                 'POST': 200,
                                                 'TRACE': 200
                                                }


@pytest.mark.parametrize(
        'data, expected_result',
        [
            ('https://cloudflare.com', {
                'DELETE': 200,
                'GET': 200,
                'OPTIONS': 200,
                'POST': 200,
                'TRACE': 200
                }),
            ('httpyau', 'Строка "httpyau" не является ссылкой'),
        ]
    )
def test_validate(data, expected_result):
    assert validate(data) == expected_result


def test_main():
    assert main('test_urls.txt') == {'http://google.com': {'GET': 200},
                                     'http://voltacom.ru': {
                                                         'DELETE': 200,
                                                         'GET': 200,
                                                         'OPTIONS': 200,
                                                         'POST': 200,
                                                         'TRACE': 200
                                                         },
                                     'httpya.ru': 'Строка "httpya.ru" не '
                                                  'является ссылкой',
                                     'https://stepik.org': {
                                                         'DELETE': 403,
                                                         'GET': 200,
                                                         'OPTIONS': 200,
                                                         'POST': 403,
                                                         'TRACE': 200
                                                         },
                                     'https://wikipedia.com': {'DELETE': 403,
                                                               'GET': 200,
                                                               'OPTIONS': 403,
                                                               'POST': 403,
                                                               'TRACE': 403
                                                               }}
