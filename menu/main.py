import json
import datetime
#escrevendo com arquivo json
def write_Json(file_,data):
    with open(file_, 'w') as file:
        json.dump(data,file)
    file.close()

#Validando dado do cadastro
def valid_email():
    #melhorar a validação
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

        "Nome Completo": nome_user,
        "E-mail": email,
          "Celular": number_phone,
        "CPF": CPF,
    }

    write_Json("../json/user.json", user_info)
    print("usuário cadastrado com sucesso!!")

def anamnese_on():
    # Solicitar as informações necessárias para a anamnese
    #usar infomações do cadastro
    #se o json do cadastro estiver sem nada pedir para o usuário se cadastrar
    #exibir os dados que estão no cadastro
    #configurar algumas repostas para não ter erro dos usuários ( valida-la)

    day = datetime.datetime.now()
    day_string = day.strftime("%Y-%m-%d %H:%M:%S")
    queixa_principal = input("Queixa principal do paciente:")
    dias_queixa= input("A quanto tempo vem sentindo os sintomas:")

    # História médica
    doencas_cronicas = input("Você tem alguma doença crônica? ")
    cirurgias = input("Você já fez alguma cirurgia? ")
    alergias = input("Você tem alguma alergia? ")
    medicamentos = input("Você toma algum medicamento? ")
    fumar = input("Você fuma? ")
    beber = input("Você bebe? ")
    historico_familiar = input("Você tem algum histórico familiar de doenças? ")

    anamnese = {
        "Hora do preenchimento da ficha": day_string,
        "Queixa principal": queixa_principal,
        "Dias da queixa": dias_queixa,
        "Doenças crônicas": doencas_cronicas,
        "Cirurgias": cirurgias,
        "Alergias": alergias,
        "Medicamentos": medicamentos,
        "Fumar": fumar,
        "Beber": beber,
        "Histórico familiar": historico_familiar
    }

    # Verificar a urgência da consulta
    #prototipando a inteligencia artificial kakakakakakaka
    #confirmar com danielo

    if queixa_principal.lower() == "dor no peito":
        urgencia = "I"
    elif dias_queixa.lower() == "menos de 24 horas":
        urgencia = "I"
    elif doencas_cronicas.lower() == "sim":
        urgencia = "II"
    elif queixa_principal.lower() == "febre alta" and dias_queixa.lower() == "menos de 24 horas":
        urgencia = "I"
    else:
        urgencia = "III"

    print("urgencia nivel: ")


    write_Json("../json/anamnese.json", anamnese)

anamnese_on()









