
import pandas as pd
import pandasql as ps
import numpy
import datetime
from matplotlib import pyplot as plt

'''
rating - MEAN
preço - MEAN

• Pelo menos 2 consultas roll-up ou drill-down.
• Pelo menos 1 consulta slice and dice, podendo ser apenas slice, apenas dice
ou slice and dice.
• Pelo menos 1 consulta pivot.
• Pelo menos 1 consulta drill-across
'''

datasets = [
    "./365k_appstore.csv",
    "./Google-Playstore.csv",
    ]

dados_iOS = pd.read_csv(datasets[0], nrows=100000)
dados_Android = pd.read_csv(datasets[1], nrows=100000)

dados_iOS.dropna(inplace=True)
dados_Android.dropna(inplace=True)

print(list(dados_Android.columns))
print("")
print(list(dados_iOS.columns))
print("")

dados_Android.columns = ['App_Name',
 'App_Id',
 'Category',
 'Rating',
 'Rating_Count',
 'Installs',
 'Minimum_Installs',
 'Maximum_Installs',
 'Free',
 'Price',
 'Currency',
 'Size',
 'Minimum_Android',
 'Developer_Id',
 'Developer_Website',
 'Developer_Email',
 'Released',
 'Last_Updated',
 'Content_Rating',
 'Privacy_Policy',
 'Ad_Supported',
 'In_App_Purchases',
 'Editors_Choice',
 'Scraped_Time']


''' Android '''
query = "SELECT * \
        FROM dados_Android \
        WHERE Currency = 'USD' "
android_facts = ps.sqldf(query)

print(f"Android Facts/Total:{android_facts.size/dados_Android.size}")

query = "SELECT * \
        FROM dados_Android \
        WHERE Currency = 'USD' "
android_facts = ps.sqldf(query)
#android_facts.to_csv("./android_facts.csv")

query = "SELECT App_Id, Price, Rating, Rating_Count \
        FROM android_facts "
android_facts = ps.sqldf(query)
android_facts.to_csv("./android_facts.csv")


query = "SELECT App_Id, Category, Minimum_Android \
        FROM dados_Android "
android_dim = ps.sqldf(query)
android_dim.to_csv("./android_dim.csv")


''' iOS '''
query = "SELECT * \
        FROM dados_iOS \
        WHERE price_currency = 'USD' "
iOS_facts = ps.sqldf(query)

query = "SELECT id AS 'App_Id', price_raw AS 'Price', ratings_avg AS 'Rating', ratings_total AS 'Rating_Count' \
        FROM dados_iOS "
iOS_facts = ps.sqldf(query)
iOS_facts.to_csv("./iOS_facts.csv")

query = "SELECT id AS 'App_Id', category AS 'Category', minimumOsVersion AS 'Minimum_iOS' \
        FROM dados_iOS "
iOS_dim = ps.sqldf(query)
iOS_dim.to_csv("./iOS_dim.csv")

''' Link Table '''
query = "CREATE TABLE link_dim ( \
    uniqueID int, \
    FK varchar(255), \
    Free bit, \
); "
link_dim = pd.DataFrame(columns = ['UniqueKey', 'Android_Or_iOS', 'Free'])
#link_dim = ps.sqldf(query)
link_dim.to_csv("./link_dim.csv")
