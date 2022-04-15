# X-Statistics
Скрипт для построения интервального распределения частот по выборочным данным.
## How to use
```
python3 main.py
```
Вводим данные через пробел без запятых.
Открываем table.csv, убрав из сепараторов запятую и строим графики ручками.
В файле table.csv будут результаты вычислений в виде таблиц:
1) таблица с интервальным распределением частот
2) таблица с числовыми характеристиками выборки          (Numerical estimates)
3) таблица с эмперической функцией распределения F*(x)   (Function F*(x))
4) таблица для построения графика F*(x)                  (Function F*(x) graph)
5) таблица для построения гистограммы частот             (Histogram of relative frequencies)
## Graphs
(актуально для LibreOffice Calc)
### Эмперическая функция распределения F*(x)
1) выделяем нужные ячейки, включая первый столбец и тыкаем кнопочку Insert Chart
2) Chart Type: XY(Scatter); Lines Only; Line type = Stepped; Properties = Start with horizontal line
3) Data Range: Data series in rows; First column as label 
4) в Chart Elements добавляем название графика, осей и тд
### Гистограмма частот
1) выделяем нужные ячейки, включая первый столбец и тыкаем кнопочку Insert Chart
2) Chart Type: Column; Normal
3) Data Range: Data series in rows; First row as label; First column as label
4) в Chart Elements добавляем название графика, осей и тд
