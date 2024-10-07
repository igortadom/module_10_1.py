from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    #
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(1, word_count + 1):
        file.write(f"Какое-то слово № {i} \n")
        sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_stop = datetime.now()
time_res = time_stop - time_start

print(f'Работа потоков {time_res}')

time1_start = datetime.now()


thr_first = Thread(target=write_words, args= (10, 'example5.txt'))
thr_second = Thread(target=write_words, args= (30, 'example6.txt'))
thr_third = Thread(target=write_words, args= (200, 'example7.txt'))
thr_fourth = Thread(target=write_words, args= (100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

time1_stop = datetime.now()
time1_res = time1_stop - time1_start
print(f'Работа потоков {time1_res}')
