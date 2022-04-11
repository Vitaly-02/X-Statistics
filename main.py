import csv
import math


def interval_row(data):
    data.sort()
    h = (data[len(data) - 1] - data[0]) / (1 + 3.322 * math.log(20))
    temp_max = data[len(data) - 1]
    # интервалы
    intervals = []
    while temp_max > 0:
        temp_min = temp_max - h
        if temp_min < 0:
            temp_min = 0
        intervals.append((temp_min, temp_max))
        temp_max -= h
    intervals.reverse()
    # подсчет частот
    n_i = [0 for _ in range(len(intervals))]
    counter = 0
    i = 0
    interval_indexes = [x + 1 for x in range(-1, len(intervals) - 1)]
    for num in data:
        if intervals[interval_indexes[i]][0] <= num <= intervals[interval_indexes[i]][1]:
            counter += 1
            n_i[interval_indexes[i]] = counter
        else:
            while intervals[interval_indexes[i]][0] >= num or num > intervals[interval_indexes[i]][1]:
                i += 1
            counter = 1
            n_i[interval_indexes[i]] = counter
    # подсчет w
    w = [n / len(data) for n in n_i]
    # подсчет x[i]
    x = [(num[0] + num[1]) / 2 for num in intervals]
    # подсчет x[i]*n[i] и x[i]^2*n[i]
    x_i_n_i = []
    x2_i_n_i = []
    for i in range(len(x)):
        x_i_n_i.append(x[i] * n_i[i])
        x2_i_n_i.append(x[i] * x[i] * n_i[i])

    # вычисление числовых оценок параметров распределения:
    # выборочная средняя М, дисперсия D и среднее квадратичное отклонение Sigma
    M = 0
    D = 0
    Sigma = 0
    for i in range(len(w)):
        M += x[i] * w[i]
    numerical_estimates = (['M', 'D', 'Sigma'], [M, D, Sigma])

    # запись таблицы в csv файл
    with open('table.csv', mode='w', encoding='utf-8') as file:
        out = csv.writer(file)
        out.writerow(['interval number', 'interval', 'ni', 'w', 'xi', 'xi*ni', 'xi*xi*ni'])
        for i in range(len(intervals)):
            out.writerow([interval_indexes[i], intervals[i], n_i[i], w[i], x_i_n_i[i], x[i], x2_i_n_i[i]])
        out.writerow(numerical_estimates[0])
        out.writerow(numerical_estimates[1])


if __name__ == '__main__':
    data1 = [11, 8, 12, 5, 3, 10, 7, 8, 3, 6, 31, 9, 5, 7, 13, 4, 4, 0, 3, 6]
    interval_row(data1)
