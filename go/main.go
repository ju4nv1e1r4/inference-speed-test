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
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure()) // Ajuste a porta conforme necessário
	if err != nil {
		log.Fatalf("Falha ao conectar ao servidor: %v", err)
	}
	defer conn.Close()

	client := pb.NewChurnServiceClient(conn) // Ajuste para ChurnService

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	
	req := &pb.Features{
		Gender:           "Male",
		SubscriptionType: "Premium",
		ContractLength:   "Annual",
	}

	
	resp, err := client.Predict(ctx, req) //
	if err != nil {
		log.Fatalf("Erro ao chamar Predict: %v", err)
	}

	// Realiza inferência
	fmt.Printf("Churn previsto: %d\n", resp.Churn)
}
