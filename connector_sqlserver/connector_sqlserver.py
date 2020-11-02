import json
import urllib
from sqlalchemy import create_engine

# Get access variables from txt
with open('vaccess.txt') as access_file:
    vaccess = json.load(access_file)

# Create connection
params = urllib.parse.quote_plus \
(r'DRIVER='+vaccess['driver']+';SERVER='+vaccess['server']+';PORT=1433;DATABASE='+vaccess['database']+';UID='+vaccess['username']+';PWD='+vaccess['password'])
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
engine_azure = create_engine(conn_str, echo=False, fast_executemany=True)

# With the engine, it's now possible to query the existing tables from your server
print(engine_azure.table_names())

# Close connection
engine_azure.dispose()