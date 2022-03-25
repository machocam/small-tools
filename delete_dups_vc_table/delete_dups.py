## This little program is built to clean **punctually** the VC table of our sqlite DB. 
## It is written to be run once only. Following this, the put_into_db.py script needs to be updated to ensure that no new dups are integrated into the DB.
## The origin of the duplicates are changes made by AMAZON variables like : (1) outstanding_quantity, (2) received_quanity, (3) title.

import pandas as pd
import numpy as np
import sqlite3

## I didn't want to upload my whole DB to GH so I moved it out of the git repo. I'm reaching out there with this relative path. 
sqlite_connection = sqlite3.connect('../../save_pandas.db')

## Creation of cursor to navigate the SQLITE DB
cur = sqlite_connection.cursor()

## Create a temp pandas dataframe with all the data in the VC table (glad that it's only 5K rows!)
whole_vc_table = pd.read_sql_query('SELECT * FROM vc;', sqlite_connection)

## Remove duplicates based off of po and external_id. I think that those two columns should remain stable over time. 
whole_vc_table = whole_vc_table.drop_duplicates(subset=['po', 'model_number'])

## This deletes all the values in VC but keeps the table and its schema in the DB.
cur.execute('DELETE FROM vc;')

## Append values of our dataframe to the VC table (which already exists)
whole_vc_table.to_sql('vc', sqlite_connection, if_exists='append', index=False)

## Commit the changes, vacuum the DB and close the connection.
sqlite_connection.commit()
cur.execute('VACUUM;')
sqlite_connection.close()

