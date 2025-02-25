import grpc
import churn_pb2
import churn_pb2_grpc

def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = churn_pb2_grpc.ChurnServiceStub(channel)

    request = churn_pb2.Features(
        gender="Male",
        subscription_type="Premium",
        contract_length="Annual"
    )

    response = stub.Predict(request)
    print(f"Predição de Churn: {response.churn}")

if __name__ == "__main__":
    run()
