# Fire webapp

The idea of this web application is to show users the fires that are going on given a location. By default shows user location first.
It is possible to change the dataset and shows information about more locals. The web application is ready for this.

It also provides warnings and the ability for a user to report a fire that is not yet in the information displayed. Thus, it is possible to update the information and prevent many accidents.

## Requirements

- Python 3.7.4

- Django 2.2.5

    1. `pip install Django==2.2.5`
- lxml 4.4.1

    1. `pip install lxml==4.4.1`

 **OR**

- pip and pipenv

    1. `sudo apt install python3-pip python3-dev`
    2. `pip3 install --user pipenv`
    3. Add pipenv (and other python scripts) to PATH: `echo "PATH=$HOME/.local/bin:$PATH" >> ~/.bashrc source ~/.bashrc`


# Setup(Windows)
- Abrir o projeto, pasta "webapp" no pycharm
- Abrir o ficheiro requirements.txt no pycharm e instalar o plugin requirements.txt
- Extrair db.zip para a pasta "C:\Programas (x86)\BaseX\data"
- Correr, pelo menu iniciar, o programa "BaseX HTTP Server (Start)"
- correr no pycharm, clicando no botão "Unnamed (1)" em alternative pode-se executar pelo terminal do pycharm o comando "python3 manage.py runserver"
- abrir o browser no endereço "http://127.0.0.1:8000/"

# Setup(Linux)
## Instalar dependências python
- No diretório base instalar as dependências descritas no ficheiro com o seguinte comando, sem aspas:
- "pip3 install --user -r requirements.txt" ou "pip3 install pipenv; pipenv sync"

## Execução do Basex server
- copiar a bd para a pasta "$HOME/basex/data" do basex
- executar o BasexServer, se instalado, senão então correr o seguinte comando no diretório do projecto 'java -cp BaseX924.jar org.basex.BaseXServer'

## Execução do projecto
- executar o comando "python3 manage.py runserver" no diretório base do projeto


# Nota dataset
- O dataset original "anpc-2018.csv" foi convertido através da ferramenta csv2html que deu origem ao "import.html"

# Nota xslt
- caso queira executar o "import_incidentes.xslt" para converter o "import.html" em xml localizado no diretório "app/xml" necessita do saxon
- após ter o saxon instalado basta corre-lo com "saxon -s:sources/import.html -xsl:import_incidentes.xslt -o:../../db.xml"


## Authors

* **Catarina Silva** - [catarinaacsilva](https://github.com/catarinaacsilva)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
