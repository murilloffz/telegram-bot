import sys
sys.path.append('../src')
from src import db_abstractor


conn1 = db_abstractor.DatabaseInterface('TEST')
print(conn1)
# TESTAR