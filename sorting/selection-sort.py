from sorting.utils import print_data


class SelectionSort:
    @staticmethod
    def sort(data):
        result = []
        for _ in range(len(data)):
            min_idx = SelectionSort._find_min_idx(data)
            result.append(data.pop(min_idx))
        return result

    @staticmethod
    def _find_min_idx(items):
        if len(items) < 1:
            return None

        min_item = items[0]
        min_idx = 0

        for idx in range(1, len(items)):
            if items[idx] < min_item:
                min_item = items[idx]
                min_idx = idx

        return min_idx


if __name__ == '__main__':
    print_data(SelectionSort)