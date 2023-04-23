from medico import Cardiologista, Dermatologista, Geral, Cirurgiao
from paciente import Paciente
from clinica import Clinica
from interface import Interface, Terminal

if __name__ == "__main__":
    Terminal.clear_terminal()
    clinica = Clinica()
    Interface.menuPrincipal()
    