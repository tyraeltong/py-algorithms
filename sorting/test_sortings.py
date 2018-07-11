from sorting.bubble_sort import BubbleSort
from sorting.counting_sort import CountingSort
from sorting.heap_sort import HeapSort
from sorting.insertion_sort import InsertionSort
from sorting.merge_sort import MergeSort
from sorting.quick_sort import QuickSort
from sorting.selection_sort import SelectionSort


def test_bubble_sort():
    assert([] == BubbleSort.sort([]))
    assert([1] == BubbleSort.sort([1]))
    assert([1, 2, 3, 4, 5, 6, 7, 8, 9] == BubbleSort.sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert([-9, -8, -7, -6, 0, 1, 2, 3] == BubbleSort.sort([3, 1, 2, -9, -8, 0, -7, -6]))
    assert([-7, -7, 0, 3, 4] == BubbleSort.sort([3, -7, -7, 4, 0]))


def test_counting_sort():
    assert([] == CountingSort.sort([]))
    assert([1] == CountingSort.sort([1]))
    assert([1, 2, 3, 4, 5, 6, 7, 8, 9] == CountingSort.sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert([-9, -8, -7, -6, 0, 1, 2, 3] == CountingSort.sort([3, 1, 2, -9, -8, 0, -7, -6]))
    assert([-7, -7, 0, 3, 4] == CountingSort.sort([3, -7, -7, 4, 0]))


def test_heap_sort():
    assert ([] == HeapSort.sort([]))
    assert ([1] == HeapSort.sort([1]))
    assert ([1, 2, 3, 4, 5, 6, 7, 8, 9] == HeapSort.sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert ([-9, -8, -7, -6, 0, 1, 2, 3] == HeapSort.sort([3, 1, 2, -9, -8, 0, -7, -6]))
    assert ([-7, -7, 0, 3, 4] == HeapSort.sort([3, -7, -7, 4, 0]))


def test_insertion_sort():
    assert ([] == InsertionSort.sort([]))
    assert ([1] == InsertionSort.sort([1]))
    assert ([1, 2, 3, 4, 5, 6, 7, 8, 9] == InsertionSort.sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert ([-9, -8, -7, -6, 0, 1, 2, 3] == InsertionSort.sort([3, 1, 2, -9, -8, 0, -7, -6]))
    assert ([-7, -7, 0, 3, 4] == InsertionSort.sort([3, -7, -7, 4, 0]))


def test_merge_sort():
    assert ([] == MergeSort.sort([]))
    assert ([1] == MergeSort.sort([1]))
    assert ([1, 2, 3, 4, 5, 6, 7, 8, 9] == MergeSort.sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert ([-9, -8, -7, -6, 0, 1, 2, 3] == MergeSort.sort([3, 1, 2, -9, -8, 0, -7, -6]))
    assert ([-7, -7, 0, 3, 4] == MergeSort.sort([3, -7, -7, 4, 0]))


def test_quick_sort():
    assert ([] == QuickSort.sort([]))
    assert ([1] == QuickSort.sort([1]))
    assert ([1, 2, 3, 4, 5, 6, 7, 8, 9] == QuickSort.sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert ([-9, -8, -7, -6, 0, 1, 2, 3] == QuickSort.sort([3, 1, 2, -9, -8, 0, -7, -6]))
    assert ([-7, -7, 0, 3, 4] == QuickSort.sort([3, -7, -7, 4, 0]))


def test_selection_sort():
    assert ([] == SelectionSort.sort([]))
    assert ([1] == SelectionSort.sort([1]))
    assert ([1, 2, 3, 4, 5, 6, 7, 8, 9] == SelectionSort.sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert ([-9, -8, -7, -6, 0, 1, 2, 3] == SelectionSort.sort([3, 1, 2, -9, -8, 0, -7, -6]))
    assert ([-7, -7, 0, 3, 4] == SelectionSort.sort([3, -7, -7, 4, 0]))