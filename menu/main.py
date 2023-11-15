import json
#escrevendo com arquivo json
def write_Json(file_,data):
    with open(file_, 'w') as file:
        json.dump(data,file)
    file.close()

#Validando dado do cadastro
def valid_email():
    #retirar os espços caso o usuario coloque
        email = input("E-mail:")
        if not '@' in email:
            print("email invalido")
            valid_email()
        return email

def valid_number(campo, rule):
    #retirar os espaços do caso o usuario coloque
    #exemplo 524 547 778 51
    var = None
    while True:
        var = int(input(campo))
        tamanho = len(str(var))
        if tamanho == rule:
            break
        else:
            print(f"{campo} invalido")

    return var

#OPÇÃO UM
def cadastras_user():

    nome_user = input("Nome Completo:")
    CPF = valid_number("CPF",11)
    email = valid_email()
    print("formato do numero (xx)xxxxxxxxx")
    number_phone = valid_number("Telefone",11)
    #fazendo dicionario com os cadastros

    user_info = {
        "CPF": CPF,
        "Nome Completo": nome_user,
        "E-mail": email,
        "Celular": number_phone
    }
    write_Json("../json/user.json", user_info)
    print("usuário cadastrado com sucesso!!")

cadastras_user()






