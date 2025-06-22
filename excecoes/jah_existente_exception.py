class JahExistenteException(Exception):

    def __init__(self, nome_obj_nao_encontrado: str, identificador: str, numero_indentificador):
        self.mensagem = f'{nome_obj_nao_encontrado.capitalize()} com {identificador} {numero_indentificador} já existe. '
        super().__init__(self.mensagem)