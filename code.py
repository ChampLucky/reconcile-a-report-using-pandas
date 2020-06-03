# --------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Code starts here
df=pd.read_csv(path)
df['state']=df.state.apply(lambda x:x.lower())
df['total']=df['Jan']+df['Feb']+df['Mar']


sum_row={"Jan":sum(df.Jan),"Feb":sum(df.Feb),"Mar":sum(df.Mar),"total":sum(df.total)}

df_final=df.append(sum_row,ignore_index=True)
# Code ends here


# --------------
import requests

# Code starts here

url="https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations"

response=requests.get(url)

df1=pd.read_html(response.content)[0]
# print(df1)
df1=df1.iloc[11:,:]

df1=df1.rename(columns=df1.iloc[0,:]).iloc[1:,:]

df1['United States of America']=df1['United States of America'].apply(lambda x:x.replace(" ","")).astype(object)




# --------------
df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)

# Code starts here


# mapping=df1.set_index('United States of America')['US'].to_dict()

kap=dict(zip(df1['United States of America'],df1['US']))
# print(kap)

df_final['abbr']=df_final['state'].map(kap)
print(df_final)

# Code ends here


# --------------

df_mississipi = df_final[df_final['state'] == 'mississipi'].replace(np.nan, 'MS')

df_tenessee = df_final[df_final['state'] == 'tenessee'].replace(np.nan, 'TN')

print(df_mississipi)
print(df_tenessee)
# replace the final_df
df_final.replace(df_final.iloc[6], df_mississipi, inplace=True)
df_final.replace(df_final.iloc[10], df_tenessee, inplace=True)




# --------------
# Code starts here


df_sub=df_final.groupby('abbr')[['Jan','Feb','Mar','total']].sum()


formatted_df=df_sub.applymap(lambda x:"${:,.0f}".format(x))

print(formatted_df)


# Code ends here


# --------------
# Code starts here



sum_row = df[["Jan", "Feb", "Mar", "total"]].sum()

# sum_row=sum_row.applymap(lambda x: "${:,.0f}".format(x))
df_sub_sum=sum_row.transpose()

df_sub_sum=df_sub_sum.map(lambda x:"${:,.0f}".format(x))
# print(type(df_sub_sum))
final_table=formatted_df.append(df_sub_sum,ignore_index=True)

final_table.rename({final_table.index[-1]: 'Total'}, inplace=True)
print(final_table)

# Code ends here


# --------------
# Code starts here
df_sub['total']=df_sub['Jan']+df_sub['Feb']+df_sub['Mar']
print(df_sub)

plt.pie(df_sub['total'])
plt.show()

# Code ends here


