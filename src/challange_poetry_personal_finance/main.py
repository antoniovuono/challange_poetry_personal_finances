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
    print("\n Valores únicos por categorias:")
    print(df["categoria"].unique())
    print("\n Valores negativos ou zero:")
    print(df[df['valor'] <= 0].shape[0])
    print("\n Data inválidas:")
    print(pd.to_datetime(df["data"], errors="coerce").isnull().sum())
    print("\n Dados duplicados:")
    print(df.duplicated().sum())

# Limpeza:
# 1. Categoria: 59 dados nulos. (Modificar para outros... )
# 2. Categoria: Padronizar formatos dos dados.
# 3. Data: Padronizar formatos dos dados. Alimentação/alimentação

def main():
    file_path = "data/despesas_pessoais.csv"
    df = load_data(file_path)
    data_info(df)

if __name__ == "__main__":
    main()
