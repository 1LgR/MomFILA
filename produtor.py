# producer.py
import pika

# Conexão com RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar uma fila
channel.queue_declare(queue='guessQueue')

# Enviar mensagem para a fila
message = 'Convidado recebe: 50'
channel.basic_publish(exchange='',
                      routing_key='guessQueue',
                      body=message)

print(f"Mensagem enviada para a fila: {message}")

# Fechar a conexão
connection.close()
