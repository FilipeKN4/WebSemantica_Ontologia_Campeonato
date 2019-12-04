# Ontologia de Campeonato

Aplicação _Web_ realizada utilizando _Python-Django_ com o objetivo de realizar algumas consultas em uma ontologia
de Campeonato com foco em Campeonato de Futebol de Campo.

## Instalação e Uso

Os passos de instalação a seguir são referentes ao uso da aplicação no Sistema Operacional _Ubuntu_ versão 18.04. Os comando devem ser executados no Terminal.

### Sem Python e Django Previamente Instalados

Passo 1) Instalar o _pip3_ com o seguinte comando:

```sh
$ sudo apt install python3-pip
```
Passo 2) Instalar o _virtualenvwrapper_ utilizando o _pip3_ com o comando a seguir:

```sh
$ sudo pip3 install virtualenvwrapper
```

Em seguida, deve-se adicionar as seguintes linhas no arquivo *.bashrc* na pasta home:

```sh
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS=' -p /usr/bin/python3 '
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```

Deve-se recarregar o arquivo com o comando:

```sh
$ source ~/.bashrc
```

Com o _virtualenvwrapper_ instalado deve-se criar uma máquina virtual e entrar com o comando:

```sh
$ mkvirtualenv my_django_environment
```

Passo 3) Instalar o _Django_ dentro da máquina virtual com o comando:

```sh
$ pip3 install django
```

### Após as Instalações do _Python_ e do _Django_

Passo 1) Clonar o repositório com o comando:

```sh
$ git clone https://github.com/FilipeKN4/WebSemantica_Ontologia_Campeonato.git
```

Passo 2) Dentro da pasta do projeto rodar o comando:

```sh
$ pip3 install -r requirements.txt
```

Passo 3) Dentro da pasta 'ontologia_campeonato' deve-se rodar o projeto com o comando:

```sh
$ python manage.py runserver
```

O projeto será executado localmente em http://localhost:8000/.