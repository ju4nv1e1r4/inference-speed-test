package models

import (
	"fmt"

	"github.com/sjwhitworth/golearn/base"
	"github.com/sjwhitworth/golearn/ensemble"
	"github.com/sjwhitworth/golearn/evaluation"
)

func RandomForestCls()  {
	rawData, err := base.ParseCSVToInstances("../data/churn.csv", true)
	if err != nil {
		panic(err)
	}

	model := ensemble.NewRandomForest(10, 3)
	trainData, testData := base.InstancesTrainTestSplit(rawData, 0.7)
	model.Fit(trainData)

	predictions, err := model.Predict(testData)
	if err != nil {
		panic(err)
	}

	confunsionMatrix, err := evaluation.GetConfusionMatrix(testData, predictions)
	if err != nil {
		panic(fmt.Sprintf("Erro ao gerar matriz de confusão: %s.", err.Error()))
	}
	fmt.Println(evaluation.GetSummary(confunsionMatrix))
}