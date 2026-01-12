import pandas as pd

# Загрузите набор данных из CSV-файла в DataFrame.
# Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
# Выведите информацию о данных (.info()) и статистическое описание (.describe()).

df = pd.read_csv('World-happiness-report-2024.csv')

# Вывод первых 5 строк
print(df.head())

# Информация о данных
print(df.info)

# Статическое описание
print(df.describe())