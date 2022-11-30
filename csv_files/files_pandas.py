import pandas as pd

df = pd.read_csv(r'C:\Users\HP\Downloads\data (1).csv')

# print(df.head())


df2=pd.read_csv(r'C:\Users\HP\Downloads\currency.csv')
# print(df2.head())

frames=[df,df2]
res=pd.concat(frames)
print(res)

rslt_df = res.sort_values(by = ['Duration','Pulse'])
print(rslt_df)