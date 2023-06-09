from clinica import Clinica
from medico import Medico, Cardiologista, Cirurgiao, Dermatologista, Geral
import winsound as ws
from paciente import Paciente
import os

class Terminal:
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')
        pass
    def header():
        print()
        print("************************************************")
        print("*** Sistema de Registros - Clínica Dr. Lopes ***")
        print("************************************************")
        print("\n") 
        pass

class Interface:
    
    @staticmethod
    def filtrarSimNao(texto)->bool:
        if texto in ("Ss"):
            return True
        else:
            return False
    
    @staticmethod
    def menuPrincipal():
        msg=""
        while True:
            Terminal.clear_terminal()
            Terminal.header()
            print("************************************************")
            print(f"Menu Inicial\n"
                f"1 - Médicos\n"
                f"2 - Pacientes\n"
                f"3 - Administração\n"
                f"4 - Sair")
            print("************************************************")
            print(msg)
            try:
                ws.Beep(170, 400)
                input1 = (input(">> "))
                if input1.isnumeric() == False:
                    raise Exception("Insira somente números...")
                menu1 = int(input1)
                ws.Beep(670, 400)
                if menu1 < 1 or menu1 > 4:
                    ws.Beep(70, 400)
                    raise Exception("Opção Inválida.")
                if menu1 == 4:
                    break
                if menu1 == 1:
                    Interface.menuMedico()
                if menu1 == 2:
                    Interface.menuPaciente()
                if menu1 == 3:
                    Interface.menuAdministracao()
            except Exception as e:
                msg = str(e)
                continue

    @staticmethod   
    def menuMedico():
        Terminal.clear_terminal()
        Terminal.header()
        msg = ""
        while True:
            print(msg)
            print(f"Menu Médicos\n"
            f"1 - Cadastrar Médico\n"
            f"2 - Listar Médicos\n"
            f"3 - Voltar ao Menu anterior")
            try:
                input2 = (input(">> "))
                if input2.isnumeric() == False:
                    raise Exception("Insira somente números...")
                menu2 = int(input2)
                ws.Beep(170, 500)
                if menu2 < 1 or menu2 > 3:
                    raise Exception("Opção Inválida.")
                if menu2 == 3:
                    break
            except Exception as e:
                msg = str(e)
                continue
            
            if menu2 == 1:
                Terminal.clear_terminal()
                print("....Cadastrando Novo Médico....\n")
                ws.Beep(370, 400)
                matricula = int(input("Matricula:\n"))
                ws.Beep(370, 400)
                nome = input("Nome:\n")
                ws.Beep(370, 400)
                taxa = float(input("Taxa (em reais):\n"))
                especialidade = int(input("Especialidade:\n1. Cardiologista 2. Cirurgiao 3. Dermatologista 4. Geral\n>> "))
                if especialidade == 1:
                    medico = Cardiologista(matricula, nome, taxa)
                elif especialidade == 2:
                    medico = Cirurgiao(matricula, nome, taxa)
                elif especialidade == 3:
                    medico = Dermatologista(matricula, nome, taxa)
                elif especialidade == 4:
                    medico = Geral(matricula, nome, taxa)
                if especialidade in range(1,5):
                    Clinica.adicionarMedico(medico)
                    ws.Beep(670, 400)
                    print("\nMédico adicionado com sucesso!\n")
                continue
            if menu2 == 2:
                Clinica.imprimirListaMedicos()
                ws.Beep(370, 400)
                continue


    @staticmethod
    def menuPaciente():
        Terminal.clear_terminal()
        Terminal.header()
        msg = ""
        while True:
            print(msg)
            print(f"Menu Pacientes\n"
            f"1 - Cadastrar Paciente\n"
            f"2 - Listar Pacientes\n"
            f"3 - Solicitar Exames, Medicamentos e Cirurgia\n"
            f"4 - Voltar ao Menu anterior")
            try:
                ws.Beep(370, 400)
                input1 = (input(">> "))
                if input1.isnumeric() == False:
                    raise Exception("Insira somente números...")
                menu2 = int(input1)
                if menu2 < 1 or menu2 > 4:
                    raise Exception("Opção Inválida.")
                if menu2 == 4:
                    break
            except Exception as e:
                msg = str(e)
                
            
            if menu2 == 1:
                print("....Cadastrando Novo Paciente....\n")
                ws.Beep(370, 500)
                documento = input("Documento:\n")
                ws.Beep(370, 400)
                nome = input("Nome:\n")
                ws.Beep(370, 400)
                idade = int(input("Idade:\n"))
                ws.Beep(370, 400)
                cpf = input("CPF:\n")
                ws.Beep(370, 400)
                particular = Interface.filtrarSimNao(input("Particular (S)im ou (N)ão\n"))
                ws.Beep(370, 400)
                lista = "Médicos:\n"
                for x in Clinica.listaMedicos:
                    lista += "({0}) - {1} (Especialidade: {2})\n".format(x.matricula, x.nome, x.especialidade)
                medico = int(input(lista))
                paciente = Paciente(documento, nome, idade, cpf, particular, medico)
                Clinica.adicionarPaciente(paciente)
                ws.Beep(370, 400)
                print("\nPaciente cadastrado com sucesso!\n")
                ws.Beep(470, 500)
                continue
            if menu2 == 2:
                ws.Beep(370, 400)
                Clinica.imprimirListaPacientes()
                continue

            if menu2 == 3:
                print("....Solicitar Estudos, Medicamentos ou Cirurgia....\n")
                print("Insira documento do paciente:")
                ws.Beep(370, 400)
                documento = input(">> ")
                print("Insira tipo de solicitação: 1- Estudo, 2 - Medicamento, 3 - Cirurgia")
                ws.Beep(370, 400)
                solicitacao = int(input(">> "))
                for paciente in Clinica.listaPacientes:
                    if paciente.documento == documento:
                        if solicitacao == 1:
                            paciente.realizarEstudo()
                            ws.Beep(470, 400)
                            print("\nEstudo solicitado\n")
                        elif solicitacao == 2:
                            paciente.receberMedicamento()
                            ws.Beep(470, 400)
                            print("\nMedicamento Solicitado\n")
                        elif solicitacao == 3:
                            paciente.realizarCirurgia()
                            ws.Beep(470, 400)
                            print("\nCirurgia solicitada\n")
                        else:
                            print("\nErro de Solicitação\n")
                    else:
                        continue

    @staticmethod
    def menuAdministracao():
        Terminal.clear_terminal()
        Terminal.header()
        msg=""
        while True:
            print(msg)
            print(f"Menu Administracão\n"
            f"1 - Calculo de Honorários\n"
            f"2 - Alta paciente\n"
            f"3 - Pagamentos em Aberto\n"
            f"4 - Pagamentos Realizados\n"
            f"5 - Voltar ao menu anterior\n")
            try:
                menu2 = int(input(">> "))
                ws.Beep(370, 400)
                if menu2 < 1 or menu2 > 5:
                    raise Exception("Opção Inválida.")
                if menu2 == 5:
                    break
            except Exception as e:
                msg = str(e)
                
            
            if menu2 == 1:
                print("\n##### Honorários #####\n")
                ws.Beep(370, 500)
                print("Insira documento do paciente:")
                documento = input(">> ")
                ws.Beep(370, 400)
                found = False
                for paciente in Clinica.listaPacientes:
                    servico = not paciente.particular
                    if paciente.documento == documento:
                        for medico in Clinica.listaMedicos:
                            if medico.matricula == paciente.medico:
                                print(f"Honorários Devidos:\n"
                                      f"RS {paciente.pagamento(medico, servico):,.2f}\n"
                                      )
                        found = True
                if found == False:
                    print("Paciente não Encontrado")

            if menu2 == 2:
                print("\n##### Alta #####\n")
                print("Insira documento do paciente:")
                ws.Beep(370, 400)
                documento = input(">> ")
                found = False
                for paciente in Clinica.listaPacientes:
                    if paciente.documento == documento:
                        paciente.alta = True
                        print("\nPaciente recebeu alta no sistema com sucesso.\n")
                        ws.Beep(470, 500)
                        found = True
                    else:
                        continue
                if found == False:
                    print("Paciente não Encontrado")
                        
            
            if menu2 == 3:
                print("##### Pagamentos em Aberto #####\n")
                ws.Beep(370, 400)
                for paciente in Clinica.listaPacientes:
                    if paciente.alta == False:
                        print(paciente)
                        print()
                                
            if menu2 == 4:
                print("##### Pagamentos Realizados #####\n")
                ws.Beep(370, 400)
                for paciente in Clinica.listaPacientes:
                    if paciente.alta == True:
                        print(paciente)
                        print()
                        