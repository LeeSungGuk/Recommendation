# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import redis

from sqlalchemy import create_engine
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy.orm import sessionmaker

server = 'ec2-54-70-249-15.us-west-2.compute.amazonaws.com'
connection_string = 'mysql+mysqldb://root:*********@{}:3306/rec'.format(server)

redis_pool = redis.ConnectionPool(host=server, port=6379)
engine = create_engine(connection_string, pool_recycle=3600, encoding='utf-8')

Session = sessionmaker(bind=engine)
r = redis.Redis(connection_pool= redis_pool)
