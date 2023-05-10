import pandas as pd
from collections import Counter
from sklearn import preprocessing



df = pd.read_excel(r'C:\Users\ilyx\Desktop\REVIEW-main\rewiewDOP.xlsx')
df1 = pd.read_excel(r'C:\Users\ilyx\Desktop\REVIEW-main\rewiew.xlsx')
print(len(df))
df = df[df['Rating'] != 5]
dfI = pd.concat([df1, df])
dfI.to_excel(r'C:\Users\ilyx\Desktop\reviewITOG.xlsx', index=False)
