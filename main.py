from medico import Medico, Cardiologista, Dermatologista, Geral, Cirurgiao
from paciente import Paciente
from clinica import Clinica


if __name__ == "__main__":
    
    print("Inicializando classe principal...")
    clinica = Clinica()

    print("Populando cadastro com exemplos de médicos e pacientes...")
    medico1 = Cardiologista(1, "Marcos", 700.00)
    medico2 = Cirurgiao(2, "Ana", 1500)
    medico3 = Dermatologista(3, "Joana", 700)
    medico4 = Geral(4, "Fernando", 400)
    paciente1 = Paciente("11", "João", 34, "004.002.442-24", True, 1)
    paciente2 = Paciente("22", "Fernando", 44, "0349024902", False, 2)
    paciente3 = Paciente("33", "Luiza", 25, "20390239", False, 3)
    paciente3 = Paciente("44", "Luiza", 25, "20390239", False, 4)
    clinica.adicionarMedico(medico1)
    clinica.adicionarMedico(medico2)
    clinica.adicionarMedico(medico3)
    clinica.adicionarMedico(medico4)
    clinica.adicionarPaciente(paciente1)
    clinica.adicionarPaciente(paciente2)
    clinica.adicionarPaciente(paciente3)

    print("\n\n\n")
    print("************************************************")
    print("*** Sistema de Registros - Clínica Dr. Lopes ***")
    print("************************************************")
    print("\n\n")

    while True:
        print("************************************************")
        print(f"\nMenu Inicial\n"
            f"1 - Médicos\n"
            f"2 - Pacientes\n"
            f"3 - Administração\n"
            f"4 - Sair")
        print("************************************************")
        #try:
        menu1 = int(input(">> "))
        if menu1 < 1 or menu1 > 4:
            raise Exception("Opção Inválida.")
        if menu1 == 4:
            break
        if menu1 == 1:
            clinica.menuMedico()
        if menu1 == 2:
            clinica.menuPaciente()
        if menu1 == 3:
            clinica.menuAdministracao()
        #except:
        print(str(Exception))