package main

import (
	"context"
	"fmt"
	"log"
	"time"

	pb "predict/churnpb" // Ajuste o caminho conforme necessário

	"google.golang.org/grpc"
)

func main() {
	// Conectar ao servidor gRPC
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure()) // Ajuste a porta conforme necessário
	if err != nil {
		log.Fatalf("Falha ao conectar ao servidor: %v", err)
	}
	defer conn.Close()

	client := pb.NewChurnServiceClient(conn) // Ajuste para ChurnService

	// Criar o contexto da requisição
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	// Criar uma requisição com os dados
	req := &pb.Features{
		Gender:           "Male",
		SubscriptionType: "Premium",
		ContractLength:   "Annual",
	}

	// Enviar requisição ao servidor gRPC
	resp, err := client.Predict(ctx, req) // Ajuste para Predict
	if err != nil {
		log.Fatalf("Erro ao chamar Predict: %v", err)
	}

	// Exibir resposta
	fmt.Printf("Churn previsto: %d\n", resp.Churn)
}
