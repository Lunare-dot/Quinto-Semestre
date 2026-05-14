import re

def RegEx(text):
    emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    
    print("\nE-mails encontrados:")
    for email in emails:
        print(email)
        
    numbers = re.findall(r'\(\d{2}\)\d{4,5}-\d{4}', text)
    
    print("\nNúmeros encontrados:")
    for number in numbers:
        print(number)
        
    clean_text = re.sub(r'\s+', ' ', text).strip()
    
    print("\nTexto limpo:")
    print(clean_text)

text = input("Digite um texto: ")
RegEx(text)

#Texto de teste:
#Meu email é corinthiansdasilva@gmail.com     e o telefone é (11)99999-8888. Também tenho o email fielhaxixe@empresa.com e o número é (21)3333-4444.