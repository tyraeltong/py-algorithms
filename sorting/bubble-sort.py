from sorting.utils import print_tests


class BubbleSort:
    """
    Time complexity:
        - worst case: O(nˆ2)
        - best case: O(n)
        - average case: O(nˆ2)
    Space complexity:
        - O(1)
    """
    @staticmethod
    def sort(data):
        if data is None:
            raise TypeError("data should not be None.")

        if len(data) < 2:
            return data

        for end in range(len(data) - 1, -1, -1):
            for i in range(end):
                if data[i] > data[i+1]:
                    data[i+1], data[i] = data[i], data[i+1]

        return data


if __name__ == "__main__":
    print_tests(BubbleSort)