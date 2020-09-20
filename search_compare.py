import random
import datetime
import statistics


def main(size):
    l_size = []
    t_seq = []
    t_or_seq = []
    t_bi_it = []
    t_bi_re = []

    for k in range(100):  # loop for 100 diff lists
        l = []
        for i in range(size):  # loop for the size
            n = random.randint(0, 99)  # get random numbers
            l.append(n)  # add to list
        l_size.append(l)

    for j in l_size:
        t_seq.append(sequential_search(j, -1))
        j.sort()
        t_or_seq.append(ordered_sequential_search(j, -1))
        t_bi_it.append(binary_search_iterative(j, -1))
        start_time = datetime.datetime.now()
        end_time = binary_search_recursive(j, -1)
        time_diff = end_time - start_time
        t_bi_re.append(time_diff.microseconds / 1000000)

    return [statistics.mean(t_seq), statistics.mean(t_or_seq), statistics.mean(t_bi_it), statistics.mean(t_bi_re)]


def sequential_search(a_list, item):
    pos = 0
    found = False
    start_time = datetime.datetime.now()

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    end_time = datetime.datetime.now()
    time_diff = end_time - start_time
    return time_diff.microseconds / 1000000


def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False
    start_time = datetime.datetime.now()

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    end_time = datetime.datetime.now()
    time_diff = end_time - start_time
    return time_diff.microseconds / 1000000


def binary_search_iterative(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False
    start_time = datetime.datetime.now()

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end_time = datetime.datetime.now()
    time_diff = end_time - start_time
    return time_diff.microseconds / 1000000


def binary_search_recursive(a_list, item):
    if len(a_list) == 0:
        return datetime.datetime.now()
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)


res_500 = main(500)
res_1000 = main(1000)
res_10000 = main(10000)
print("Sequential Search took {} seconds on average for list size of {}.".format(res_500[0], 500))
print("Sequential Search took {} seconds on average for list size of {}.".format(res_1000[0], 1000))
print("Sequential Search took {} seconds on average for list size of {}.".format(res_10000[0], 10000))

print("Ordered Sequential Search took {} seconds on average for list size of {}.".format(res_500[1], 500))
print("Ordered Sequential Search took {} seconds on average for list size of {}.".format(res_1000[1], 1000))
print("Ordered Sequential Search took {} seconds on average for list size of {}.".format(res_10000[1], 10000))

print("Binary Search Iterative Search took {} seconds on average for list size of {}.".format(res_500[2], 500))
print("Binary Search Iterative Search took {} seconds on average for list size of {}.".format(res_1000[2], 1000))
print("Binary Search Iterative Search took {} seconds on average for list size of {}.".format(res_10000[2], 10000))

print("Binary Search Recursive Search took {} seconds on average for list size of {}.".format(res_500[3], 500))
print("Binary Search Recursive Search took {} seconds on average for list size of {}.".format(res_1000[3], 1000))
print("Binary Search Recursive Search took {} seconds on average for list size of {}.".format(res_10000[3], 10000))
