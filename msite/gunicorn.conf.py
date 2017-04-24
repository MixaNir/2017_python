import multiprocessing
import os

bind = "localhost:8020"
name='pestyle'
workers = multiprocessing.cpu_count() * 2 + 1
max_requests = 1000
errorlog   = os.path.dirname(os.path.abspath(__file__))+"/log/gunicorn.log"
