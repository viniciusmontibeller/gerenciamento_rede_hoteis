from entidade.reserva import Reserva
from limite.tela_reserva import TelaReserva


class ControladorReserva():

    def __init__(self, controlador_sistema):
        self.__reservas = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_reserva = TelaReserva()
        
    @property
    def reservas(self):
        return self.__reservas
        
    def __verificar_quarto_disponivel_em_hotel(self, hotel, quarto, data_entrada, data_saida):
        for reserva in self.__reservas:
            if reserva.hotel.codigo == hotel.codigo and reserva.quarto.numero == quarto.numero:
                if (data_entrada <= reserva.data_saida) and (data_saida >= reserva.data_entrada):
                    return False
        return True
    
    def calcular_custo(self, reserva: Reserva):
        return reserva.quarto.preco_diaria * (reserva.data_saida - reserva.data_entrada).days

    def adicionar(self):
        codigo_reserva = self.__tela_reserva.pega_codigo_reserva()
        dados_reserva = self.__tela_reserva.pega_dados_reserva()

        try:
            if self.buscar_por_codigo(codigo_reserva):
                raise Exception("Reserva já existente")

            hotel = self.__controlador_sistema.controlador_hotel.buscar_por_codigo(dados_reserva["codigo_hotel"])
            if hotel is None:
                raise Exception("Hotel não encontrado")
            
            quarto = hotel.busca_quarto_por_numero(dados_reserva["codigo_quarto"])
            if quarto is None:
                raise Exception("Quarto não encontrado")
            if not self.__verificar_quarto_disponivel_em_hotel(hotel, quarto, dados_reserva["data_entrada"], dados_reserva["data_saida"]):
                raise Exception("Esse quarto ja possui reserva nesse periodo")
            
            cliente = self.__controlador_sistema.controlador_hotel.controlador_cliente.busca_por_cpf(hotel, dados_reserva["cpf_cliente"])
            if cliente is None:
                raise Exception("Cliente não encontrado")

            funcionario = self.__controlador_sistema.controlador_hotel.controlador_funcionario.busca_por_cpf(hotel, dados_reserva["cpf_funcionario"])
            if funcionario is None:
                raise Exception("Funcionário não encontrado")
            
            reserva = Reserva(codigo_reserva, hotel, quarto, cliente, funcionario, dados_reserva["data_entrada"], dados_reserva["data_saida"])
            reserva.custo = self.calcular_custo(reserva)

            self.__reservas.append(reserva)
            self.__tela_reserva.mostra_mensagem("Reserva adicionada com sucesso")
        except Exception as e:
            self.__tela_reserva.mostra_mensagem(str(e))

    def remover(self):
        self.listar()
        try:
            if not len(self.__reservas) >= 1:
                raise Exception("Não existe nenhuma resrva para ser removida")
            codigo = self.__tela_reserva.pega_codigo_reserva()
            reserva_existe = False

            for reserva in self.__reservas:
                if reserva.codigo == codigo:
                    self.__reservas.remove(reserva)
                    self.__tela_reserva.mostra_mensagem("Removido com sucesso.")

                    reserva_existe = True

                    break

            if not reserva_existe:
                raise Exception(
                    f"Reserva de código [{codigo}] não foi encontrada para ser removida."
                )
        except Exception as e:
            self.__tela_reserva.mostra_mensagem(str(e))

    def buscar_por_codigo(self, codigo):
        for reserva in self.__reservas:
            if reserva.codigo == codigo:
                return reserva

        return None

    def listar(self):
        lista_dados_reserva = map(
            lambda reserva: {
                "codigo": reserva.codigo,
                "cliente": reserva.cliente.nome,
                "hotel": reserva.hotel.nome,
                "quarto": reserva.quarto.numero,
                "funcionario": reserva.funcionario.nome,
                "data_entrada": reserva.data_entrada,
                "data_saida": reserva.data_saida,
                "status": reserva.status,
                "custo": reserva.custo
            }, self.__reservas)

        self.__tela_reserva.mostrar_reservas(lista_dados_reserva)

    def alterar(self):
        self.listar()

        try:
            if not len(self.__reservas) >= 1:
                raise Exception("Não existe nenhuma reserva para ser alterada")
            codigo = self.__tela_reserva.pega_codigo_reserva()
            reserva = self.buscar_por_codigo(codigo)
            if reserva is None:
                raise Exception("Reserva não encontrada")

            dados_reserva = self.__tela_reserva.pega_dados_reserva()
            
            hotel = self.__controlador_sistema.controlador_hotel.buscar_por_codigo(dados_reserva["codigo_hotel"])
            if hotel is None:
                raise Exception("Hotel não encontrado")
            
            quarto = hotel.busca_quarto_por_numero(dados_reserva["codigo_quarto"])
            if quarto is None:
                raise Exception("Quarto não encontrado")
            if not self.__verificar_quarto_disponivel_em_hotel(hotel, quarto, dados_reserva["data_entrada"], dados_reserva["data_saida"]):
                raise Exception("Esse quarto ja possui reserva nesse periodo")
            
            cliente = self.__controlador_sistema.controlador_hotel.controlador_cliente.busca_por_cpf(hotel, dados_reserva["cpf_cliente"])
            if cliente is None:
                raise Exception("Cliente não encontrado")

            funcionario = self.__controlador_sistema.controlador_hotel.controlador_funcionario.busca_por_cpf(hotel, dados_reserva["cpf_funcionario"])
            if funcionario is None:
                raise Exception("Funcionário não encontrado")
            
            reserva.hotel = hotel
            reserva.quarto = quarto
            reserva.cliente = cliente
            reserva.funcionario = funcionario
            reserva.data_entrada = dados_reserva["data_entrada"]
            reserva.data_saida = dados_reserva["data_saida"]
            reserva.custo = self.calcular_custo(reserva)

            self.__tela_reserva.mostra_mensagem("Alterado com sucesso.")
        except Exception as e:
            self.__tela_reserva.mostra_mensagem(str(e))

    def listar_reservas_por_hotel(self, codigo_hotel):
        hotel = self.__controlador_sistema.controlador_hotel.buscar_por_codigo(codigo_hotel)
        if hotel is None:
            raise Exception("Hotel não encontrado") 
        
        lista_reservas = [reserva for reserva in self.__reservas if reserva.hotel == hotel]

        return lista_reservas

    def abre_tela(self):
        lista_opcoes = {
            1: self.adicionar,
            2: self.alterar,
            3: self.listar,
            4: self.remover,
            0: self.retornar
        }

        continua = True
        while continua:
            lista_opcoes[self.__tela_reserva.tela_opcoes()]()
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()    