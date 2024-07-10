import multiprocessing

# Configuration for Gunicorn - avoid memory errors when deploying
bind = "0.0.0.0:8000"
workers = 2
threads = 2
timeout = 120
max_requests = 1000
max_requests_jitter = 50
