import multiprocessing

# bind
bind = "0.0.0.0:8000"

workers = multiprocessing.cpu_count() * 2 + 1
reload_engine = "inotify"
# group = "dockeruser"
# user = "dockeruser"
reload = True

# logs
loglevel = "debug"
accesslog = "logs/gunicorn/jgpnr.access"
errorlog = "logs/gunicorn/jgpnr.error"