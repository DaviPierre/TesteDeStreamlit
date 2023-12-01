import streamlit as st

def calcular_operacao(num1, num2, operacao):
    if operacao == "Soma":
        return num1 + num2
    elif operacao == "Subtração":
        return num1 - num2
    elif operacao == "Multiplicação":
        return num1 * num2
    elif operacao == "Divisão":
        if num2 != 0:
            return num1 / num2
        else:
            return None  # Retorna None para indicar erro de divisão por zero

# Definindo o título da página
st.title("Calculadora Simples")

# Entrada dos números
num1 = st.number_input("Digite o primeiro número:")
num2 = st.number_input("Digite o segundo número:")

# Botões para seleção da operação
operacao = st.radio("Selecione a Operação", ["Soma", "Subtração", "Multiplicação", "Divisão"])

# Botão de calcular
if st.button("Calcular"):
    # Realiza a operação selecionada
    resultado = calcular_operacao(num1, num2, operacao)

    # Exibindo o resultado ou mensagem de erro
    if resultado is not None:
        st.success(f"Resultado: {resultado}")
    else:
        st.error("Erro: Divisão por zero!")