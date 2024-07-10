import multiprocessing

# Configuration for Gunicorn - avoid memory errors when deploying
bind = f"0.0.0.0:{os.getenv('PORT', '8000')}"  # default to 8000
workers = 3
threads = 2
timeout = 120
max_requests = 1000
max_requests_jitter = 50
