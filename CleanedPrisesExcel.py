import matplotlib.pyplot as plt
import pandas as pd

# Загружаем данные из файла Excel
data = pd.read_excel(r'C:\Users\Евгений\Documents\GitHub\SpiderMatplotlib\divan_scraper\divan_scraper\spiders\divan_data.xlsx')
df = pd.DataFrame(data)
print(df.head())
#print(df.describe())
#print(df.info())

# Удаляем пробелы и преобразуем в int
df['price'] = df['price'].str.replace(' ', '').astype(int)
#print(df.info()) проверка преобразования типа

mean_price = df['price'].mean()
print(f'Средняя стоимость - {mean_price}')

# Гистограмма цен
plt.hist(df['price'], bins=8)
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Количество позиций')
plt.show()
