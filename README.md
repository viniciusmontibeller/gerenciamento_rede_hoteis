# Sistema de Gerenciamento de Reservas em Rede de Hotéis


### Problema
Desenvolver um sistema orientado a objetos em Python para gerenciamento de reservas em uma rede de hotéis. O sistema deve permitir a administração de:
- Hóspedes
- Funcionários
- Reservas
- Quartos
- Filiais hoteleiras

### Escopo do Desenvolvimento
A rede de hotéis gerencia diversas filiais (hotéis), cada uma com múltiplos quartos classificados como **Normal** ou **VIP**. Os hóspedes realizam reservas por meio de funcionários. Cada reserva deve conter:
- Cliente
- Quarto
- Funcionário responsável

O sistema deve permitir as seguintes funcionalidades:
- Cadastro, listagem, alteração e exclusão de:
  - Hotéis
  - Quartos
  - Clientes
  - Funcionários
  - Reservas
- Garantia da integridade das operações
- Geração de relatórios administrativos

### Regras do Sistema
- Um **quarto** pertence a um único **hotel**
- Um **hotel** pode ter vários **quartos**
- Um **cliente** pode realizar várias **reservas**, mas cada reserva pertence a apenas um cliente
- Um **funcionário** pode ser responsável por várias **reservas**
- Os **quartos** podem ser do tipo "Normal" ou "VIP"
- Cada **reserva** deve obrigatoriamente conter: cliente, quarto e funcionário
- Uma **rede de hotéis** pode conter várias filiais, mas cada hotel pertence a uma única rede

### Restrições de Escopo
Para simplificação, o sistema contemplará apenas funcionalidades básicas, excluindo aspectos financeiros, tributários, jurídicos ou integração com sistemas externos.

### Funcionalidades do Sistema

#### Cadastros
Operações de inclusão, exclusão, alteração e listagem para:
- **Clientes**: ID, nome
- **Funcionários**: ID, nome
- **Hotéis**: nome
- **Quartos**: associação ao hotel e tipo (Normal ou VIP)
- **Rede de Hotéis**: com seus respectivos hotéis

#### Registros
- **Reservas**: inclusão, exclusão, alteração e listagem
  - Cada reserva inclui: cliente, quarto e funcionário

#### Relatórios
- Reservas realizadas por hotel e por tipo de quarto
- Ocupação de quartos por hotel (quantidade de reservas por quarto)
- Clientes com mais reservas realizadas
- Funcionários com mais reservas cadastradas

