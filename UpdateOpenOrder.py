import pygsheets
import pandas as pd

client = pygsheets.authorize(service_account_file="[account].json")

df = pd.read_excel (r'Open Orders.xls')

spreadsht = client.open("Open Orders - All Locations")

worksht = spreadsht.worksheet("title", "Data")

worksht.set_dataframe(df,(1,1),extend=True)
