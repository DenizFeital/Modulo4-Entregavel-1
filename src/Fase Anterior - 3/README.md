<!-- Sobre este projeto -->
## Sobre este projeto


Este engajamento foi feito pensando em desenvolver uma solução para a Farm Tech Solutions, uma solução para conectar os sensores físicos existentes no campo em uma plataforma digital.

### Ferramentas utilizadas

As ferramentas utilizadas para este engajamento foram:
* Visual Studio Code
* Plataforma web Wokwi
* Banco de Dados Oracle
* Oracle Modeler
* Python
* ChatGPT!




<!-- Visão Geral -->
## Visão Geral

### Requisitos

* Desenvolver uma solução onde se possa coletar as informações obtidas pelo sensores instalados na Farm Tech Solutions, com o objetivo de coletar dados sobre as plantações, especificamente sobre os seguintes pontos:

  * Potássio
  * Fósforo
  * Luminosidade
  * Humidade

* Desenvolver também um controle de irrigação, onde determinamos as condições que o sistema de irrigação deve entrar em ação.
    Esta configuração foi feita através do ESP32.
<img width="598" alt="image" src="https://github.com/user-attachments/assets/099e4a5b-0e8c-4088-80cb-3f10b015de6e">


* Armazenar todas as informações dos sensores em base de dados.
A base de dados escolhida foi o Oracle.
<img width="260" alt="image" src="https://github.com/user-attachments/assets/5cd13428-b9b2-4255-9463-dc7ba387b381">

### Bases de Dados

* A modelagem das bases de dados foi feita através do Data Modeler da Oracle

Estrutura lógica do banco de dados:

<img width="674" alt="image" src="https://github.com/user-attachments/assets/9b1d3348-1cca-4db6-b2c5-06e84c0aec3c">

Estrutura física do banco de dados:

<img width="773" alt="image" src="https://github.com/user-attachments/assets/27ecaa71-39ee-4cb5-b3aa-02c263ad955f">

Neste momento os dados da base de dados foram criados manualmente.

### Manuseio das informações:

O manuseio das informações na base de dados é feito através de uma solução desenvolvida em Python.

Esta solução possui o seguinte menu de opções:

<img width="365" alt="image" src="https://github.com/user-attachments/assets/8088039d-7c55-429b-a5ac-0bfedb3cfa9b">


Bibliotecas adicionais para o código Python:

* import os

* import oracledb

* import pandas as pd

* from datetime import datetime

* from tabulate import tabulate

<!-- Análise de dados -->
## Análise de dados

Foram criados dois gráficos através da ferramenta R, mostrando algumas informações sobre o ambiente

![image](https://github.com/user-attachments/assets/654ce32a-6f9c-44f3-9b62-15f3d5871ae2)

![image](https://github.com/user-attachments/assets/a35a6226-84c2-4772-8a83-9c2f48ca14f5)



<!-- ROADMAP -->
## Roadmap
* Desenvolver outros tipos de relatórios.

<!-- CRIATION -->
## Criação:


Deniz Feital Armanhe (RM559439)- <img width="35" alt="image" src="https://github.com/user-attachments/assets/96a043d2-fe26-459e-96aa-577c929759be">
