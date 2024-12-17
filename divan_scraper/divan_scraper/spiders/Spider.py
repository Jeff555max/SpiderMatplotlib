import scrapy
import pandas as pd

class DivanScraperSpider(scrapy.Spider):
    name = "divan_scraper"
    allowed_domains = ["divan.ru"]
    # start_urls - ссылка, c которой начинается парсинг
    start_urls = ["https://www.divan.ru/category/divany"]

    def __init__(self):
        # Инициализация списка для сохранения данных
        self.data = []

    def parse(self, response):
        # Создаём переменную, в которую будет сохраняться информация
        # response.css('div.lsooF') — поиск по тегу. Будет создан целый список
        divans = response.css('div.lsooF')

        # Настраиваем работу с каждым отдельным диваном в списке
        for divan in divans:
            # оператор "yield" помогает обрабатывать одно отдельное действие
            # С его помощью мы можем управлять потоком выполнения,
            # останавливать и возобновлять работу парсера (С другими операторами мы такого делать не можем)

            price = divan.css('div.fxA6s span::text').get()
            exist = divan.css('link[itemprop="availability"]::attr(href)').get() # exist — проверяет, доступен ли товар.

            item = {
                # Создаём словарик названий, используем поиск по div, а внутри div — по тегу span
                'name': divan.css('div.lsooF span::text').get(),
                # Создаём словарик цен, используем поиск по div, а внутри div — по тегу span
                'price': price if exist else '0'
            }
            self.data.append(item)
            yield item

        # Создали новый запрос для перехода на следующую страницу
        # `self.parse` - функция, которая будет вызвана для обработки ответа с новой страницы.
        # Мы повторно вызываем метод `parse`, чтобы извлечь данные с новой страницы точно так же, как и с первой.
        # `yield` возвращает новый запрос в очередь Scrapy. Это асинхронный подход,
        # который позволяет Scrapy эффективно управлять многими запросами параллельно
        # Поиск ссылки на след страницу из атрибута href в теге <a> класс ZIuae
        next_page = response.css('a.ZIuae::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def closed(self, reason):
        # Сохраняем данные в Excel после завершения работы паука
        df = pd.DataFrame(self.data)
        df.to_excel('divan_data.xlsx', index=False)
