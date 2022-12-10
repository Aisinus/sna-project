import sys
import ProtoFile_pb2 as pb2
import ProtoFile_pb2_grpc as pb2_grpc
import grpc
from concurrent import futures

clients = {}


class ClientMetric(pb2_grpc.ClientMetricServiceServicer):
    def __init__(self):
        pass

    def SendMetric(self, request, context):
        try:
            print(f'{request.cpu} {request.ram} {context.peer()}')
        except Exception as ex:
            print(f'error {ex}')
        return pb2.Empty()


def serve():
    address = 'localhost'
    port = sys.argv[1]
    max_size = sys.argv[2] if len(sys.argv) > 2 else 10
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_size))
    pb2_grpc.add_ClientMetricServiceServicer_to_server(ClientMetric(), server)
    server.add_insecure_port(f'{address}:{port}')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    try:
        serve()
    except KeyboardInterrupt:
        print("Shutting down")
        sys.exit()
