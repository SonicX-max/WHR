import pandas as pd

file_path = 'World-happiness-report-2024.csv'
df = pd.read_csv(file_path)

print("Первые 5 строк данных:")
print(df.head())

print("\nИнформация о данных:")
df.info()

print("\nСтатистическое описание данных:")
print(df.describe())