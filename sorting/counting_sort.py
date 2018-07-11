from sorting.utils import print_tests


class CountingSort:
    """
    Time complexity:
        - worst case: O(n+k)
        - best case: O(n+k)
        - average case: O(n+k)
    Space complexity:
        - worst case: O(k)

    Ideal usage scenario:
        - data is made up of integers or can be mapped to integers
        - the range of the data is known
        - most of the data in the range are presented
        - additional memory usage is not an issue
    """
    @staticmethod
    def sort(data) -> list:
        if data is None:
            raise TypeError("data should not be None.")

        if len(data) < 2:
            return data

        # find out the max number in data
        max_num = max(data)
        min_num = min(data)
        aux = [0] * (max_num - min_num + 1)

        for i in range(len(data)):
            aux_idx = data[i] - min_num
            aux[aux_idx] += 1

        k = 0
        for j in range(len(aux)):
            if aux[j] > 0:
                for _ in range(aux[j]):
                    data[k] = j + min_num
                    k += 1

        return data


if __name__ == '__main__':
    print_tests(CountingSort)