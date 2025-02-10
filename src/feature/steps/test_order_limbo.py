from behave import given, when, then
import time
import random

# Simulação de pedidos "no limbo"
pending_orders = []

@given("um pedido é criado no sistema")
def step_given_order_created(context):
    context.order = {
        "id": random.randint(1000, 9999),
        "status": "unassigned",
        "created_at": time.time() - 750  # Simulando um pedido criado há 750 segundos (~12.5 minutos)
    }
    pending_orders.append(context.order)

@when("o pedido não recebe um entregador")
def step_when_order_unassigned(context):
    context.order["unassigned_time"] = time.time() - context.order["created_at"]

@when("o tempo excede 12 minutos")
def step_when_time_exceeds(context):
    context.time_exceeded = context.order["unassigned_time"] > 720  # 12 minutos em segundos

@then("um alerta de crise deve ser gerado")
def step_then_trigger_alert(context):
    assert context.time_exceeded, f"❌ ERRO: O pedido {context.order['id']} não atingiu o tempo limite!"
    print(f"⚠️ ALERTA: Pedido {context.order['id']} está sem alocação há mais de 12 minutos!")
