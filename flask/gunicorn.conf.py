proc_name = "gunicorn_spleeter"
workers = 4
bind = ['127.0.0.1:5000']
errolog = "/app/spleeter.gunicorn.error"
acesslog = "app/spleeter.gunicorn.access"
loglevel = "debug"
timeout = 300
graceful_timeout = 300

#sudo systemctl start app