# Importação dos módulos
import os
import oracledb
import pandas as pd
from datetime import datetime
from tabulate import tabulate

today_date = datetime.today().date()
# Try para tentativa de Conexão com o Banco de Dados
try:
    # Efetua a conexão com o Usuário no servidor
    conn = oracledb.connect(user='rm559439', password="010170", dsn='oracle.fiap.com.br:1521/ORCL')
    # Cria as instruções para cada módulo
    inst_cadastro = conn.cursor()
    inst_consulta = conn.cursor()
    inst_alteracao = conn.cursor()
    inst_exclusao = conn.cursor()
except Exception as e:
    # Informa o erro
    print("Erro: ", e)
    # Flag para não executar a Aplicação
    conexao = False
else:
    # Flag para executar a Aplicação
    conexao = True 
margem = ' ' * 4 # Define uma margem para a exibição da aplicação

# Enquanto o flag conexao estiver como True
while conexao:
    # Limpa a tela via SO
    os.system('cls')

    # Apresenta o menu
    print("------- Farm Tech Solutions - Manutenção do ambiente -------")
    print("""
    Para a manutenção dos sensores:  
        
    1 - Cadastrar Sensor
    2 - Listar Sensor
    3 - Alterar Sensor
    4 - Excluir Sensor
    
    Para consultas gerais:
    
    5 - Consultar Solo
    6 - Consultar Humidade
    7 - Consultar Irrigacao
    
    Para sair do sistema:
    
    8 - Sair
    """)

    # Captura a escolha do usuário
    escolha = input(margem + "Escolha -> ")

    # Verifica se o número digitado é um valor numérico
    if escolha.isdigit():
        escolha = int(escolha)
    else:
        escolha = 8
        print("Digite um número.\nReinicie a Aplicação!")

    os.system('cls')  # Limpa a tela via SO

    # VERIFICA QUAL A ESCOLHA DO USUÁRIO
    match escolha:
        case 1:
            try:
                print("----- CADASTRAR SENSOR-----\n")
                # Recebe os valores para cadastro
                var_sensor_type = input("Digite o tipo....: ")
                var_status = input("Digite o status....: ")
                var_sensor_location = input("Digite a localização...: ")
                today_date = datetime.today().date()

                # Monta a instrução SQL de cadastro com parâmetros
                cadastro = """ 
                INSERT INTO tb_md3_sensors (sensor_type, installation_date, status, sensor_location)
                VALUES (:sensor_type, :installation_date, :status, :sensor_location)
                """

                # Define the data dictionary for the parameterized query
                data = {
                    "sensor_type": var_sensor_type,
                    "installation_date": today_date,
                    "status": var_status,
                    "sensor_location": var_sensor_location
                }

                # Execute and commit the record
                inst_cadastro.execute(cadastro, data)
                conn.commit()

            except ValueError:
                # Handle non-numeric input where numeric is expected
                print("Digite um número válido!")
            except Exception as e:
                # Handle any database connection or SQL errors
                print("Erro na transação do BD:", e)
            else:
                # Success message if the record was saved
                print("\n##### Dados GRAVADOS #####")

                # LISTAR TODOS OS PETS
        case 2:
            
            try:
                print("----- LISTAR OS SENSORES -----\n")

                num_records = int(input("Quantos registros quer ver nesta amostragem? "))
                query = f"SELECT * FROM TB_MD3_Sensors FETCH FIRST {num_records} ROWS ONLY"
                inst_cadastro.execute(query)
                sensors = inst_cadastro.fetchall()
                headers = ["Sensor ID", "Sensor Type", "Installation Date", "Status", "Sensor Location"]

                if sensors:
                    print(tabulate(sensors, headers=headers, tablefmt="grid"))
                else:
                    print("No sensors found.")

            except Exception as e:
                print("Erro ao listar os sensores:", e)
            finally:
                pass
                    # ALTERAR OS DADOS DE UM REGISTRO
        case 3:
            try:
                print("----- ATUALIZAR SENSOR -----\n")
                var_sensor_id = int(input("Digite o Sensor ID para atualizar: "))

                check_query = "SELECT COUNT(*) FROM TB_MD3_Sensors WHERE sensor_id = :sensor_id"
                inst_cadastro.execute(check_query, {"sensor_id": var_sensor_id})
                result = inst_cadastro.fetchone()

                if result[0] == 0:
                    print(f"Sensor ID {var_sensor_id} não encontrado!")
                else:
                    # Recebe os novos valores para o sensor
                    var_sensor_type = input("Digite o tipo....: ")
                    var_status = input("Digite o status....: ")
                    var_sensor_location = input("Digite a localização...: ")
                    today_date = datetime.today().date()

                    # Monta a instrução SQL para atualizar os dados
                    update_query = """
                    UPDATE TB_MD3_Sensors
                    SET sensor_type = :sensor_type, 
                        installation_date = :installation_date,
                        status = :status,
                        sensor_location = :sensor_location
                    WHERE sensor_id = :sensor_id
                    """

                    # Dados para passar para a query
                    data = {
                        "sensor_type": var_sensor_type,
                        "installation_date": today_date,
                        "status": var_status,
                        "sensor_location": var_sensor_location,
                        "sensor_id": var_sensor_id
                    }

                    # Executa a atualização
                    inst_cadastro.execute(update_query, data)
                    conn.commit()

                    print("\n##### Dados ATUALIZADOS #####")

            except ValueError:
                # Erro de tipo de dado, por exemplo, se o ID não for um número
                print("Digite um número válido para o Sensor ID!")
            except Exception as e:
                # Erro de conexão ou SQL
                print("Erro ao atualizar o sensor:", e)
        case 4:
            try:
                print("----- EXCLUIR SENSOR -----\n")
                
                # Recebe o Sensor_ID para localizar o sensor
                var_sensor_id = int(input("Digite o Sensor ID para excluir: "))

                # Check if the sensor exists
                check_query = "SELECT COUNT(*) FROM TB_MD3_Sensors WHERE sensor_id = :sensor_id"
                inst_cadastro.execute(check_query, {"sensor_id": var_sensor_id})
                result = inst_cadastro.fetchone()

                # If the count is 0, the sensor does not exist
                if result[0] == 0:
                    print(f"Sensor ID {var_sensor_id} não encontrado!")
                else:
                    # Prompt to confirm deletion
                    confirm = input(f"Tem certeza de que deseja excluir o Sensor ID {var_sensor_id}? (s/n): ")
                    if confirm.lower() == 's':
                        # Monta a instrução SQL para excluir o sensor
                        delete_query = "DELETE FROM TB_MD3_Sensors WHERE sensor_id = :sensor_id"

                        # Executa a exclusão
                        inst_cadastro.execute(delete_query, {"sensor_id": var_sensor_id})
                        conn.commit()

                        print(f"\n##### Sensor ID {var_sensor_id} EXCLUÍDO #####")
                    else:
                        print("Exclusão cancelada.")

            except ValueError:
                # Erro de tipo de dado, por exemplo, se o ID não for um número
                print("Digite um número válido para o Sensor ID!")
            except Exception as e:
                # Erro de conexão ou SQL
                print("Erro ao excluir o sensor:", e)

        case 5:
            try:
                num_records = int(input("Quantos registros quer ver nesta amostragem? "))

                query = f"""
                SELECT n.nutrient_name, c.collection_value
                FROM tb_md3_nutrient_collection c
                JOIN tb_md3_nutrients n ON c.nutrient_type = n.nutrient_id
                FETCH FIRST {num_records} ROWS ONLY
                """
                inst_cadastro = conn.cursor()
                inst_cadastro.execute(query)
                records = inst_cadastro.fetchall()

                if records:
                    print(f"\nMostrando {num_records} registros(s) do solo:")
                    print(" ")
                    print(f"{'Nutriente':<20}{'Valor coletado':<15}")  
                    print(" ")
                    for row in records:
                        print(f"{row[0]:<20}{row[1]:<15}") 
                else:
                    print("Nenhum registro encontrado.")
            
            except Exception as e:
                print("Error:", e)

        case 6:
            try:
                num_records = int(input("Quantos registros quer ver nesta amostragem? "))
                query = f"""
                SELECT tb_sensors_sensor_id, humidity_value, TO_CHAR(reading_timestamp, 'YYYY-MM-DD HH24:MI:SS')
                FROM tb_md3_humidity_readings
                FETCH FIRST {num_records} ROWS ONLY
                """
                inst_cadastro = conn.cursor()
                inst_cadastro.execute(query)
                records = inst_cadastro.fetchall()

                if records:
                    print(f"Mostrando {num_records} registro(s) de humidade:")
                    print(" ")
                    print(f"{'Sensor ID':<15}{'Humidade':<15}{'Horário de leitura':<25}")
                    print(" ")
                    for row in records:
                        print(f"{row[0]:<15}{row[1]:<15}{row[2]:<25}") 
                else:
                    print(f"Nenhum registro encontrado.")
            
            except Exception as e:
                print("Error:", e)

        case 7:
            try:
                num_records = int(input("Quantos registros quer ver nesta amostragem? "))

                query = f"""
                SELECT tb_sensors_sensor_id, TO_CHAR(irrigation_time, 'YYYY-MM-DD HH24:MI:SS'), duration
                FROM tb_md3_irrigation_events
                FETCH FIRST {num_records} ROWS ONLY
                """
                inst_cadastro = conn.cursor()
                inst_cadastro.execute(query)
                records = inst_cadastro.fetchall()
                if records:
                    print(f"\nMostrando {num_records} registro(s) de irrigação:")
                    print(" ")
                    print(f"{'Sensor ID':<15}{'Hora da irrigação':<25}{'Duracao em minutos':<20}")
                    print(" ")
                    for row in records:
                        duration_value = row[2] if row[2] else 'N/A' 
                        print(f"{row[0]:<15}{row[1]:<25}{duration_value:<20}") 
                else:
                    print(f"Nenhum registro encontrado.")
            
            except Exception as e:
                print("Error:", e)

            # SAI DA APLICAÇÃO
        case 8:
            
            conexao = False

        case _:
            input(margem + "Digite um número entre 1 e 8.")

    input(margem + "Pressione ENTER")
else:
    print("")
    print("Obrigado por utilizar a nossa aplicação! :)")
    print("")