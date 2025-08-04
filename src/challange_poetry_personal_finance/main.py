import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

# Estudo do dataframe: Aqui é o momento de análisar os dados e verificar pontos de limpeza.
def data_info(df):
    print("\n Dataset:")
    print(df.head(10))
    print("\n Informações do dataset:")
    df.info()
    print("\n Quantidades de dados nulos por categoria:")
    print(df.isnull().sum())

# Limpeza:
# 1. Categorias: 59 dados nulos. (Modificar para outros... )
# 2. Categorias: Padronizar formatos dos dados.

def main():
    file_path = "data/despesas_pessoais.csv"
    df = load_data(file_path)
    data_info(df)

if __name__ == "__main__":
    main()
