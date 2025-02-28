## Para rodar

Utilize o comando no docker:

````
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management

````

<hr>

Crie uma ENV:

````
python -m venv env

````

<hr>

Rode:

````
pip install -r requirements.txt

````

<hr>

Após tudo isso Rode:

````
python consumidor.py

````

<hr>

E:

````
python produtor.py

````