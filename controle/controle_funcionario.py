from limite.tela_funcionario import TelaFuncionario
from entidade.funcionario import Funcionario


class ControladorFuncionario():

    def __init__(self, controlador_hotel):
        self.__controlador_hotel = controlador_hotel
        self.__tela_funcionario = TelaFuncionario()

    def adicionar(self):
        try: 
            codigo_hotel = self.__tela_funcionario.pega_codigo_hotel()
            dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()
            hotel = self.__controlador_hotel.busca_hotel_por_codigo(codigo_hotel)
        
            if self.busca_por_cpf(hotel, dados_funcionario["cpf"]):
                raise Exception("Funcionario ja existente")
            hotel.funcionarios.append(
                Funcionario(dados_funcionario["nome"],
                            dados_funcionario["cpf"],
                            dados_funcionario["telefone"],
                            dados_funcionario["email"]))
            self.__tela_funcionario.mostra_mensagem("Funcionario adicionado com sucesso!")
        except Exception as e:
            self.__tela_funcionario.mostra_mensagem(str(e))

    def remover(self):
        codigo_hotel = self.__tela_funcionario.pega_codigo_hotel()
        cpf = self.__tela_funcionario.pega_cpf_funcionario()
        try:
            funcionario_existe = False
            for funcionario in self.__controlador_hotel.busca_hotel_por_codigo(codigo_hotel).funcionarios:
                if funcionario.cpf == cpf:
                    self.__controlador_hotel.busca_hotel_por_codigo(codigo_hotel).funcionarios.remove(funcionario)
                    self.__tela_funcionario.mostra_mensagem("Removido com sucesso.")
                    funcionario_existe = True
                    break

            if not funcionario_existe:
                raise Exception(
                    f"Funcionario com cpf [{cpf}] não foi encontrada para ser removida."
                )
        except Exception as e:
            self.__tela_funcionario.mostra_mensagem(str(e))

    def listar(self, codigo_hotel = None):
        try:
            if not codigo_hotel:
                codigo_hotel = self.__tela_funcionario.pega_codigo_hotel()
            
            lista_dados_funcionario = map(
                lambda funcionario: {
                    "nome": funcionario.nome,
                    "cpf": funcionario.cpf,
                    "telefone": funcionario.telefone,
                    "email": funcionario.email
                }, self.__controlador_hotel.busca_hotel_por_codigo(codigo_hotel).funcionarios)
            
            self.__tela_funcionario.mostrar_funcionarios(lista_dados_funcionario)
        except Exception as e:
            self.__tela_funcionario.mostra_mensagem(str(e))

    def alterar(self):
        codigo_hotel = self.__tela_funcionario.pega_codigo_hotel()
        self.listar(codigo_hotel)

        dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()

        try:
            funcionario_existe = False
            for funcionario in self.__controlador_hotel.busca_hotel_por_codigo(codigo_hotel).funcionarios:
                if funcionario.cpf == dados_funcionario["cpf"]:
                    funcionario.nome = dados_funcionario["nome"]
                    funcionario.telefone = dados_funcionario["telefone"]
                    funcionario.email = dados_funcionario["email"]
                    self.__tela_funcionario.mostra_mensagem("Alterado com sucesso.")
                    funcionario_existe = True
                    break

            if not funcionario_existe:
                raise Exception(
                    f"Funcionario de cpf [{dados_funcionario['cpf']}] não foi encontrada."
                )
        except Exception as e:
            self.__tela_funcionario.mostra_mensagem(str(e))

    def busca_por_cpf(self, hotel, cpf):
        for funcionario in hotel.funcionarios:
            if funcionario.cpf == cpf:
                return funcionario

        return None

    def retornar(self):
        self.__controlador_hotel.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.adicionar,
            2: self.alterar,
            3: self.listar,
            4: self.remover,
            0: self.retornar
        }

        while True:
            lista_opcoes[self.__tela_funcionario.tela_opcoes()]()
