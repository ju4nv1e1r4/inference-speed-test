# Melhorando a Latência da Inferência de Modelos de ML

Este repositório se trata de experimentos de model serving em linguagens diferentes. Pense no python como a industria, fábrica o modelo, mas não o serve tão bem em APIs, softwares e sistemas. O desafio aqui é encontrar a melhor implementação para servir modelos de Machine Learning, visando reduzir a latência.

## Servindo com FastAPÍ e alimentando um client Go

Python:
<img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ClxrLiDhN-b2Sze15D2Acw.png">

Golang:
<img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*IOmuFgAfuAFdo3guRDMgEA.png">

Observações:

  Go é significativamente mais rápido: Os tempos de execução em Go (em média 0,0215 segundos) são consideravelmente menores do que em Python (em média 0,0615 segundos). Isso indica que, para este cenário específico, a aplicação Go apresenta um desempenho superior.
  Baixa variância: Os tempos de execução em ambos os testes são bastante consistentes, com pequenas variações entre as execuções.
  Tempo de usuário e sistema: Em ambos os casos, o tempo de usuário e de sistema são muito baixos, indicando que a maior parte do tempo de execução é provavelmente gasta em operações de I/O ou na comunicação com o servidor.

## Servindo com gRPC + Go + Python

Python:

```
(env) juanvieira@juanvieira:~/local/pymlgo/python$ time python3 client.py
Predição de Churn: 0

real 0m0,273s
user 0m0,202s
sys 0m0,037s
(env) juanvieira@juanvieira:~/local/pymlgo/python$ time python3 client.py
Predição de Churn: 0

real 0m0,260s
user 0m0,170s
(env) juanvieira@juanvieira:~/local/pymlgo/python$ time python3 client.py
Predição de Churn: 0

real 0m0,267s
user 0m0,182s
sys 0m0,040s
```

Golang:
```
juanvieira@juanvieira:~/local/pymlgo/go$ time ./churn
Churn previsto: 0

real 0m0,055s
user 0m0,000s
sys 0m0,013s
juanvieira@juanvieira:~/local/pymlgo/go$ time ./churn
Churn previsto: 0

real 0m0,051s
user 0m0,000s
sys 0m0,012s
juanvieira@juanvieira:~/local/pymlgo/go$ time ./churn
Churn previsto: 0

real 0m0,070s
user 0m0,007s
sys 0m0,007s
```

1. Performance — Go vs Python
    O tempo de execução em Go é muito mais rápido do que em Python, como você observou. Isso ocorre porque Go é uma linguagem compilada e a execução do binário diretamente é significativamente mais rápida do que a execução de um código interpretado em Python.
    Go é altamente eficiente para operações de rede, como no caso de um servidor gRPC, o que faz com que ele seja uma excelente escolha quando a performance é um fator crucial.

2. Compilação em Go
    A vantagem de compilar o código em Go em vez de interpretá-lo (como no Python) resulta em menor overhead de tempo de execução.
    Isso é especialmente notável em sistemas distribuídos de alto desempenho, como serviços que utilizam gRPC, onde a latência e o tempo de resposta são fundamentais para a experiência do usuário.

   Autor: Juan Vieira
