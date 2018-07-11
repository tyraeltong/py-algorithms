from sorting.utils import print_tests


class SelectionSort:
    """
    Time complexity:
        - Worst case: O(nˆ2)
        - Best case: O(nˆ2)
        - Average case: O(nˆ2)
    Space complexity:
        - O(1)
    """
    @staticmethod
    def sort(data):
        if data is None:
            raise TypeError("data should not be None.")

        if len(data) < 2:
            return data

        for i in range(len(data) - 1):
            min_idx = SelectionSort._find_min_idx(data[i:])
            data[i], data[min_idx+i] = data[min_idx+i], data[i]
        return data

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
    print_tests(SelectionSort)