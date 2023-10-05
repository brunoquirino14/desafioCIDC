import pandas as pd
url1 = 'https://github.com/brunoquirino14/desafioCIDC/raw/main/SiteList.xlsx'
url2 = 'https://github.com/brunoquirino14/desafioCIDC/raw/main/Results.xlsx'
df_sites = pd.read_excel(url1)
df_results = pd.read_excel(url2)
df = pd.concat([df_sites, df_results])
nova_ordem = ['Site Name',
'Site ID',
'State',
'Equipment',
'Signal (%)',
'Quality (0-10)',
'Mbps']
df = df[nova_ordem]
df.sort_values(by='State')
soma = df[df['Alerts'] == 'yes']
soma
