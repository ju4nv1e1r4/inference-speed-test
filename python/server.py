import grpc
import pickle
import numpy as np
from concurrent import futures

import churn_pb2 # estamos importanto os dois arquivos
import churn_pb2_grpc
from schemas import preprocess_input, Features # importamos o schemas.py que criei para validação de dados

# Carregamos o arquivo
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Criamos a classe para o serviço
class ChurnService(churn_pb2_grpc.ChurnServiceServicer):
    # Criamos o método "Predict" para realizar a inferência
    def Predict(self, request, context):
        features = Features(
            gender=request.gender,
            subscription_type=request.subscription_type,
            contract_length=request.contract_length
        )
        input_data = preprocess_input(features)

        prediction = model.predict(input_data)

        return churn_pb2.PredictResponse(churn=int(prediction[0]))
# Criamos aqui o servidor
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    churn_pb2_grpc.add_ChurnServiceServicer_to_server(ChurnService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Servidor gRPC rodando na porta 50051...")
    server.wait_for_termination()

# Servimos o servidor
if __name__ == "__main__":
    serve()
