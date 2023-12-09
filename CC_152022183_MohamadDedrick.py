# Menggunakan library pandas
import pandas as pd

# Variabel Data
data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

# Membuat sebuah dataframe dari dictionary data
df = pd.DataFrame(data)

# No 1
# Menambahkan 5% ke nilai kolom 'Gaji'
df['Gaji']= df['Gaji'].apply(lambda x: x * 1.05)

# No 2
# Menunjukan DataFrame setelah modifikasi yang pertama
print("DataFrame setelah 1st modification:")
print(df)

# No 3
# Menambahkan 2% tambahan ke nilai kolom 'Gaji' untuk individu dengan 'Usia' lebih dari 30
df['Gaji'] = df.apply(lambda row: row['Gaji'] * 1.02 if row['Usia'] > 30 else row['Gaji'], axis=1)

# No 4
# Menunjukan DataFrame setelah modifikasi yang kedua
print("DataFrame setelah 2nd modification:")
print(df)

Nama = "Mohamad Dedrick Finnegan"
NRP = 152022183
Kelas = "CC"