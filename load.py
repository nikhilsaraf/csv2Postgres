import sys
import pandas as pd
from sqlalchemy import create_engine

dbname = sys.argv[1]
print 'dbname:', dbname

filename = sys.argv[2]
print 'filename:', filename

tablename = sys.argv[3]
#postgres doesn't like capitals or spaces
tablename = tablename.lower()
print 'tablename:', tablename

# the logic below has been taken from this stack overflow post: http://stackoverflow.com/a/29722393/1484710
df = pd.read_csv(filename)
#postgres doesn't like capitals or spaces
df.columns = [c.lower() for c in df.columns]

engine = create_engine('postgresql://localhost:5432/' + dbname)
df.to_sql(tablename, engine)
