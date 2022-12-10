import sys

import psutil
import grpc
import ProtoFile_pb2 as pb2
import ProtoFile_pb2_grpc as pb2_grpc

address = 'localhost:5505'
channel = grpc.insecure_channel(address)
stub = pb2_grpc.ClientMetricServiceStub(channel)

def get_info():
    return psutil.cpu_percent(interval=1, percpu=False), psutil.virtual_memory().percent

try:
    while True:
        cpu, ram = get_info()
        print(type(ram))
        message = pb2.Metric(cpu=cpu, ram=ram)
        stub.SendMetric(message)
except KeyboardInterrupt:
    print("shutting down")
    sys.exit()
