from limite.tela_rede import TelaRede
from entidade.rede import Rede
from excecoes.lista_vazia_exception import ListaVaziaException
from excecoes.jah_existente_exception import JahExistenteException
from excecoes.nao_encontrado_exception import NaoEncontradoException
from persistence.rede_dao import RedeDao


class ControladorRede():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_rede = TelaRede()
        self.__rede_dao = RedeDao()
        
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def rede_dao(self):
        return self.__rede_dao

    def adicionar(self):
        dados_rede = self.__tela_rede.pega_dados_rede()
        try:
            if self.buscar_por_codigo(dados_rede["codigo"]):
                raise JahExistenteException("Rede", "codigo", dados_rede["codigo"])
            self.__rede_dao.add(
                Rede(dados_rede["nome"], dados_rede["codigo"],
                        dados_rede["localizacao_rede"]))
            self.__tela_rede.mostra_mensagem("Rede adicionada com sucesso!")
        except JahExistenteException as e:
            self.__tela_rede.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_rede.mostra_mensagem(str(e))

    def remover(self):
        if not self.listar():
            return
        
        codigo = self.__tela_rede.pega_codigo_rede()
        
        try:
            self.__rede_dao.remove(codigo)
            self.__tela_rede.mostra_mensagem("Removido com sucesso.")
        except NaoEncontradoException as e:
            self.__tela_rede.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_rede.mostra_mensagem(str(e))

    def buscar_por_codigo(self, codigo):
        return self.__rede_dao.get(codigo)

    def listar(self):
        try:
            lista_redes = self.__rede_dao.get_all()
            if not len(lista_redes) >= 1:
                    raise ListaVaziaException('redes')
            lista_dados_rede = map(
                lambda rede: {
                    "nome": rede.nome,
                    "localizacao_rede": rede.localizacao_rede,
                    "codigo": rede.codigo,
                    "hoteis": rede.hoteis
                }, lista_redes)

            self.__tela_rede.mostrar_redes(lista_dados_rede)
            return True
        except ListaVaziaException as e:
            self.__tela_rede.mostra_mensagem(str(e))
            return False

    def alterar(self):
        if not self.listar():
            return
        
        dados_rede = self.__tela_rede.pega_dados_rede_para_alteracao()
        
        try:
            rede = self.__rede_dao.get(dados_rede['codigo'])
            
            rede.nome = dados_rede["nome"]
            rede.nome = dados_rede["codigo"]
            rede.nome = dados_rede["localizacao_rede"]
            
            self.__rede_dao.update(rede)
            
            self.__tela_rede.mostra_mensagem("Alterado com sucesso.")
        except NaoEncontradoException as e:
            self.__tela_rede.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_rede.mostra_mensagem(str(e))


    def adicionar_hotel_em_rede(self):
        dados_inclusao = self.__tela_rede.pega_dados_inclusao_de_hotel()

        try:
            if (not len(self.__rede_dao.get_all()) or 
                    not len(self.__controlador_sistema.controlador_hotel.hotel_dao.get_all()) >= 1):
                raise Exception("Não pode ser adicionao hotel quando não existe hoteis ou redes")
            
            rede = self.buscar_por_codigo(dados_inclusao["codigo_rede"])
            hotel = self.__controlador_sistema.controlador_hotel.buscar_por_codigo(dados_inclusao["codigo_hotel"])
            
            if not rede:
                raise NaoEncontradoException("Rede", "codigo", dados_inclusao["codigo_rede"])
            if not hotel:
                raise NaoEncontradoException("Hotel", "codigo", dados_inclusao["codigo_hotel"])

            rede.adicionar_hotel(hotel)
            self.__tela_rede.mostra_mensagem("Hotel adicionado com sucesso.")
        except NaoEncontradoException as e:
            self.__tela_rede.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_rede.mostra_mensagem(str(e))

    def abre_tela(self):
        lista_opcoes = {
            1: self.adicionar,
            2: self.alterar,
            3: self.listar,
            4: self.remover,
            5: self.adicionar_hotel_em_rede,
            0: self.retornar
        }

        continua = True
        while continua:
            lista_opcoes[self.__tela_rede.tela_opcoes()]()

    def retornar(self):
        self.__controlador_sistema.abre_tela()
