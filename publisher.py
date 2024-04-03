# python publisher.py "<binding_key1>.<binding_key2>" "<message>"
# python consumer.py "#"
# python consumer.py "<binding_key>.*"
# python consumer.py "*.<binding_key>"
# python consumer.py "<binding_key>.*" "*.<binding_key>"
# python consumer.py "<binding_key>.#"
# Uber - Carro porte X, bairro Y, Z, A

import pika
import sys

def publisher(client, car_type, origem, destination):
    # Estabelece uma conexão com o servidor RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Criado uma exchange do tipo 'topic_logs' do tipo topic (a mensagem vai para quem tiver um binding key de interesse)
    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

    # Lê a lista de binding keys separada por .
    # routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'

    binding_key = f"{car_type}.{origem}.{destination}"

    # Cria objeto de mensagem a ser enviado
    message = f" Cliente {client} deseja uma corrida da origem: {origem} ao destino {destination}.\n"
    channel.basic_publish(exchange='topic_logs',
                          routing_key=binding_key,
                          body=message)

    print(f" ENVIADO PEDIDO DE CORRIDA: {client}: {message}, Routing key: {binding_key}\n")

    connection.close()
