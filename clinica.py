from medico import Medico, Cardiologista, Dermatologista, Geral, Cirurgiao
from paciente import Paciente
import winsound as ws

class Clinica:
        
    listaMedicos = []
    listaPacientes = []

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
            print(f"\n {medico} \n")    
    
    @staticmethod
    def imprimirListaPacientes():
        for paciente in Clinica.listaPacientes:
            print(f"\n {paciente} \n")
