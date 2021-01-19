import pandas as pd 
from datetime import date , timedelta
import os 
today = date.today()
yesterday = today - timedelta(days = 2) 

yesterday= yesterday.strftime("%d-%b-%y")

print(type(yesterday))
def data():
    global df 
    destination = os.getcwd() + '/main/.resources/data.csv'
    df = pd.read_csv(destination)
    #print(df)
    colmuns = ['Post to name','Item title','Post to address 1','Post to address 2','Post to city','Post to county','Post to postcode','Quantity','Post to country','Sale date']
    return df[colmuns].T

def filter_(date=today):
    query = data()
    for i in range(len(query.columns)):
        if date != (query[i]['Sale date']):
           query = query.drop(i,1) 
    return query
print(filter_(yesterday))
output=filter_(date=yesterday)
output.t