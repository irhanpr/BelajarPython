import pandas as pd
csv_path = (r'C:\Users\irhan\OneDrive - grow distributed users\BelajarPython\Dataset\COVID_INDONESIA\cases.csv')
df = pd.read_csv(csv_path)
print(df.head())
print(df.iloc[0,0])

x = df[['acc_tested']] #digunakkan untuk mengambil satu kolom dari seluruh tabel
print(x)

xlsx_path = (r'C:\Users\irhan\OneDrive - grow distributed users\BelajarPython\Dataset\1.1-data-pegawai-dishub-dan-diagram-maret-2020.xls')
df = pd.read_excel(xlsx_path)
print(df.head())

import pandas as pd
songs = {'Artist' :['Michael Jackson','AC/DC', 'Pink Floyd', 'Whitney Houston', 'Meat Loaf', 'Eagles'], 'Album': ['Thriller', 'Back in Black', 'The Dark Side of the Moon','The Bodyguard','Bat Out of Hell', 'Their Greatest Hits (1971-1975)'],
         'Released':[1982, 1980, 1973, 1992, 1977,1976], 'Length': ['00:42:19', '00:42:11', '00:42:49', '00:57:44', '00:46:33','00:43:08']}

songs_frame = pd.DataFrame(songs)
print(songs_frame.head())
x = songs_frame[['Length']] #digunakkan untuk mengambil data dari satu kolom
print(x)
y = songs_frame[['Album','Released']] #digunakkan untuk mengambil data dari multi kolom atau banyak kolom
print(y)
print(songs_frame.iloc[0,0]) #digunakkan untuk memanggil salah satu atribut dari list