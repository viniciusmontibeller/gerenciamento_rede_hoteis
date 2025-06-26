from entidade.reserva import Reserva
from limite.tela_reserva import TelaReserva
from excecoes.nao_encontrado_exception import NaoEncontradoException
from excecoes.quarto_possui_reserva_no_periodo_exception import QuartoPossuiReservaNoPeriodo
from excecoes.lista_vazia_exception import ListaVaziaException
from excecoes.jah_existente_exception import JahExistenteException
from persistence.reserva_dao import ReservaDAO


class ControladorReserva():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_reserva = TelaReserva()
        self.__reserva_dao = ReservaDAO()
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
    
    @property
    def reserva_dao(self):
        return self.__reserva_dao
        
    def __verificar_quarto_disponivel_em_hotel(self, hotel, quarto, data_entrada, data_saida):
        for reserva in self.__reserva_dao.get_all():
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
            if not (self.__controlador_sistema.controlador_hotel.hotel_dao.get_all()) >= 1:
                raise Exception("Não existem hoteis para cadastrar uma reserva")
            
            if self.buscar_por_codigo(codigo_reserva):
                raise JahExistenteException("Reserva", "codigo", codigo_reserva)

            hotel = self.__controlador_sistema.controlador_hotel.buscar_por_codigo(dados_reserva["codigo_hotel"])
            if hotel is None:
                raise NaoEncontradoException("Hotel", "codigo", dados_reserva["codigo_hotel"])
            
            if not len(hotel.funcionarios) >= 1:
                raise Exception("Não existem funcionarios nesse hotel para cadastrar uma reserva")
            if not len(hotel.clientes) >= 1:
                raise Exception("Não existem clientes nesse hotel para cadastrar uma reserva")
            if not len(hotel.clientes) >= 1:
                raise Exception("Não existem quartos nesse hotel para cadastrar uma reserva")
            
            quarto = hotel.busca_quarto_por_numero(dados_reserva["numero_quarto"])
            if quarto is None:
                raise NaoEncontradoException("quarto", "numero", dados_reserva["numero_quarto"])
            if not self.__verificar_quarto_disponivel_em_hotel(hotel, quarto, dados_reserva["data_entrada"], dados_reserva["data_saida"]):
                raise QuartoPossuiReservaNoPeriodo(dados_reserva["data_entrada"], dados_reserva["data_saida"])
            
            cliente = hotel.busca_cliente_por_cpf(dados_reserva["cpf_cliente"])
            if cliente is None:
                raise NaoEncontradoException("cliente", "CPF", dados_reserva["cpf_cliente"])

            funcionario = hotel.busca_funcionario_por_cpf(dados_reserva["cpf_funcionario"])
            if funcionario is None:
                raise NaoEncontradoException("funcionario", "CPF", dados_reserva["cpf_funcionario"])
            
            reserva = Reserva(codigo_reserva, hotel, quarto, cliente, funcionario, dados_reserva["data_entrada"], dados_reserva["data_saida"])
            reserva.custo = self.calcular_custo(reserva)

            self.__reserva_dao.add(reserva)
            self.__tela_reserva.mostra_mensagem("Reserva adicionada com sucesso")
        except NaoEncontradoException as e:
            self.__tela_reserva.mostra_mensagem(str(e))
        except QuartoPossuiReservaNoPeriodo as e:
            self.__tela_reserva.mostra_mensagem(str(e))
        except JahExistenteException as e:
            self.__tela_reserva.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_reserva.mostra_mensagem(str(e))

    def remover(self):
        if not self.listar():
            return
        
        codigo = self.__tela_reserva.pega_codigo_reserva()
        
        try:
            self.__reserva_dao.remove(codigo)
            self.__tela_reserva.mostra_mensagem("Removido com sucesso.")
        except NaoEncontradoException as e:
            self.__tela_reserva.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_reserva.mostra_mensagem(str(e))

    def buscar_por_codigo(self, codigo):
        return self.__reserva_dao.get(codigo)

    def listar(self):
        try:
            lista_reservas = self.__reserva_dao.get_all()
            if not len(lista_reservas) >= 1:
                raise ListaVaziaException("reservas")
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
                }, lista_reservas)

            self.__tela_reserva.mostrar_reservas(lista_dados_reserva)
            return True
        except ListaVaziaException as e:
            self.__tela_reserva.mostra_mensagem(str(e))
            return False

    def alterar(self):
        if not self.listar():
            return

        codigo = self.__tela_reserva.pega_codigo_reserva()
        
        try:
            reserva = self.buscar_por_codigo(codigo)
            if reserva is None:
                raise NaoEncontradoException("reserva", "codigo", codigo)

            dados_reserva = self.__tela_reserva.pega_dados_reserva()
            
            hotel = self.__controlador_sistema.controlador_hotel.buscar_por_codigo(dados_reserva["codigo_hotel"])
            if hotel is None:
                raise NaoEncontradoException("Hotel", "codigo", dados_reserva["codigo_hotel"])
            
            quarto = hotel.busca_quarto_por_numero(dados_reserva["numero_quarto"])
            if quarto is None:
                raise NaoEncontradoException("quarto", "numero", dados_reserva["numero_quarto"])
            if not self.__verificar_quarto_disponivel_em_hotel(hotel, quarto, dados_reserva["data_entrada"], dados_reserva["data_saida"]):
                raise QuartoPossuiReservaNoPeriodo(dados_reserva["data_entrada"], dados_reserva["data_saida"])
            
            cliente = hotel.busca_cliente_por_cpf(dados_reserva["cpf_cliente"])
            if cliente is None:
                raise NaoEncontradoException("cliente", "CPF", dados_reserva["cpf_cliente"])

            funcionario = hotel.busca_funcionario_por_cpf(dados_reserva["cpf_funcionario"])
            if funcionario is None:
                raise NaoEncontradoException("funcionario", "CPF", dados_reserva["cpf_funcionario"])
            
            reserva.hotel = hotel
            reserva.quarto = quarto
            reserva.cliente = cliente
            reserva.funcionario = funcionario
            reserva.data_entrada = dados_reserva["data_entrada"]
            reserva.data_saida = dados_reserva["data_saida"]
            reserva.custo = self.calcular_custo(reserva)
            
            self.__reserva_dao.update(reserva)

            self.__tela_reserva.mostra_mensagem("Alterado com sucesso.")
        except NaoEncontradoException as e:
            self.__tela_reserva.mostra_mensagem(str(e))
        except QuartoPossuiReservaNoPeriodo as e:
            self.__tela_reserva.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_reserva.mostra_mensagem(str(e))

    def listar_reservas_por_hotel(self, codigo_hotel):
        hotel = self.__controlador_sistema.controlador_hotel.buscar_por_codigo(codigo_hotel)
        if hotel is None:
            raise Exception("Hotel não encontrado") 
        
        lista_reservas = [reserva for reserva in self.__reserva_dao.get_all() if reserva.hotel == hotel]

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