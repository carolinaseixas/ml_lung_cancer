from pathlib import Path


PASTA_PROJETO = Path(__file__).resolve().parents[2]

PASTA_DADOS = PASTA_PROJETO / "dados"

DADOS_ORIGINAIS = PASTA_DADOS / "lung_cancer_dataset.csv"
DADOS_LIMPOS = PASTA_DADOS / "lung_cancer_clean.parquet"

PASTA_MODELOS = PASTA_PROJETO / "modelos"

MODELO_FINAL = PASTA_MODELOS / "lung_cancer_model.joblib"
