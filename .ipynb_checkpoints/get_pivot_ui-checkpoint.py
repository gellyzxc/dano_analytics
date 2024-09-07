import pandas as pd
from pivottablejs import pivot_ui
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')


a = ['Уникальный номер выпущенного полиса', 'Сумма премии выпущенного полиса ','Покрытие полиса', 'Выбранный ремонт по полису', 'Флаг оплаты полиса', 'Регион использования авто', 'Марка авто', 'Модель авто', 'Цена авто', 'Пробег авто', 'Флаг нового авто', 'Количество убытков за предыдущие периоды', 'Сумма убытков за предыдущие периоды', 'Год выпуска авто', 'Флаг кредитного авто', 'Стаж вождения', 'Пол водителя', 'Возраст водителя', 'Флаг выпуски полиса', 'Сумма предполагаемого убытка по полису', 'Флаг наличия предыдущего полиса другой страховой', 'Стоимость предыдущего полиса страховой', 'Флаг выпуска пролонгации', 'Флаг оплаты пролонгации'    ]
df.drop(columns=df.columns[0], axis= 1, inplace= True)


df.columns = a

df_dedup = df.sort_values('Сумма предполагаемого убытка по полису', ascending=False) \
             .drop_duplicates(subset=['Уникальный номер выпущенного полиса', 'Пол водителя', 'Возраст водителя'], keep='first')

df_dedup = df_dedup.sort_values('Стаж вождения', ascending=False) \
                   .drop_duplicates(subset=['Уникальный номер выпущенного полиса', 'Пол водителя', 'Возраст водителя'], keep='first')


# df = df.drop_duplicates(subset=['insurant_gender_cd', 'age', 'policy_rk'])
# df = df.drop_duplicates(subset=['min_driver_experience_years_cnt', 'expected_loss_amt'])


df_dedup = df_dedup.dropna(subset=['Возраст водителя'], axis='rows')

plt.figure()
df_dedup.plot(kind='bar',x='Флаг оплаты полиса',y='Уникальный номер выпущенного полиса')


# pt = pivot_ui(df=df_dedup)
# df_dedup.to_csv('deduplicated_dataset.csv', index=False)
