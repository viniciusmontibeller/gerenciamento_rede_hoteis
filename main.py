from cliente import Cliente
from funcionario import Funcionario
from quarto_normal import QuartoNormal
from quarto_vip import QuartoVip
from hotel import Hotel
from rede import Rede
from reserva import Reserva

cliente1 = Cliente("Maria Silva", "123.456.789-00", "11 91234-5678",
                   "maria@email.com")
funcionario1 = Funcionario("João Pedro", "987.654.321-00", "11 99876-5432",
                           "joao@email.com")

quarto1 = QuartoNormal(101, 2, 150.0)
quarto2 = QuartoVip(201, 4, 300.0)

hotel1 = Hotel("Hotel Central", 1, "Rua das Flores, 123", "11 1234-5678")
hotel1.adicionar_quarto(quarto1.numero, quarto1.capacidade,
                        quarto1.preco_diaria, False)
hotel1.adicionar_quarto(quarto2.numero, quarto2.capacidade,
                        quarto2.preco_diaria, True)

rede1 = Rede("Rede Confort", "12.345.678/0001-90", "São Paulo", [])
rede1.adicionar_hotel(hotel1)

reserva1 = Reserva(1, cliente1, quarto1, funcionario1)

print(reserva1.consultar_reserva())

reserva1.checkin()
print("\nApós check-in:")
print(reserva1.consultar_reserva())

reserva1.checkout()
print("\nApós check-out:")
print(reserva1.consultar_reserva())
print(f"Valor total a pagar: R${reserva1.custo}")

reserva1.cancelar()
print("\nApós tentativa de cancelamento:")
print(reserva1.consultar_reserva())
