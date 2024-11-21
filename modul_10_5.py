from multiprocessing import Pool
import threading
import time
import os

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            lines = file.readline()
            all_data.append(lines)
            if not lines:
                break


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start_time = time.time()
    for name in filenames:
        read_info(name)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(elapsed_time, '(линейный)')

    start_time = time.time()
    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)
        end_time = time.time()
        elapsed_time = end_time - start_time
    print(elapsed_time, '(многопроцессный)')





