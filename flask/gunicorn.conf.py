proc_name = "gunicorn"
workers = 4
bind = ['0.0.0.0:5000']
errolog = "/app/spleeter.gunicorn.error"
acesslog = "/app/spleeter.gunicorn.access"
loglevel = "debug"
timeout = 300
graceful_timeout = 300

#sudo systemctl start app