# consumer.py
import pika

# Conexão com RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar a fila (mesma fila usada pelo produtor)
channel.queue_declare(queue='guessQueue')

# Função que será chamada quando uma mensagem for recebida
def callback(ch, method, properties, body):
    print(f"Mensagem recebida: {body.decode()}")

# Consumir as mensagens da fila
channel.basic_consume(queue='guessQueue', on_message_callback=callback, auto_ack=True)

print('Esperando mensagens. Para sair, pressione CTRL+C')
channel.start_consuming()
