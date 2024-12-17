import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(r'C:\Users\Евгений\Documents\GitHub\SpiderMatplotlib\divan_scraper\divan_scraper\spiders\output.csv')
df = pd.DataFrame(data)
print(df.head())
#print(df.describe())
#print(df.info())

# Удаляем пробелы и преобразуем в int

df['price'] = df['price'].str.replace(' ', '').astype(int)
#print(df.info()) проверка преобразования типа

mean_price = df['price'].mean()
print(f'Средняя стоимость - {mean_price}')

#гистограмма цен
plt.hist(df['price'], bins=8)
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Количество позиций')
plt.show()