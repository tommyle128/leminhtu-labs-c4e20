from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)
db = client.get_default_database()

new_post = {
    'title': 'In The End',
    'author': 'Tu Le',
    'content': '''It starts with one thing
                I don't know why
                It doesn't even matter how hard you try
                Keep that in mind
                I designed this rhyme
                To explain in due time
                All I know
                Time is a valuable thing
                Watch it fly by as the pendulum swings
                Watch it count down to the end of the day
                The clock ticks life away'''
}

db['posts'].insert_one(new_post)