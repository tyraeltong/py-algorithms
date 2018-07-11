from sorting.utils import print_data


class CountingSort:
    """
    Time complexity:
        - worst case: O(n+k)
        - best case: O(n+k)
        - average case: O(n+k)
    Space complexity:
        - worst case: O(k)
    """
    @staticmethod
    def sort(data) -> list:
        if data is None:
            raise TypeError("data should not be None.")

        if len(data) < 2:
            return data

        # find out the max number in data
        max_num = max(data)
        aux = [0] * (max_num + 1)

        for i in range(len(data)):
            aux_idx = data[i]
            aux[aux_idx] += 1

        k = 0
        for j in range(len(aux)):
            if aux[j] > 0:
                for _ in range(aux[j]):
                    data[k] = j
                    k += 1

        return data


if __name__ == '__main__':
    print_data(CountingSort)