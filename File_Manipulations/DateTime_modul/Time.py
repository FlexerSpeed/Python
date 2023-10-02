import time

start_time = time.time()

print(time.ctime())  # Дата - время на данный момент
# time.sleep(2.5)  # Задаём таймер работы программы

end_time = time.time()
print(end_time - start_time)

# -----------------------
# Замеряем время выполнения кода, программы
star_time = time.time()

my_list = list(range(100000000))
print(my_list[1000])

end_time = time.time()

print(end_time - star_time)
