from sorting.utils import print_data


class CountingSort:
    @staticmethod
    def sort(data) -> list:
        if data is None:
            raise TypeError("data should not be None.")

        if len(data) < 2:
            return data

        votes = [0] * len(data)
        buckets = [0] * len(data)

        for i in range(len(data)):
            for j in range(len(data)):
                if data[i] >= data[j]:
                    votes[i] += 1

        for i in range(len(data)):
            buckets[votes[i]-1] = data[i]

        return buckets


if __name__ == '__main__':
    print_data(CountingSort)