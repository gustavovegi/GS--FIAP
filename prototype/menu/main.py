import datetime
import random
import json
import math

#escrevendo com arquivo json
def write_Json(file_path,data):
    with open(file_path, 'w') as file:
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
def check_symptoms_urgency(symptoms, urgency_data):
    for category in urgency_data["categories"]:
        if any(symptom in category["symptoms"] for symptom in symptoms):
            return category["name"]
    return "Não classificado"

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
    urgency_data = read_json('../json/sitomas.json')
    patient_symptoms = [queixa_principal, doencas_cronicas, cirurgias, alergias, medicamentos, fumar, beber,historico_familiar]
    urgency_category = check_symptoms_urgency(patient_symptoms, urgency_data)
    print(f"A categoria de urgência é: {urgency_category}")
    write_Json("../json/anamnese.json", anamnese)

#OPAÇÃOTRÊS
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
        hospitals = []
        for hospital in hospital_data:
            distance = calculate_distance(latitude, longitude, hospital["latitude"], hospital["longitude"])
            hospitals.append({
                "name": hospital["name"],
                "distance": distance
            })
        while True:
            # Mostra os hospitais disponíveis
            print("Hospitais disponíveis:")
            for i, hospital in enumerate(hospitals, start=1):
                print(f"{i}. {hospital['name']} - Distância: {hospital['distance']} km")
            escolha_hospital = input("Escolha o número do hospital desejado (ou 's' para sair): ")
            if escolha_hospital.lower() == 's':
                print("Você saiu da seleção de hospitais.")
                return None
            try:
                escolha_hospital = int(escolha_hospital)
                if 1 <= escolha_hospital <= len(hospitals):
                    hospital_escolhido = hospitals[escolha_hospital - 1]
                    print(f"Você escolheu o hospital {hospital_escolhido['name']}.")
                    numero_senha = random.randint(1, 50)
                    print(f"Sua senha de atendimento é a {numero_senha}")
                    return hospital_escolhido
                else:
                    print("Escolha inválida. Por favor, escolha um número de hospital válido.")
            except ValueError:
                print("Por favor, digite um número válido.")
    except Exception as err:
        print(err)
        return None
#Opção 4
def encerrar_programa():
    print("Encerrando...")
    exit()
    return


# Configuração do menu
opcoes_menu = {
    "1": cadastras_user,
    "2": anamnese_on,
    "3":get_hospital,
    "4": encerrar_programa
}

print("seja-bem vindo ao anameasy")
while True:
    print("\nSelecione uma opção:")
    print("1 - Usuário")
    print("2 - preeencher ficha")
    print("3 - ir para hospital")
    print("4- Logout")

    escolha = input("->")
    if escolha in opcoes_menu:
        opcoes_menu[escolha]()
    else:
        print("Opção inválida. Por favor, digite novamente.")











