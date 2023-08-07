

import hashlib
string = ''
while string != 'sair':
    string = input("Digite uma palavra para gerar o hash (ou 'sair' para encerrar): ")
    
    if string.lower() == "sair":
        break
    
    hash_obj = hashlib.sha1()
    hash_obj.update(string.encode('utf-8'))
    hash_value = hash_obj.hexdigest()
    
    print("Hash SHA-1 da palavra:", hash_value)
