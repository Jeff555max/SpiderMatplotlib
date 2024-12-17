### 1. Парсинг цен диванов с сайта divan.ru с построением гистограммы цен
 В папке divan_scraper находится паук файл Spyder.py

 Для сохранения результата парсинга в файл Excel  устанавливаем 

### pip install pandas

выполняем команды в терминале 

###  .venv\Scripts\activate

###  pip install openpyxl  

заходим в папку с пауком 
### cd (Указываем полный путь) \SpiderMatplotlib\divan_scraper\divan_scraper\spiders
 и выполняем команду
### scrapy crawl divan_scraper -o output.csv (где divan_scraper название папки с проектом)
Результаты парсинга сохранятся в файле формата CSV (output.csv) и XLSX (divan_data.xlsx)

Сохраняем данные в Excel после завершения работы паука

 def closed(self, reason):

        df = pd.DataFrame(self.data)
        df.to_excel('divan_data.xlsx', index=False)

### 2. Обрабатываем данные, находим среднюю цену и выводим ее
Используем библиотеки Matplotlib и Pandas 

import matplotlib.pyplot as plt

import pandas as pd

Строим гистограмму цен, для этого можно использовать output.csv или divan_data.xlsx

1. В файле CleanedPrices.csv.py используем данные из CSV файла (output.csv)
2. В файле CleanedPrisesExcel.py используем данные из Excel файла (divan_data.xlsx)

Результат видим в файле "Гистограмма цен.JPG"

