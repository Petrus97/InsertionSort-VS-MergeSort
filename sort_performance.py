import array_generator as ag
import time
import merge_sort
import insertion_sort
import pickle

# RANDOM


def mergesort_performance_random(dim):
    array_length = dim
    elapsed = []
    Array = []
    m_elapsed = []
    for element in array_length:
        for i in range(1, 10):
            with open("db/random_array.txt", "rb") as openfile:
                count = 0
                while count < element:
                    try:
                        Array.append(pickle.load(openfile))
                        count += 1
                    except EOFError:
                        break
            start = time.perf_counter()
            merge_sort.mergesort(Array, 0, len(Array)-1)
            end = time.perf_counter()
            elapsed.append(end-start)
            Array.clear()
        m_elapsed.append(sum(elapsed)/10)
        elapsed.clear()
    return m_elapsed


def insertionsort_performance_random(dim):
    array_length = dim
    elapsed = []
    Array = []
    m_elapsed = []
    for element in array_length:
        for i in range(1, 10):
            with open("db/random_array.txt", "rb") as openfile:
                count = 0
                while count < element:
                    try:
                        Array.append(pickle.load(openfile))
                        count += 1
                    except EOFError:
                        break
            start = time.perf_counter()
            insertion_sort.insertion_sort(Array)
            end = time.perf_counter()
            elapsed.append(end-start)
            Array.clear()
        m_elapsed.append(sum(elapsed)/10)
        elapsed.clear()
    return m_elapsed

# SORTED


def mergesort_performance_sorted(dim):
    array_length = dim
    elapsed = []
    Array = []
    m_elapsed = []
    for element in array_length:
        for i in range(1, 10):
            with open("db/ascending_ordered_array.txt", "rb") as openfile:
                count = 0
                while count < element:
                    try:
                        Array.append(pickle.load(openfile))
                        count += 1
                    except EOFError:
                        break
            start = time.perf_counter()
            merge_sort.mergesort(Array, 0, len(Array)-1)
            end = time.perf_counter()
            elapsed.append(end-start)
            Array.clear()
        m_elapsed.append(sum(elapsed)/10)
        elapsed.clear()
    return m_elapsed


def insertionsort_performance_sorted(dim):
    array_length = dim
    elapsed = []
    Array = []
    m_elapsed = []
    for element in array_length:
        for i in range(1, 10):
            with open("db/ascending_ordered_array.txt", "rb") as openfile:
                count = 0
                while count < element:
                    try:
                        Array.append(pickle.load(openfile))
                        count += 1
                    except EOFError:
                        break
            start = time.perf_counter()
            insertion_sort.insertion_sort(Array)
            end = time.perf_counter()
            elapsed.append(end-start)
            Array.clear()
        m_elapsed.append(sum(elapsed)/10)
        elapsed.clear()
    return m_elapsed

# REVERSE


def mergesort_performance_reverse(dim):
    array_length = dim
    elapsed = []
    Array = []
    m_elapsed = []
    for element in array_length:
        for i in range(1, 10):
            with open("db/descending_ordered_array.txt", "rb") as openfile:
                count = 0
                while count < element:
                    try:
                        Array.append(pickle.load(openfile))
                        count += 1
                    except EOFError:
                        break
            start = time.perf_counter()
            merge_sort.mergesort(Array, 0, len(Array)-1)
            end = time.perf_counter()
            elapsed.append(end-start)
            Array.clear()
        m_elapsed.append(sum(elapsed)/10)
        elapsed.clear()
    return m_elapsed


def insertionsort_performance_reverse(dim):
    array_length = dim
    elapsed = []
    Array = []
    m_elapsed = []
    for element in array_length:
        for i in range(1, 10):
            with open("db/descending_ordered_array.txt", "rb") as openfile:
                count = 0
                while count < element:
                    try:
                        Array.append(pickle.load(openfile))
                        count += 1
                    except EOFError:
                        break
            start = time.perf_counter()
            insertion_sort.insertion_sort(Array)
            end = time.perf_counter()
            elapsed.append(end-start)
            Array.clear()
        m_elapsed.append(sum(elapsed)/10)
        elapsed.clear()
    return m_elapsed
