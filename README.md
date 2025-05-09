# Projeto câncer de pulmão

O câncer de pulmão é responsável por um número significativo de mortes anuais. Esta doença caracteriza-se pelo crescimento descontrolado de células no pulmão, que pode se espalhar para outras partes do corpo. Fatores de risco como tabagismo, exposição a poluentes ambientais e substâncias tóxicas, além de predisposição genética, estão fortemente associados ao desenvolvimento da doença. O diagnóstico precoce e o tratamento adequado são fundamentais para aumentar as chances de sobrevivência, mas muitas vezes a doença é descoberta em estágios avançados, o que dificulta o sucesso terapêutico.

Este conjunto de dados consiste em 5.000 registros com 18 características relacionadas a fatores de risco e previsão de câncer de pulmão. Inclui informações demográficas, hábitos de vida, histórico médico e sintomas associados à doença pulmonar. O objetivo do projeto é realizar tratamento dos dados, análise exploratória e criação de modelo de machine learning com foco em previsão de risco de desenvolvimento de câncer de pulmão.

Fonte dos dados: [Kaggle](https://www.kaggle.com/datasets/shantanugarg274/lung-cancer-prediction-dataset)

[Notebooks desenvolvidos no projeto](./notebooks/)

## Resultados principais

[Neste notebook](./notebooks/projeto_cancer_pulmao_02_eda.ipynb) foi realizada análise exploratória para avaliação dos insights principais.

[Neste notebook](./notebooks/projeto_cancer_pulmao_03_classificacao.ipynb) foi criado o modelo de classificação para câncer de pulmão ([disponível aqui](./modelos/)) de acordo com os dados avaliados na etapa de análise exploratória.

## Organização do projeto

```
├── LICENSE            <- Licença de código aberto.
├── README.md          <- Instruções e detalhes do projeto.
|
├── dados              <- Arquivos de dados para o projeto.
|
├── modelos            <- Arquivos de modelos de ML criados no projeto.
|
├── notebooks          <- Cadernos Jupyter. A numeração indica a ordem em que as etapas
|                         foram executadas.
│
|   └──src             <- Dados centralizados organizados para uso neste projeto.
|      │
|      ├── __init__.py  <- Torna um módulo Python.
|      ├── config.py    <- Configurações básicas de caminhos de arquivos do projeto.
|      ├── graphics.py  <- Variáveis e funções para gráficos utilizadas no projeto.
|      ├── models.py    <- Variáveis e funções para modelos de ML utilizadas no projeto.
|
```
