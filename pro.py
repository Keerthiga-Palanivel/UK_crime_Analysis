import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r"C:\Users\keerthi\PycharmProjects\UKCRIME\venv\Scripts\rec-crime-pfa.csv")
print(df.head())
print(df.info())
print(df.isnull().any().any())
print(df.nunique())

df['12 months ending'] = pd.to_datetime(df['12 months ending'])
df['Year'] = df['12 months ending'].dt.year
df['Month'] = df['12 months ending'].dt.month
df['Day'] = df['12 months ending'].dt.day
df['Day of week']  = df['12 months ending'].dt.dayofweek
df['Week of Year']  = df['12 months ending'].dt.weekofyear
df = df.rename(columns= {'Rolling year total number of offences' : 'Total Offence'})
print(df.head())
print(df.info())

for col in ['PFA'  ,'Region','Offence' ]:
    print('Unique value {0}:'.format(col))
    print(df[col].unique())
for One in df['Offence'].unique():
    print(One)

df.loc[df['Offence'].isin(['Domestic burglary','Non-residential burglary',
'Residential burglary']),'Offence'] = 'Bulgary'
df.loc[df['Offence'].isin(['All other theft offences','Bicycle theft',
'Shoplifting','Theft from the person']),'Offence'] = 'Theft'
df.loc[df['Offence'].isin(['Violence with injury',
'Violence without injury',]),'Offence'] = 'Violence'

print(df['Offence'])

del(df['12 months ending'])
print(df.head())

#################################################
print('#DATA_VISUALIATION##########')

plt.figure(figsize=(15,6))
ax = sns.barplot(x="Year", y= "Total Offence" , data = df)
plt.xticks(rotation=55, fontsize = 7)


plt.figure(figsize=(15,6))
ax1 = sns.barplot(x="Region", y="Total Offence", data = df)
plt.xticks(rotation=55, fontsize = 7)


df_temp= df[-df['Region'].isin(['Fraud: Action Fraud','Fraud: CIFAS','Fraud: UK Finance'])]
plt.figure(figsize=(15,6))
ax2 = sns.barplot(x="Region", y="Total Offence", data = df_temp)
plt.xticks(rotation =55, fontsize = 7)

df_london = df[df['Region']== 'London']
plt.figure(figsize=(15,6))
ax3 = sns.barplot(x="Offence", y="Total Offence", data = df_london)
plt.xticks(rotation =55, fontsize = 7)


offence_list = list(df_london['Offence'].unique())

g= sns.FacetGrid(df_london, col='Offence', height= 5, col_wrap= 5)
g.map(plt.bar,'Year', 'Total Offence', color= 'Blue')
plt.show()
