import os
import zipfile

def script(path):
    files_data = {}
    
    with zipfile.ZipFile('backup.zip', 'w', compression=zipfile.ZIP_DEFLATED) as zf:
    
        for file in os.listdir(path):
            full_path = os.path.join(path, file)
            
            if file.endswith(".txt"):
                original_size = os.path.getsize(full_path)
                
                files_data[file] = {
                    "tamanho original": original_size
                }
                
                zf.write(full_path, arcname=file)
        
        for info in zf.infolist():
            files_data[info.filename]["tamanho comprimido"] = info.compress_size
            
    return files_data
    
u_entry = input("Digite o path do diretório dos arquivos .txt: ")
result = script(u_entry)

for file, data in result.items():
    print(f"Arquivo .txt: {file}")
    print(f"Tamanho original: {data["tamanho original"]} bytes")
    print(f"Tamanho comprimido: {data["tamanho comprimido"]} bytes")