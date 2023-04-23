from medico import Medico, Cardiologista, Dermatologista, Geral, Cirurgiao
from paciente import Paciente

class Clinica:
        
    listaMedicos = []
    listaPacientes = []

    def __init__(self) -> None:
        medico1 = Cardiologista(1, "Marcos", 700.00)
        medico2 = Cirurgiao(2, "Ana", 1500)
        medico3 = Dermatologista(3, "Joana", 700)
        medico4 = Geral(4, "Fernando", 400)
        paciente1 = Paciente("11", "João", 34, "004.002.442-24", True, 1)
        paciente2 = Paciente("22", "Fernando", 44, "0349024902", False, 2)
        paciente3 = Paciente("33", "Luiza", 25, "20390239", False, 3)
        paciente3 = Paciente("44", "Luiza", 25, "20390239", False, 4)
        Clinica.adicionarMedico(medico1)
        Clinica.adicionarMedico(medico2)
        Clinica.adicionarMedico(medico3)
        Clinica.adicionarMedico(medico4)
        Clinica.adicionarPaciente(paciente1)
        Clinica.adicionarPaciente(paciente2)
        Clinica.adicionarPaciente(paciente3)

    @staticmethod
    def adicionarMedico(medico):
        Clinica.listaMedicos.append(medico)
        pass

    @staticmethod
    def adicionarPaciente(paciente):
        Clinica.listaPacientes.append(paciente)
        pass

    @staticmethod
    def imprimirListaMedicos():
        for medico in Clinica.listaMedicos:
            print(f"{medico} \n")    
    
    @staticmethod
    def imprimirListaPacientes():
        for paciente in Clinica.listaPacientes:
            print(f"{paciente} \n")

    @staticmethod
    def carregarArquivo():
        pass

    @staticmethod
    def salvarArquivo():
        pass


        