# README - Anameasy (Protótipo Demonstrativo)

**Bem-vindo ao Anameasy - Facilitando o seu Atendimento Médico!**

Este é um protótipo demonstrativo desenvolvido em Python para apresentar algumas funcionalidades relacionadas ao atendimento médico. É importante ressaltar que este projeto é um protótipo educacional e serve como uma base para futuras implementações e melhorias. Abaixo estão as principais funcionalidades e instruções de uso:

## Funcionalidades

### 1. Cadastro de Usuário
   - **Opção:** 1 - Usuário
   - **Descrição:** Permite ao usuário cadastrar suas informações pessoais, como nome completo, CPF, e-mail e número de telefone.

### 2. Preencher Ficha de Anamnese
   - **Opção:** 2 - Preencher Ficha
   - **Descrição:** Solicita informações relacionadas à saúde do usuário, como queixa principal, histórico médico, hábitos e histórico familiar. Com base nessas informações, é calculada uma categoria de urgência.

### 3. Escolher Hospital
   - **Opção:** 3 - Ir para o Hospital
   - **Descrição:** Calcula a distância entre a localização do usuário e os hospitais cadastrados. Permite ao usuário escolher um hospital próximo para atendimento. Após a escolha, gera uma senha de atendimento.

### 4. Encerrar Programa
   - **Opção:** 4 - Logout
   - **Descrição:** Encerra o programa.

## Configurações

O usuário tem a flexibilidade de ajustar a localização utilizada para calcular a distância até os hospitais que estão nos banco de dados. Para isso, é necessário modificar as coordenadas de latitude e longitude diretamente no código-fonte.

```python
latitude = -23.644909
longitude = -46.636527
```
## Arquivos JSON

Este protótipo utiliza arquivos JSON para armazenar dados importantes, como informações do usuário, ficha de anamnese, sintomas e informações dos hospitais. Abaixo estão os arquivos JSON associados:

### 1. `user.json`
   - Armazena as informações cadastradas pelo usuário, como nome, CPF, e-mail e número de telefone.
   - **Localização:** `../json/user.json`

### 2. `anamnese.json`
   - Armazena os dados preenchidos na ficha de anamnese, como queixa principal, histórico médico e hábitos.
   - **Localização:** `../json/anamnese.json`

### 3. `sintomas.json`
   - Contém informações sobre categorias de sintomas e suas classificações de urgência.
   - **Localização:** `../json/sintomas.json`

### 4. `hospital.json`
   - Armazena informações sobre hospitais, incluindo nome, latitude e longitude.
   - **Localização:** `../json/hospital.json`