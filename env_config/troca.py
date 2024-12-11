import re


with open("/home/amauri/python/django/testes/teste/settings.py") as file:
    readFile = file.read()
    # a = re.compile("SECRET_KEY\s=\s'.+'")
    reg_sec_key = re.search("SECRET_KEY = '(.+)'", readFile)
    # sec_key = reg_sec_key.group(1)
    reg_deb = re.search("DEBUG = (.+)", readFile)
    # deb = reg_deb.group(1)
    # print(sec_key)
    # print(deb)
    # print(reg_sec_key.group(2))

with open("/home/amauri/python/django/testes/teste/settings.py", 'w') as file_w:
    reg = re.sub('import os', 'import os\n'
                              'from decouple import config, Csv\n'
                              'from dj_database_url import parse as dburl\n',
                              readFile)
    reg = re.sub("SECRET_KEY = '.+'", "SECRET_KEY = config('SECRET_KEY')", reg)
    reg = re.sub("DEBUG = .+", "DEBUG = config('DEBUG', default=False, cast=bool)", reg)
    reg = re.sub("ALLOWED_HOSTS = \[\]", "ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=[], cast=Csv())", reg)
    reg = re.sub(".staticfiles',", ".staticfiles',\n    'teste.core',", reg)
    reg = re.sub("DATABASES.+\n.+\n.+\n.+\n.+}\n}",
                 "default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')\n"
                 "DATABASES = {\n'default': config('DATABASE_URL', default=default_dburl, cast=dburl),\n}",
                 reg)
    reg = re.sub('en-us', 'pt-br', reg)
    reg = re.sub('UTC', 'America/Sao_Paulo', reg)

    writeFile = file_w.write(reg)

with open("/home/amauri/python/django/testes/.env", "w") as env_file:

    env_file.write("SECRET_KEY=" + reg_sec_key.group(1) + "\n"
                   "DEBUG=" + reg_deb.group(1) + "\n"
                   "ALLOWED_HOSTS=127.0.0.1, .localhost, .herokuapp.com\n")

with open("/home/amauri/python/django/testes/Procfile", "w") as proc_file:
    proc_file.write("web: gunicorn {}.wsgi - -log - file -".format("teste"))

with open("/home/amauri/python/django/testes/runtime.txt", "w") as run_time:
    run_time.write("python-3.5.2")
