# python publisher.py "<binding_key1>.<binding_key2>" "<message>"
# python consumer.py "#"
# python consumer.py "<binding_key>.*"
# python consumer.py "*.<binding_key>"
# python consumer.py "<binding_key>.*" "*.<binding_key>"
# python consumer.py "<binding_key>.#"

import pika

def publisher(client, time_of_day, subject, level):
    # Estabelece uma conexão com o servidor RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Criado uma exchange do tipo 'topic_logs' do tipo topic (a mensagem vai para quem tiver um binding key de interesse)
    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

    binding_key = f"{time_of_day}.{subject}.{level}"

    # Cria objeto de mensagem a ser enviado
    message = f" Client {client} wishes to enroll in course {subject}, level {level} and during shift {time_of_day}.\n"
    channel.basic_publish(exchange='topic_logs',
                          routing_key=binding_key,
                          body=message)

    print(f" Publisher send: {client}: {message}, Routing key: {binding_key}\n")

    connection.close()
