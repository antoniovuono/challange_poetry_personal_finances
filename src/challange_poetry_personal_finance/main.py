import pandas as pd
import matplotlib.pyplot as plt

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
    
def clean_category(df): 
    # Remove espaços em branco e padroniza para capitalização (Primeira letra maiúscula)
    df['categoria'] = df['categoria'].str.strip().str.capitalize()
    # Ajustar categorias incorretas ou inconsistentes
    df['categoria'] = df['categoria'].replace({
        'transporte': 'Transporte',
        'alimentacao': 'Alimentação',
        None: 'Outros',
    })
    return df

def clean_date(df): 
    # converter a coluna data para o formato datetime
    df['data'] = pd.to_datetime(df['data'], errors='coerce')
    return df

def drop_duplicates(df):
    df = df.drop_duplicates()
    return df

def statatics(df): 
    print(f"\n💰 Total gasto: R$ {df['valor'].sum():,.2f}")
    print(f"📈 Maior despesa: R$ {df['valor'].max():.2f}")
    print(f"📉 Menor despesa: R$ {df['valor'].min():.2f}")
    print(f"📊 Média de despesa: R$ {df['valor'].mean():.2f}")

def resume_per_category(df):
    resumo = df.groupby("categoria")["valor"].sum().sort_values(ascending=False)
    print("\nGastos por categoria:")
    print(resumo)

def resumo_por_mes(df):
    df["mes"] = df["data"].dt.to_period("M")  # Ex: 2025-08
    resumo = df.groupby("mes")["valor"].sum()
    print("\nGastos por mês:")
    print(resumo)

def grafico_categoria(df):
    resumo = df.groupby("categoria")["valor"].sum()
    resumo.plot.pie(autopct="%1.1f%%", figsize=(6, 6))
    plt.title("Distribuição dos gastos por categoria")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()

def main():
    file_path = "data/despesas_pessoais.csv"
    df = load_data(file_path)
    data_info(df)
    df = clean_category(df)
    df = clean_date(df)
    df = drop_duplicates(df)

    statatics(df)
    resume_per_category(df)
    resumo_por_mes(df)
    grafico_categoria(df)

    df.to_csv("data/despesas_limpo")

if __name__ == "__main__":
    main()
