import pika

def consumer(driver_name, car_type, origem, destination):
    # Estabelece uma conexão com o servidor RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Criado uma exchange do tipo 'topic_logs' do tipo topic (a mensagem vai para quem tiver um binding key de interesse)
    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

    # Cria uma fila vazia de nome aleatório, deleta a fila quando a conexão fechar
    result = channel.queue_declare(queue='', exclusive=True)

    queue_name = result.method.queue

    # # Lê do terminal a string passada
    # binding_keys = sys.argv[1:]
    #
    # # Se não for passada nenhuma string, alerta e fecha o programa
    # if not binding_keys:
    #     sys.stderr.write('Usage: %s [binding_key]... \n' % sys.argv[0])
    #     sys.exit(0)

    binding_key = f"{car_type}.{origem}.{destination}"

    # Faz a conexão da fila com a binding key passada
    channel.queue_bind(exchange='topic_logs',
                       queue=queue_name,
                       routing_key=binding_key)

    print(f" {driver_name} aguardando corridas, {binding_key}.\n")

    # Sobrescrevendo a função de retorno da mensagem da fila
    def callback(ch, method, properties, body):
        print(f" CORRIDA RECEBEBIDA: {body}, Routing key: {method.routing_key}\n")

    # Informa a fila que ela receberá mensagens da função callback
    # Informa que ela só enviará um pedido para um receptor se receber o ack dele
    channel.basic_consume(queue=queue_name,
                          on_message_callback=callback,
                          auto_ack=True)

    channel.start_consuming()

# p1 = threading.Thread(target=publisher, args=("João", "*", "centro", "batel"))
consumer("Zezão", "*", "*", "*")
