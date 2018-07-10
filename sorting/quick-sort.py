from sorting.utils import print_data
import random


class QuickSort:
    @staticmethod
    def sort(data):
        if data is None:
            raise TypeError("data should not be None.")

        if len(data) < 2:
            return data

        pivot_idx = random.randint(0, len(data)-1)
        pivot = data[pivot_idx]
        smaller = [i for i in data[:pivot_idx] if i < pivot] + [i for i in data[pivot_idx+1:] if i < pivot]
        greater = [i for i in data[:pivot_idx] if i >= pivot] + [i for i in data[pivot_idx+1:] if i >= pivot]
        return QuickSort.sort(smaller) + [pivot] + QuickSort.sort(greater)


if __name__ == '__main__':
    print_data(QuickSort)