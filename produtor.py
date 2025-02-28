# producer.py
import pika

# Conexão com RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar uma fila
channel.queue_declare(queue='guessQueue')

num = 50
cont = 1

# Enviar mensagem para a fila
while(cont < 20):
    message = (f"Convidado recebe: {num}")
    num+=10
    cont+=1
    channel.basic_publish(exchange='',
                        routing_key='guessQueue',
                        body=message)

    print(f"Mensagem enviada para a fila: {message}")

# Fechar a conexão
connection.close()
