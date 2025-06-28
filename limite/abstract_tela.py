from abc import ABC, abstractmethod
import datetime
import PySimpleGUI as sg


class AbstractTela(ABC):
    ESTILO_JANELA = 'DarkGrey7'
    TITULO_BASE = 'Genrenciamento de Hoteis e Redes'
    
    def __validar_input_numerico(self, values: dict, chave: str, campo_legivel: str) -> bool:
        valor = values.get(chave, "").strip()
        try:
            int(valor)
            return True
        except ValueError:
            self.mostra_mensagem(f"O campo '{campo_legivel}' deve conter apenas números.", "erro")
            return False
    
    def __validar_input_obrigatorio(self, values: dict, chave: str, campo_legivel: str) -> bool:
        valor = values.get(chave, "").strip()
        try:
            if valor == '':
                raise Exception(f"O campo '{campo_legivel}' é obrigatório.")
            return True
        except Exception as e:
            self.mostra_mensagem(e, "erro")
            return False
    
    def __validar_data(self, values: dict, chave: str, campo_legivel: str, formato="%d-%m-%Y") -> bool:
        valor = values.get(chave, "").strip()
        try:
            datetime.datetime.strptime(valor, formato)
            return True
        except ValueError:
            self.mostra_mensagem(f"Data inválida no campo '{campo_legivel}'. Formato esperado: {formato}", "erro")
            return False
        
    def __validar_input_float(self, values: dict, chave: str, campo_legivel: str) -> bool:
        valor = values.get(chave, "").strip()
        try:
            float(valor)
            return True
        except ValueError as e:
            self.mostra_mensagem(f"O campo '{campo_legivel}' deve conter apenas números.", "erro")
            return False

    def __validar_input_cpf(self, values: dict, chave: str, campo_legivel: str) -> bool:
        valor = values.get(chave, "").strip()
        try:
            int(valor)
            if len(valor) != 11:
                raise ValueError
            return True
        except ValueError:
            self.mostra_mensagem(f"Valor incorreto! Formato esperado para '{campo_legivel}' deve conter exatamente 11 digitos.", "erro")
            return False
            
    def __validar_input_telefone(self, values: dict, chave: str, campo_legivel: str) -> bool:
        valor = values.get(chave, "").strip()
        try:
            int(valor)
            if len(valor) != 11:
                raise ValueError
            return True
        except ValueError:
            self.mostra_mensagem(f"Valor incorreto! Formato esperado para '{campo_legivel}' deve conter exatamente 11 digitos e sem espaços.\n Exemplo: 47988303706", "erro")
            return False
        
    def _validar_campos(self, values: dict, regras: list[tuple]) -> bool:
        for tipo, chave, campo_legivel in regras:
            if tipo.lower() == "obrigatorio" and not self.__validar_input_obrigatorio(values, chave, campo_legivel):
                return False
            elif tipo.lower() == "numero" and not self.__validar_input_numerico(values, chave, campo_legivel):
                return False
            elif tipo.lower() == "float" and not self.__validar_input_float(values, chave, campo_legivel):
                return False
            elif tipo.lower() == "cpf" and not self.__validar_input_cpf(values, chave, campo_legivel):
                return False
            elif tipo.lower() == "telefone" and not self.__validar_input_telefone(values, chave, campo_legivel):
                return False
            elif tipo.lower() == "data" and not self.__validar_data(values, chave, campo_legivel):
                return False
        return True
    
    def _extrair_valor(self, values: dict, chave: str) -> str:
        return values.get(chave, "").strip()
    
    def mostra_mensagem(self, mensagem: str, tipo: str = "info"):
        if tipo.lower() == "erro":
            sg.popup_error(mensagem, title="Erro")
        elif tipo.lower() == "sucesso":
            sg.popup_ok(mensagem, title="Sucesso")
        elif tipo.lower() == "aviso":
            sg.popup_yes_no(mensagem, title="Atenção")
        else:
            sg.popup(mensagem, title="Mensagem")

    @abstractmethod
    def tela_opcoes(self):
        pass
    
    # @abstractmethod
    # def init_opcoes(self):
    #     pass
    
    # @abstractmethod
    # def close(self):
    #     pass
