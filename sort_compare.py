import random
import datetime
import statistics


def main(size):
    l_size = []
    t_ins_sort = []
    t_shell_sort = []
    t_py_sort = []

    for k in range(100):  # loop for 100 diff lists
        l = []
        for i in range(size):  # loop for the size
            n = random.randint(0, 99)  # get random numbers
            l.append(n)  # add to list
        l_size.append(l)

    for j in l_size:
        t_ins_sort.append(insertion_sort(j))
        t_shell_sort.append(shell_sort(j))
        t_py_sort.append(python_sort(j))

    return [statistics.mean(t_ins_sort), statistics.mean(t_shell_sort), statistics.mean(t_py_sort)]


def insertion_sort(a_list):
    start_time = datetime.datetime.now()

    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value

    end_time = datetime.datetime.now()
    time_diff = end_time - start_time
    return time_diff.microseconds / 1000000


def shell_sort(alist):
    start_time = datetime.datetime.now()

    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for start_position in range(sublistcount):
            gap_InsertionSort(alist, start_position, sublistcount)
        sublistcount = sublistcount // 2

    end_time = datetime.datetime.now()
    time_diff = end_time - start_time
    return time_diff.microseconds / 1000000


def gap_InsertionSort(nlist, start, gap):
    for i in range(start + gap, len(nlist), gap):
        current_value = nlist[i]
        position = i

        while position >= gap and nlist[position - gap] > current_value:
            nlist[position] = nlist[position - gap]
            position = position - gap

        nlist[position] = current_value


def python_sort(alist):
    start_time = datetime.datetime.now()

    alist.sort()

    end_time = datetime.datetime.now()
    time_diff = end_time - start_time
    return time_diff.microseconds / 1000000


res_500 = main(500)
res_1000 = main(1000)
res_10000 = main(10000)
print("Insertion sort took {} seconds on average for list size of {}.".format(res_500[0], 500))
print("Insertion sort took {} seconds on average for list size of {}.".format(res_1000[0], 1000))
print("Insertion sort took {} seconds on average for list size of {}.".format(res_10000[0], 10000))

print("Shell sort Search took {} seconds on average for list size of {}.".format(res_500[1], 500))
print("Shell sort Search took {} seconds on average for list size of {}.".format(res_1000[1], 1000))
print("Shell sort Search took {} seconds on average for list size of {}.".format(res_10000[1], 10000))

print("Python sort Search took {} seconds on average for list size of {}.".format(res_500[2], 500))
print("Python sort Search took {} seconds on average for list size of {}.".format(res_1000[2], 1000))
print("Python sort Search took {} seconds on average for list size of {}.".format(res_10000[2], 10000))
