# import multiprocessing
#
# def count_even_numbers(numbers):
#     even_count = 0
#     for num in numbers:
#         if num % 2 == 0:
#             even_count += 1
#     return even_count
#
# def main():
#     # Создайте список целых чисел (вы можете заменить его своим собственным списком)
#     big_list = [i for i in range(1, 1000000)]
#
#     # Разделите список на две примерно равные части
#     mid = len(big_list) // 2
#     part1 = big_list[:mid]
#     part2 = big_list[mid:]
#
#     # Создайте два отдельных процесса для подсчета четных чисел в каждой части
#     process1 = multiprocessing.Process(target=count_even_numbers, args=(part1,))
#     process2 = multiprocessing.Process(target=count_even_numbers, args=(part2,))
#
#     # Запустите процессы
#     process1.start()
#     process2.start()
#
#     # Дождитесь завершения обоих процессов
#     process1.join()
#     process2.join()
#
#     # Получите результаты из каждого процесса
#     even_count1 = process1.exitcode
#     even_count2 = process2.exitcode
#
#     # Сложите результаты
#     total_even_count = even_count1 + even_count2
#
#     # Выведите общее количество четных чисел
#     print(f"Общее количество четных чисел в списке: {total_even_count}")
#
# if __name__ == "__main__":
#     main()
