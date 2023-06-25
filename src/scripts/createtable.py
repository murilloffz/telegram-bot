import sys
sys.path.append('../src')
from src import db_connector

# TO DO colocar dados em uma config.py !!
conn1 = db_connector.DatabaseConnector('localhost', 'admin', 'password', 'MH_STUFF')
print(conn1)
conn1.connect()
print(conn1.connection)
# print(conn1.execute_query(
#     '''CREATE TABLE Professional (
#     ID int NOT NULL,
#     Name varchar(50),
#     Phone varchar(20) NOT NULL,
#     PRIMARY KEY (ID));
#     '''))

print(conn1.execute_query("SHOW TABLES"))
