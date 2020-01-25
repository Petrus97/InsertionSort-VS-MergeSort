import pandas as pd
import matplotlib.pyplot as plt
import sort_performance as sp


def test_sorted():
    df = pd.DataFrame(columns=['Size', 'MergeSort', 'InsertionSort'])
    df['Size'] = [100, 500, 1000, 2500, 5000, 10000, 25000]
    merge_time = sp.mergesort_performance_sorted(df['Size'])
    df['MergeSort'] = merge_time
    ins_time = sp.insertionsort_performance_sorted(df['Size'])
    df['InsertionSort'] = ins_time
    print(df)
    plt.xlabel("Array dimension")
    plt.ylabel("Time to sorting")
    plt.plot(df['Size'], merge_time, marker="o")
    plt.plot(df['Size'], ins_time, marker="o")
    plt.legend(['mergesort', 'insertionsort'], loc='upper left')
    plt.title("Sorted Array")
    plt.suptitle("InsertionSort vs MergeSort")
    plt.savefig('figures/sorted.png')
    plt.clf()


def test_random():
    df = pd.DataFrame(columns=['Size', 'MergeSort', 'InsertionSort'])
    df['Size'] = [100, 500, 1000, 2500, 5000, 10000, 25000]
    merge_time = sp.mergesort_performance_random(df['Size'])
    df['MergeSort'] = merge_time
    ins_time = sp.insertionsort_performance_random(df['Size'])
    df['InsertionSort'] = ins_time
    print(df)
    plt.xlabel("Array dimension")
    plt.ylabel("Time to sorting(ms)")
    plt.plot(df['Size'], merge_time, marker="o")
    plt.plot(df['Size'], ins_time, marker="o")
    plt.legend(['mergesort', 'insertionsort'], loc='upper left')
    plt.title("Random Array")
    plt.suptitle("InsertionSort vs MergeSort")
    plt.savefig('figures/random.png')
    plt.clf()


def test_reverse():
    df = pd.DataFrame(columns=['Size', 'MergeSort', 'InsertionSort'])
    df['Size'] = [100, 500, 1000, 2500, 5000, 10000, 25000]
    merge_time = sp.mergesort_performance_reverse(df['Size'])
    df['MergeSort'] = merge_time
    ins_time = sp.insertionsort_performance_reverse(df['Size'])
    df['InsertionSort'] = ins_time
    print(df)
    plt.xlabel("Array dimension")
    plt.ylabel("Time to sorting(ms)")
    plt.plot(df['Size'], merge_time, marker="o")
    plt.plot(df['Size'], ins_time, marker="o")
    plt.legend(['mergesort', 'insertionsort'], loc='upper left')
    plt.title("Reverse Array")
    plt.suptitle("InsertionSort vs MergeSort")
    plt.savefig('figures/reverse.png')
    plt.clf()


def test_all():
    print("SORTED")
    test_sorted()
    print("RANDOM")
    test_random()
    print("REVERSE")
    test_reverse()
