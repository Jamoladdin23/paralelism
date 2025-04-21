import multiprocessing


def count_even_numbers(numbers, result_queue):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    result_queue.put(count)


def split_list_into_two_parts(lst):
    split_index = len(lst) // 2
    return lst[:split_index], lst[split_index:]


if __name__ == "__main__":
    numbers = [i for i in range(1, 40)]

    part1, part2 = split_list_into_two_parts(numbers)

    result_queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=count_even_numbers, args=(part1, result_queue))
    p2 = multiprocessing.Process(target=count_even_numbers, args=(part2, result_queue))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    count1 = result_queue.get()
    count2 = result_queue.get()

    total_count = count1 + count2
    print("Total count of even numbers:", total_count)
    print(f"In count-1: {count1} | In count-2: {count2}")
