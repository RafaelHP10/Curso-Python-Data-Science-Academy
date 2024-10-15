# Imports
import openai
import os
import time

# Chave da API (substitua 'SUA_API_KEY' pela sua chave real)
openai.api_key = os.environ['OPENAI_API_KEY']
cache = {}

# Função para gerar o texto a partir do modelo de linguagem
def gera_texto(texto, espera=10):

    # Obtém a resposta do modelo de linguagem
    response = openai.chat.completions.create(
        # Modelo usado
        model='gpt-4o-mini',
        messages=[
            {
                "role": "user",
                "content": texto,  # Texto é passado diretamente
            },
        ],
        max_tokens=1,
        n=5,
        stop=None,
        temperature=0.8,
    )
    time.sleep(espera)
    return response.choices[0].message['content']

# Função principal do programa em Python
def main():

    print("\nBem-vindo ao Chatbot do Projeto 3 do curso da Data Science Academy!")
    print("(Digite 'sair' a qualquer momento para encerrar o chat)")

    # loop
    while True:

        # Colete a pergunta digitada pelo usuário.
        user_message = input("\nVocê: ")

        # Se a mensagem for "sair" finaliza o programa.
        if user_message.lower() == 'sair':
            break

        # Coloca a mensagem digitada pelo usuário na variável Python chamada gpt4_prompt.
        gpt4_prompt = f"\nUsuário: {user_message}\nChatbot:"   

        # Obtém a resposta do modelo executando a função gera_texto().
        chatbot_response = gera_texto(gpt4_prompt)

        # Imprime a resposta do chatbot.
        print(f"\nChatbot: {chatbot_response}")

# Execução do programa (bloco main) em Python
if __name__ == '__main__':
    main()
