import pandas as pd

def load_data(path):
    try:
        df = pd.read_csv(path)
        df['data'] = pd.to_datetime(df['data'])
        return df
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return pd.DataFrame()