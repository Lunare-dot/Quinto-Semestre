import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Identifica o arquivo que foi enviado
    bucket_origem = event['Records'][0]['s3']['bucket']['name']
    nome_arquivo = event['Records'][0]['s3']['object']['key']
    
    # Define o bucket de destino (substituindo a palavra 'entrada' por 'saida')
    bucket_destino = bucket_origem.replace("entrada", "saida")
    
    # Lê o conteúdo do arquivo
    objeto = s3.get_object(Bucket=bucket_origem, Key=nome_arquivo)
    conteudo_original = objeto['Body'].read().decode('utf-8')
    
    # Regra de negócio: transformar em Maiúsculas
    conteudo_processado = conteudo_original.upper()
    
    # Salva o novo arquivo no bucket de saída
    s3.put_object(Bucket=bucket_destino, Key=nome_arquivo, Body=conteudo_processado)
    
    return {"status": "Processado com sucesso!"}