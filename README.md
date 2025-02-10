# 📌 Teste do Business Drivers

## 📖 Visão Geral
Este repositório documenta a implementação e testes automatizados dos Business Drivers do projeto. O foco está na redução da taxa de pedidos "no limbo" (DN1) e na garantia da disponibilidade do sistema (DN2).

## 🗺️ Mapa dos Business Drivers
```mermaid
graph TD;
    A[Redução da Taxa de Pedidos No Limbo] -->|Monitoramento de Pedidos Unassigned| B(Triggers Automáticos);
    A -->|Aprimoramento de Algoritmo de Distribuição| C(Ajuste de Critérios);
    B -->|Alertas e Playbooks| D(Gerenciamento de Crises);
    C -->|Melhoria de Alocação| D;
    E[Disponibilidade do Sistema] -->|Monitoramento Contínuo| F(Dashboards e Logs);
    E -->|Redundância e Failover| G(Infraestrutura de Alta Disponibilidade);
    G -->|Redução de Tempo de Inatividade| H(Recuperação Automática);
    F -->|Ações Corretivas Rápidas| H;
```
