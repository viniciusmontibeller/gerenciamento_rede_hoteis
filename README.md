# Sistema de Gerenciamento de Reservas em Rede de Hotéis

### PROBLEMA:
Desenvolver um sistema orientado a objetos em Python para gerenciamento de reservas em uma rede de hotéis, possibilitando a administração de: 
* Hóspedes
* Funcionários
* Reservas
* Quartos
* Filiais hoteleiras

### ESCOPO DO DESENVOLVIMENTO:
A rede de hotéis gerencia diversas filiais (hotéis), cada uma contendo vários quartos que podem ser classificados como **“Normal”** ou **“VIP”**. Através do sistema é possivel agendar reservas de quartos por meio de funcionários, e cada *reserva* deve registrar: **Cliente**, **Quarto** e **Funcionário** responsável.

O sistema deve permitir o **cadastro, listagem, alteração e exclusão** de hotéis, quartos, clientes, funcionários e reservas. Além disso, deve garantir a integridade das operações e disponibilizar relatórios úteis para a administração.

### REGRAS DO SISTEMA:
- Um quarto pertence a um único hotel, mas cada hotel pode ter um ou mais quartos.
- Um cliente pode realizar várias reservas, mas cada reserva pertence a apenas um cliente.
- O cliente é responsável por solicitar sua própria reserva e, caso o quarto esteja disponível, uma reserva será criada para ele. Na reserva, o sistema atribui automaticamente um funcionário para ser o responsável pela reserva.
- Quartos podem ser do tipo **“Normal”** ou **“VIP”**, sendo o quarto VIP **20% mais caro**.
- Cada reserva deve conter obrigatoriamente: **cliente, quarto e funcionário responsável**.
- Cada rede de hotéis pode ter várias filiais (hotéis), mas cada hotel pertence a apenas uma rede.
- O custo da reserva é calculado após o **checkout**, sendo:  
  (valor da diária * dias utilizados).

### RESTRIÇÕES DE ESCOPO:
Para simplificar este trabalho, o sistema contemplará apenas funcionalidades básicas de um sistema de reservas hoteleiras, **sem considerar aspectos financeiros, tributários, jurídicos ou integração com sistemas externos**.

O sistema deve considerar:

#### Cadastros:
Inclusão, exclusão, alteração e listagem de:
- **Clientes**, com atributos: CPF, nome, telefone e-mail.
- **Funcionários**, com atributos: CPF, nome, telefone e-mail.
- **Hotéis**, com atributos: nome, código, endereço, telefone, quartos, funcionarios e clientes.
- **Quartos**, com associação ao hotel e indicação do tipo (Normal ou VIP).
- **Rede de hotéis**, com seus respectivos hotéis.

#### Registros:
- **Reservas**, com inclusão, exclusão, alteração e listagem.  
  Cada reserva contém: cliente, quarto e funcionário.

#### Relatório:
Relatório detalhado de cada hotel contendo:
- Quantidade de clientes
- Quantidade de funcionarios
- Quantidade de quartos
- Quantidade de reservas
- Faturamento atrvés das reservas

