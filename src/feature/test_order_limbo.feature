Feature: Redução da Taxa de Pedidos "No Limbo"

    Scenario: Pedidos não devem ficar sem alocação por mais de 12 minutos
        Given um pedido é criado no sistema
        When o pedido não recebe um entregador
        And o tempo excede 12 minutos
        Then um alerta de crise deve ser gerado