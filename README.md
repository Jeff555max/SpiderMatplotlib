### Парсинг цен диванов с сайта divan.ru с построением гистограммы средних цен
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

Для конвертации из формата CSV в Excel используется функция

 def closed(self, reason):

        df = pd.DataFrame(self.data)
        df.to_excel('divan_data.xlsx', index=False)