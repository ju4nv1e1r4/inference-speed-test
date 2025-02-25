package main

import (
 "context"
 "fmt"
 "log"
 "time"

 pb "predict/churnpb" // package dos arquivos gerados pelo .proto

 "google.golang.org/grpc"
)

func main() {
 // Conecta com o servidor
 conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure())
 if err != nil {
  log.Fatalf("Falha ao conectar ao servidor: %v", err)
 }
 defer conn.Close()
 
 // Cria o client
 client := pb.NewChurnServiceClient(conn)

 ctx, cancel := context.WithTimeout(context.Background(), time.Second)
 defer cancel()

 // Cria uma requisição com os dados
 req := &pb.Features{
  Gender:           "Male",
  SubscriptionType: "Premium",
  ContractLength:   "Annual",
 }

 // Realiza a inferência
 resp, err := client.Predict(ctx, req) //
 if err != nil {
  log.Fatalf("Erro ao chamar Predict: %v", err)
 }

 // Imprime a resposta da inferência
 fmt.Printf("Churn previsto: %d\n", resp.Churn)
