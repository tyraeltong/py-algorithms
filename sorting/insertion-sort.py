from sorting.utils import print_data


class InsertionSort:
    @staticmethod
    def sort(data):
        if data is None:
            raise TypeError("data should not be None.")

        if len(data) < 2:
            return data

        for i in range(1, len(data)):
            for j in range(i):
                if data[j] < data[i]:
                    data[j], data[i] = data[i], data[j]

        return data


if __name__ == '__main__':
    print_data(InsertionSort)