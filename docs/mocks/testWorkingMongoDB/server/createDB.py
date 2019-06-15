from pymongo import MongoClient #add dependency
from settings import *
from constants import CONSTANTS
import sys



client = MongoClient(connection_str + '?ssl=true&replicaSet=globaldb')

db = client[CONSTANTS['COSMOS']['COLLECTION']]

db.authenticate(cosmosDB_user, cosmosDB_password)

list_items = db.test

