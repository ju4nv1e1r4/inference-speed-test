import grpc
import pickle
import numpy as np
from concurrent import futures

import churn_pb2
import churn_pb2_grpc
from schemas import preprocess_input, Features

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

class ChurnService(churn_pb2_grpc.ChurnServiceServicer):
    def Predict(self, request, context):
        features = Features(
            gender=request.gender,
            subscription_type=request.subscription_type,
            contract_length=request.contract_length
        )
        input_data = preprocess_input(features)

        prediction = model.predict(input_data)

        return churn_pb2.PredictResponse(churn=int(prediction[0]))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    churn_pb2_grpc.add_ChurnServiceServicer_to_server(ChurnService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Servidor gRPC rodando na porta 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
