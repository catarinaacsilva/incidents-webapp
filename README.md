# Incident webapp

The idea of this web application is to show users the incidents that are going on a given location. By default shows user location first.
It is possible to change the dataset and shows information about more locals or in real time.

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


## Setup(Windows)

- Open the project (webapp folder) on pycharm
- Open requirements.txt on pycharm and install the requirements.txt plugin
- Move db.zip to `C:\Programas (x86)\BaseX\data`
- Run the program `BaseX HTTP Server (Start)`
- Run on pycharm or in terminal: `python3 manage.py runserver`
- Open browser: `http://127.0.0.1:8000/`


## Setup(Linux)

1. **Instalar dependências python**

- Run `pip3 install --user -r requirements.txt" ou "pip3 install pipenv; pipenv sync` to install all dependencies


2. **Execução do Basex server**

- Copy bd to `$HOME/basex/data`
- Run BasexServer. If it is not install run `java -cp BaseX924.jar org.basex.BaseXServer` on project folder.


3. **Execução do projecto**

- Run `python3 manage.py runserver`


## Authors

* **Catarina Silva** - [catarinaacsilva](https://github.com/catarinaacsilva)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
