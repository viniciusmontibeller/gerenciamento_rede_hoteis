from enum import Enum


class StatusReserva(Enum):

    AGENDADO = "AGENDADO"
    CHECKIN = "CLIENTE FEZ CHECKIN"
    FINALIZADO = "CLIENTE FEZ CHECKOUT"
    CANCELADO = "CANCELADO"
