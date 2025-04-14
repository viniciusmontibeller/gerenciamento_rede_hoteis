# Sistema de Gerenciamento de Reservas em Rede de Hotéis

### PROBLEMA:
Desenvolver um sistema orientado a objetos em Python para gerenciamento de reservas em uma rede de hotéis, possibilitando a administração de: 
* Hóspedes
* Funcionários
* Reservas
* Quartos
* Filiais hoteleiras

### ESCOPO DO DESENVOLVIMENTO:
A rede de hotéis gerencia diversas filiais (hotéis), cada uma contendo vários quartos que podem ser classificados como **“Normal”** ou **“VIP”**. Os hóspedes podem realizar reservas de quartos por meio de funcionários, e cada *reserva* deve registrar: **Cliente**, **Quarto** e **Funcionário** responsável.

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
- Caso o cliente possua fidelidade, ele ganhará um **desconto de 10%**.

### RESTRIÇÕES DE ESCOPO:
Para simplificar este trabalho, o sistema contemplará apenas funcionalidades básicas de um sistema de reservas hoteleiras, **sem considerar aspectos financeiros, tributários, jurídicos ou integração com sistemas externos**.

O sistema deve considerar:

#### Cadastros:
Inclusão, exclusão, alteração e listagem de:
- **Clientes**, com atributos: ID, nome.
- **Funcionários**, com atributos: ID, nome.
- **Hotéis**, com atributos: nome.
- **Quartos**, com associação ao hotel e indicação do tipo (Normal ou VIP).
- **Rede de hotéis**, com seus respectivos hotéis.

#### Registros:
- **Reservas**, com inclusão, exclusão, alteração e listagem.  
  Cada reserva contém: cliente, quarto e funcionário.

#### Relatórios:
- Relatório de hotéis por região/endereço.
- Relatório das reservas realizadas por hotel e por tipo de quarto.
- Relatório de ocupação de quartos por hotel, listando a quantidade de reservas por quarto.
- Relatório de clientes com mais reservas realizadas.
- Relatório de funcionários com mais reservas cadastradas.
