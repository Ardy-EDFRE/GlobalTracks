# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 13:41:56 2020

@author: ardyb
"""

import os
import topsongs_daily
import ranking_system
# import create_db
# import get_song_info

path = os.getcwd()
data_path = os.path.join(path, r'TestData')

# topsongs_daily.DataPull(path)
# print('Finished spotify data pull')

ranking_system.SongRankings(data_path)
print('Finished ranking songs')

# create_db.CreateDB(data_path)
# print('Finished creating database')
