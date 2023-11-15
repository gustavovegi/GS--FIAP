import json
# escrevendo com JSON
def write_Json(file_,data):
    with open(file_, 'w') as file:
        json.dump(data,file)
    file.close()

#VALIDAÇÕES DE CADASTRO
def valid_cpf():
    cpf = input('cpf')
    tamanho_cpf = len(str(cpf))
    if ( tamanho_cpf == 11):
        valid = cpf
        return valid
    else:
        print("cpf invalido")
        valid_cpf()
    return

#OPÇÃO UM
def cadastras_user():
# validar as ifos, transforma em um dicionario para depois conerver em um json
    nome_user = input("nome completo:")
    cep = valid_cpf()
    user_info = {
        "Nome Completo": nome_user,
        "CPF": cep
    }
    write_Json("../json/user.json", user_info)

cadastras_user()






