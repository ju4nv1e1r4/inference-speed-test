package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"

	"github.com/gin-gonic/gin"
)

// Estrutura para os dados de entrada
type Features struct {
	Gender           string `json:"gender"`
	SubscriptionType string `json:"subscription_type"`
	ContractLength   string `json:"contract_length"`
}

// Estrutura para a resposta do FastAPI
type PredictResponse struct {
	Churn int `json:"churn"`
}

func main() {
	r := gin.Default()

	r.POST("/predict", func(c *gin.Context) {
		var features Features

		// Bind JSON recebido pelo cliente
		if err := c.ShouldBindJSON(&features); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}

		// Converte para JSON para enviar ao FastAPI
		jsonData, err := json.Marshal(features)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": "Erro ao criar JSON"})
			return
		}

		// Faz a requisição para o FastAPI
		resp, err := http.Post("http://127.0.0.1:8000/predict/", "application/json", bytes.NewBuffer(jsonData))
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": "Erro ao chamar o FastAPI"})
			return
		}
		defer resp.Body.Close()

		// Lê a resposta do FastAPI
		body, err := ioutil.ReadAll(resp.Body)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": "Erro ao ler resposta do FastAPI"})
			return
		}

		// Envia a resposta para o cliente
		c.Data(resp.StatusCode, "application/json", body)
	})

	fmt.Println("Servidor Gin rodando na porta 8080...")
	r.Run(":8080") // Roda na porta 8080
}