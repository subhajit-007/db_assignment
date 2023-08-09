import pymongo
import os


class DbConnection:
    # Connect mongodb
    CLIENT = pymongo.MongoClient(os.getenv('MONGODB_URL'))

    # Create or access mongodb database
    TODO_DB = CLIENT['Todo']

    # Create Collection named "tasks"
    task = TODO_DB.tasks


DB_INSTANCE = DbConnection()
