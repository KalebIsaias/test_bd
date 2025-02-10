Feature: Monitoramento da Disponibilidade do Sistema

    Scenario: Sistema deve responder com disponibilidade acima de 99,95%
        Given o sistema está operacional
        When consultamos a métrica de uptime
        Then a disponibilidade deve ser maior que 99.95%