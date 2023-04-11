from paciente import Paciente    
    
class Medico:

    especialidade = "Nenhuma"
    
    def __init__(self, matricula: int, nome: str, taxa:float) -> None:
        self.__matricula = matricula
        self.__nome = nome
        self.__taxa = taxa
        self.__taxaAjudante = 250.00
        self.__valorMedicamento = 50.00
        self.__valorEstudo = 125.00
        pass

    @property
    def matricula(self)->int:
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula:int):
        self.__matricula = matricula
    
    @property
    def nome(self)->str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome:str):
        self.__nome = nome

    @property
    def taxa(self)->float:
        return self.__taxa
    
    @taxa.setter
    def taxa(self, taxa:float):
        self.__taxa = taxa
        pass

    @property
    def taxaAjudante(self)->float:
        return self.__taxaAjudante
    
    @taxaAjudante.setter
    def taxaAjudante(self, taxaAjudante:float):
        self.__taxaAjudante = taxaAjudante

    @property
    def valorMedicamento(self)->float:
        return self.__valorMedicamento
    
    @valorMedicamento.setter
    def valorMedicamento(self, valorMedicamento: float):
        self.__valorMedicamento = valorMedicamento

    @property
    def valorEstudo(self):
        return self.__valorEstudo
    
    @valorEstudo.setter
    def valorEstudo(self, valorEstudo: float):
        self.__valorEstudo = valorEstudo

    def calcularHonorario(self, paciente:Paciente)->float:
        return -1.0

    def __str__(self) -> str:
        return "\nMatrícula: {0}\nNome: {1}\nEspecialidade: {2}\nTaxa: R$ {3}".format(self.matricula, self.nome, self.especialidade, self.taxa)
    
    def __repr__(self)->str:
        return "Medico({}, {}, {}, {}, {}, {})".format(self.matricula, self.nome, self.taxa, self.taxaAjudante, self.valorMedicamento, self.valorEstudo)
    
class Cardiologista(Medico):
    especialidade = "Cardiologia"
    def calcularHonorario(self, paciente: Paciente) -> float:
        return self.taxa + (self.valorEstudo * paciente.estudos)
    
class Cirurgiao(Medico):
    especialidade = "Cirurgia"
    def calcularHonorario(self, paciente: Paciente) -> float:
        return self.taxa + (self.taxaAjudante *2)

class Dermatologista(Medico):
    especialidade = "Dermatologia"
    def calcularHonorario(self, paciente: Paciente) -> float:
        return self.taxa + (self.valorMedicamento * paciente.medicamentos)
    
class Geral(Medico):
    especialidade = "Clínica-Geral"
    def calcularHonorario(self, paciente: Paciente) -> float:
        return self.taxa
    