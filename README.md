# Challenge de Data Science

<div align="center">
<img src="https://i.imgur.com/oxab3uu.png" width="800px" />
</div>

Neste projeto, vamos trabalhar com a Alura Cash, estudar o banco de dados e modelar um sistema para avaliar se novos clientes possuem potêncial de inadimplência ou não.

São 3 etapas propostas separadas por semanas com graus de dificuldade crescentes em que cada uma respectivamente corresponde aos seguintes objetivos:

1- Restaurar BD Alura Cash.

2- Construção  e validação do Modelo de Aprendizado de Maquina.

3- Hospedar Modelo em API. Criar requisição para API e apresentar resultado na ferramenta PowerBI.


## Semana 1

A semana 1 é dedicada à análise e estruturação dos dados oferecidos pelo banco com MySQL. Através de um DUMP foi obtido os todos os dados necessários para o projeto. Foi observado que os dados estavam relacionados através do ID e dessa forma foi possível relacionado todas as informçaões e os tratamentos necessários. A tabela de dados unidos foi exportada do MySQL como ***csv***.

## Semana 2

Através da linguagem ** Python** e utilizando o ambiente do **Google Colab** os dados obtidos do MySQL foram tratados conforme o procedimento abaixo:
1- Remoção dos dados nulos
2- Tratamento de outliers
3- Identificação e correção de variáveis faltantes
4- Aplicação de enconding e normalização
5- Balanceamento da variável alvo
6- Criação e avaliação de modelos de classificação 


## Semana 3 e 4

O desafio desta semana foi focado em fornecer os modelos criados na semana 2 através de uma API para o Power BI e poder fazer predições em um cliente ainda não avaliado pelo modelo. Informando se o banco irá fazer a concessão de crédito ou não.

1- Criação de API para disponibilização de modelo
2- Conectar API ao PowerBI
3- Criação de parámetros para receber os dados do cliente
4- Finalização de dashboard

Foi utilizado a biblioteca FastAPI e Uvicorn para poder consumir no Power BI. O sistema faz uma requisição na API e ela retorna se o cliente com os dados passados poderá se tornar inadimplente ou não, retornando também as probabilidades. 


