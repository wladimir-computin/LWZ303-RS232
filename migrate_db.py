#!/usr/bin/env python3
import dataset

#with dataset.connect("sqlite:///status_2022_02_old.db", sqlite_wal_mode=False) as old_db:
#	with dataset.connect("sqlite:///log/status_2022_02.db", sqlite_wal_mode=False) as db:
#		print(old_db.tables)
#		for table in old_db.tables:
#			db[table].insert_many(list(old_db[table].all()))
