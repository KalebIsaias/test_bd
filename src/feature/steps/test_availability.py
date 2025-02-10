from behave import given, when, then

# Simulação de disponibilidade do sistema
availability = 99.97  # Simulando uma métrica coletada

@given("o sistema está operacional")
def step_given_system_operational(context):
    context.system_up = True

@when("consultamos a métrica de uptime")
def step_when_check_availability(context):
    context.availability = availability

@then("a disponibilidade deve ser maior que 99.95%")
def step_then_check_uptime(context):
    assert context.availability > 99.95, "Disponibilidade abaixo do esperado!"
