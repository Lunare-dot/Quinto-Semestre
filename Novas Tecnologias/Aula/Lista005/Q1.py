import os
from datetime import datetime

uPath = input("Digite o path: ")

tArchives = 0
tDir = 0
tSize = 0

for item in os.listdir(uPath):
    fullPath = os.path.join(uPath, item)
    
    if os.path.isfile(fullPath):
        
        tArchives += 1
        
        size = os.path.getsize(fullPath)
        tSize += size
        
        mod = os.path.getmtime(fullPath)
        modDate = datetime.fromtimestamp(mod)
        
        print(f"Nome do arquivo: {item}")
        print(f"Tamanho do arquivo: {size}")
        print(f"Data de modificação: {modDate}")
    
    elif os.path.isdir(fullPath):
        tDir += 1
        
print(f"Quantidade de arquivos: {tArchives}")
print(f"Quantidade de diretórios: {tDir}")
print(f"Tamanho total dos arquivos: {tSize}")