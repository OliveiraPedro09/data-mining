import pandas as pd

def processar_emails(lista_emails):
    df = pd.DataFrame(lista_emails, columns=['email'])
    df['dominio'] = df['email'].str.split('@').str[-1]
    df['is_empresarial'] = df['dominio'].str.endswith('.com.br').astype(int)
    return df

emails = ["user@gmail.com", "contato@empresa.com.br", "dev@startup.com.br", "teste@outlook.com"]
print(processar_emails(emails))