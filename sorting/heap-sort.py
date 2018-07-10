from sorting.utils import print_data


class HeapSort:
    @staticmethod
    def sort(data):
        HeapSort._heapify(data, len(data))
        end = len(data) - 1
        while end > 0:
            data[end], data[0] = data[0], data[end]
            end -= 1
            HeapSort._sift_down(data, 0, end)
        return data

    @staticmethod
    def _heapify(data, count):
        start = (count - 2) // 2
        while start >= 0:
            HeapSort._sift_down(data, start, count-1)
            start -= 1

    @staticmethod
    def _sift_down(data, start, end):
        root = start
        while (root*2 + 1) <= end:
            child = root*2 + 1
            swap = root
            if data[swap] < data[child]:
                swap = child
            if (child+1) <= end and data[swap] < data[child+1]:
                swap = child + 1
            if swap != root:
                data[root], data[swap] = data[swap], data[root]
                root = swap
            else:
                return


if __name__ == '__main__':
    print_data(HeapSort)