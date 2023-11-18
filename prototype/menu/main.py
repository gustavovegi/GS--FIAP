import datetime
import json
import math

#escrevendo com arquivo json
def write_Json(file_,data):
    with open(file_, 'w') as file:
        json.dump(data,file)
    file.close()
def read_json(doc):
    with open(doc, "r") as file:
        data = json.load(file)
    file.close()
    return data


#Validando campos
def valid_email():
        email = input("E-mail:")
        if not '@' in email:
            print("email invalido")
            valid_email()
        return email
    

def limpa_dado(campo):
    resposta = ''
    campo = str(campo)
    for i in campo:
        if ( i.isnumeric()):
            resposta += i
    return resposta

          
def valid_number(campo, rule):
    var = None
    while True:
        var = (input(campo))
        var = limpa_dado(var)
        tamanho = len(str(var))
        if tamanho == rule:
            break
        else:
            print(f"{campo} invalido")
    print(var)
    return var


#OPÇÃO UM
def cadastras_user():

    nome_user = input("Nome Completo:")
    CPF = valid_number("CPF",11)
    email = valid_email()
    number_phone = valid_number("Telefone",11)

    user_info = {
        "Nome Completo": nome_user,
        "E-mail": email,
          "Celular": number_phone,
        "CPF": CPF,
    }
    write_Json("../json/user.json", user_info)
    print("usuário cadastrado com sucesso!!")

#OPÇÃODOIS
def anamnese_on():
    #se o json do cadastro estiver sem nada pedir para o usuário se cadastrar
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
    #prototipando a inteligencia artificial
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

    print(f"urgencia nivel: {urgencia}")
    write_Json("../json/anamnese.json", anamnese)

#OPAÇÃOTRÊS

#configurações de distancia
def calculate_distance(latitude1, longitude1, latitude2, longitude2):
    earth_radius_km = 6371.01
    distance_in_km = earth_radius_km * math.acos(
        math.sin(math.radians(latitude1)) * math.sin(math.radians(latitude2)) +
        math.cos(math.radians(latitude1)) * math.cos(math.radians(latitude2)) * math.cos(math.radians(longitude1 - longitude2))
    )
    return distance_in_km
def get_hospital():
    latitude = -23.644909
    longitude = -46.636527
    try:
        hospital_data = read_json('../json/hospital.json')
        hospitals =[ ]
        for hospital in hospital_data:
             distance = calculate_distance(latitude, longitude, hospital["latitude"], hospital["longitude"])
             hospitals.append({
                    "name": hospital["name"],
                    "distance": distance
            })
        print(hospitals)
        return hospitals

    except Exception as e:
        print(e)
        return None

# Configuração do menu
opcoes_menu = {
    "1": cadastras_user,
    "2": anamnese_on,
    "3":get_hospital
}

print("seja-bem vindo ao anameasy")
while True:
    print("\nSelecione uma opção:")
    print("1 - Usuário")
    print("2 - preeencher ficha")
    print("3 - ir para hospital")

    escolha = input("->")
    if escolha in opcoes_menu:
        opcoes_menu[escolha]()
    else:
        print("Opção inválida. Por favor, digite novamente.")











