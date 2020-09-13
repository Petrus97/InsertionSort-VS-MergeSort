import pandas as pd
import matplotlib.pyplot as plt
import sort_performance as sp

import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


def test_sorted():
    df = pd.DataFrame(columns=['Dimensione array', 'MergeSort', 'InsertionSort'])
    df['Dimensione array'] = [100, 500, 1000, 2500, 5000, 7500, 10000, 15000, 25000, 35000, 50000]
    merge_time = sp.mergesort_performance_sorted(df['Dimensione array'])
    df['MergeSort'] = merge_time
    ins_time = sp.insertionsort_performance_sorted(df['Dimensione array'])
    df['InsertionSort'] = ins_time
    logging.info(df)
    # print(df)
    # plt.xlabel("Array dimension")
    # plt.ylabel("Time to sorting")
    plt.plot(df['Dimensione array'], merge_time, marker="o")
    plt.plot(df['Dimensione array'], ins_time, marker="o")
    plt.legend(['mergesort', 'insertionsort'], loc='upper left')
    plt.title("Array ordinato")
    plt.suptitle("InsertionSort vs MergeSort")
    plt.savefig('figures/sorted.png')
    plt.clf()
    df.to_latex(buf="results/sorted.tex", index=False, column_format='|l|l|l|', bold_rows=True)


def test_random():
    df = pd.DataFrame(columns=['Dimensione array', 'MergeSort', 'InsertionSort'])
    df['Dimensione array'] = [100, 500, 1000, 2500, 5000, 7500, 10000, 15000, 25000, 35000, 50000]
    merge_time = sp.mergesort_performance_random(df['Dimensione array'])
    df['MergeSort'] = merge_time
    ins_time = sp.insertionsort_performance_random(df['Dimensione array'])
    df['InsertionSort'] = ins_time
    print(df)
    # plt.xlabel("Array dimension")
    # plt.ylabel("Time to sorting(ms)")
    plt.plot(df['Dimensione array'], merge_time, marker="o")
    plt.plot(df['Dimensione array'], ins_time, marker="o")
    plt.legend(['mergesort', 'insertionsort'], loc='upper left')
    plt.title("Array randomico")
    plt.suptitle("InsertionSort vs MergeSort")
    plt.savefig('figures/random.png')
    plt.clf()
    df.to_latex("results/random.tex", index=False, column_format='|l|l|l|', bold_rows=True)


def test_reverse():
    df = pd.DataFrame(columns=['Dimensione array', 'MergeSort', 'InsertionSort'])
    df['Dimensione array'] = [100, 500, 1000, 2500, 5000, 7500, 10000, 15000, 25000, 35000, 50000]
    merge_time = sp.mergesort_performance_reverse(df['Dimensione array'])
    df['MergeSort'] = merge_time
    ins_time = sp.insertionsort_performance_reverse(df['Dimensione array'])
    df['InsertionSort'] = ins_time
    print(df)
    # plt.xlabel("Array dimension")
    # plt.ylabel("Time to sorting(ms)")
    plt.plot(df['Dimensione array'], merge_time, marker="o")
    plt.plot(df['Dimensione array'], ins_time, marker="o")
    plt.legend(['mergesort', 'insertionsort'], loc='upper left')
    plt.title("Array ordinato al contrario")
    plt.suptitle("InsertionSort vs MergeSort")
    plt.savefig('figures/reverse.png')
    plt.clf()
    df.to_latex("results/reverse.tex", index=False, column_format='|l|l|l|', bold_rows=True)


def test_all():
    print("SORTED")
    test_sorted()
    print("RANDOM")
    test_random()
    print("REVERSE")
    test_reverse()
