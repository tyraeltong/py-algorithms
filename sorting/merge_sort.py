from sorting.utils import print_tests


class MergeSort:
    """
    Time complexity:
        - Worst case: O(nlogn)
        - Best case: O(nlogn)
        - Average case: O(nlogn)
    Space complexity:
        - O(n)
    """
    @staticmethod
    def sort(data):
        if data is None:
            raise TypeError("data should not be None.")

        if len(data) < 2:
            return data

        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        MergeSort.sort(left)
        MergeSort.sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1

        return data


if __name__ == '__main__':
    print_tests(MergeSort)