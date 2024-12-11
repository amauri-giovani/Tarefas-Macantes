import os
import re
import threading
import webbrowser


os.system('clear')
print("\nEsse script irá instalar e configurar o Django na última versão dentro do virtualenv.\n")
os.chdir('/home/amauri/python/django')

while True:
    new_folder = input("Nome da pasta a ser criada: ")
    if os.path.exists(new_folder):
      print("Essa pasta já existe. Escolha outra.\n")
    else:
        os.makedirs(new_folder)
        os.chdir('./{}'.format(new_folder))
        break

project = input("Digite o nome do projeto: ")
app = input("Digite o nome da app: ")
print()

def command_shell(command_line):
    py = os.system(command_line)

command_shell('virtualenv -p python3 .venv')
print()
command_shell('.venv/bin/pip install -r /home/amauri/python/django/env_config/requirements.txt')
command_shell('.venv/bin/django-admin startproject {} .'.format(project))
os.chdir('/home/amauri/python/django/{}/{}'.format(new_folder, project))
command_shell('../.venv/bin/python ../manage.py startapp {}'.format(app))
os.mkdir('static templates')


# Configura e cria os arquivos necessários
with open("/home/amauri/python/django/{}/{}/settings.py".format(new_folder, project)) as file:
    readFile = file.read()
    reg_sec_key = re.search("SECRET_KEY = '(.+)'", readFile)
    reg_deb = re.search("DEBUG = (.+)", readFile)

with open("/home/amauri/python/django/{}/{}/settings.py".format(new_folder, project), 'w') as file_w:
    reg = re.sub('import os', 'import os\n'
                              'from decouple import config, Csv\n'
                              'from dj_database_url import parse as dburl\n',
                              readFile)
    reg = re.sub("SECRET_KEY = '.+'", "SECRET_KEY = config('SECRET_KEY')", reg)
    reg = re.sub("DEBUG = .+", "DEBUG = config('DEBUG', default=False, cast=bool)", reg)
    reg = re.sub("ALLOWED_HOSTS = \[\]", "ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=[], cast=Csv())", reg)
    reg = re.sub(".staticfiles',", ".staticfiles',\n    '{}.core',".format(project), reg)
    reg = re.sub("DATABASES.+\n.+\n.+\n.+\n.+}\n}",
                 "default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')\n"
                 "DATABASES = {\n    'default': config('DATABASE_URL', default=default_dburl, cast=dburl),\n}",
                 reg)
    reg = re.sub('en-us', 'pt-br', reg)
    reg = re.sub('UTC', 'America/Sao_Paulo', reg)

    writeFile = file_w.write(reg + "\nSTATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')")

with open("/home/amauri/python/django/{}/.env".format(new_folder), "w") as env_file:

    env_file.write("SECRET_KEY=" + reg_sec_key.group(1) + "\n"
                   "DEBUG=" + reg_deb.group(1) + "\n"
                   "ALLOWED_HOSTS=127.0.0.1, .localhost, .herokuapp.com\n")

with open("/home/amauri/python/django/{}/Procfile".format(new_folder), "w") as proc_file:
    proc_file.write("web: gunicorn {}.wsgi - -log - file -".format(project))

with open("/home/amauri/python/django/{}/runtime.txt".format(new_folder), "w") as run_time:
    run_time.write("python-3.5.2")

command_shell('clear')
print("\nO arquivo settings.py foi modificado.")
print("Foram criados os seguintes arquivos de configuração:\n.env\nruntime.txt\nProcfile")
os.chdir('/home/amauri/python/django/{}'.format(new_folder))
input("\nPressione uma tecla para continuar...")
command_shell('clear')
print("\nAs seguintes dependências foram instaladas:\n")
command_shell('.venv/bin/pip freeze > requirements.txt')
command_shell('.venv/bin/pip freeze | more')
input("\nPressione uma tecla para continuar...")
command_shell('clear')
print("\nA estrutura de pastas é a seguinte:\n")
command_shell('tree | more')
input("\nPressione uma tecla e AGUARDE abrir a página no browser...")

b = webbrowser.get('google-chrome')

threadObj = threading.Thread(b.open_new('http:/127.0.0.1:8000'))
threadObj.start()

threadObj2 = threading.Thread(command_shell('.venv/bin/python manage.py runserver'))
threadObj2.start()
