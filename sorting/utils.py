def print_tests(sorting):
    _print([], sorting.sort([]))
    _print([1], sorting.sort([1]))
    _print([2, 1], sorting.sort([2, 1]))
    d = [i for i in range(11, -1, -1)]
    _print(d, sorting.sort(d.copy()))
    d = [i for i in reversed(range(-20, 10))]
    _print(d, sorting.sort(d.copy()))


def _print(data, result):
    print('data to sort:')
    print('\t', data)
    print('data sorted:')
    print('\t', result)