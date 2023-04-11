class Paciente:

    def __init__(self, documento:str, nome:str, idade:int, cpf:str, particular:bool,medico:int = 0) -> None:
        self.__documento = documento 
        self.__nome = nome
        self.__idade = idade 
        self.__cpf = cpf 
        self.__particular = particular
        self.__medico = medico
        self.__cirurgia = False
        self.__alta = False
        self.__medicamentos = 0 
        self.__estudos = 0
        self.__quantidadeCirurgia = 0
        pass
    
    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self,documento):
        self.__documento = documento 
        
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self,idade):
        self.__idade = idade
        
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self,cpf):
        self.__cpf = cpf
        
    @property
    def particular(self):
        return self.__particular

    @particular.setter
    def particular(self,particular):
        self.__particular = particular
        
    @property
    def medico(self):
        return self.__medico

    @medico.setter
    def medico(self,medico):
        self.__medico = medico
        
    @property
    def cirurgia(self):
        return self.__cirurgia

    @cirurgia.setter
    def cirurgia(self, cirurgia):
        self.__cirurgia = cirurgia         
    @property
    def alta(self):
        return self.__alta

    @alta.setter
    def alta(self,alta):
        self.__alta = alta         
    
    @property
    def medicamentos(self):
        return self.__medicamentos

    @medicamentos.setter
    def medicamentos(self, medicamentos):
        self.__medicamentos =  medicamentos      

    @property
    def estudos(self):
        return self.__estudos

    @estudos.setter
    def estudos(self,estudos):
        self.__estudos =estudos 
            
    @property
    def quantidadeCirurgia(self):
        return self.__quantidadeCirurgia

    @quantidadeCirurgia.setter
    def quantidadeCirurgia(self,quantidadeCirurgia):
        self.__quantidadeCirurgia = quantidadeCirurgia
     
    def pagamento(self, medico,servicoSocial:bool)->float:
        from medico import Medico
        honorario = medico.calcularHonorario(self)
        if servicoSocial == True:
            return honorario/2
        return honorario
    
    def realizarEstudo(self):
        self.estudos += 1

    def receberMedicamento(self):
        self.medicamentos += 1

    def realizarCirurgia(self):
        self.cirurgia = True
        self.quantidadeCirurgia += 1

    def __str__(self) -> str:
        particular = "Não"
        if self.particular == True:
            particular = "Sim"
        return "== Paciente ==\nDocumento: {0}\nNome: {1}\nIdade:{2}\nCPF:{3}\nParticular:{4}\nMédico: {5}\nCirurgia Realizada: {6}\nAlta: {7}\nMedicamentos Recebidos: {8}\nEstudos Solicitados: {9}\nCirurgias Realizadas: {10}".format(self.documento, self.nome, self.idade, self.cpf, particular, self.medico, self.cirurgia, self.alta, self. medicamentos, self.estudos, self.quantidadeCirurgia)
    
    def __repr__(self):
        return "Paciente({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10})".format(self.documento, self.nome, self.idade, self.cpf, self.particular, self.medico, self.cirurgia, self.alta, self.medicamentos, self.estudos, self.quantidadeCirurgia)
