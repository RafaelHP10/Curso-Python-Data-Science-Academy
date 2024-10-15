# Imports

from openai import OpenAI

client = OpenAI()

# Função para gerar o texto a partir do modelo de linguagem
def gera_texto(texto):

        # Obtém a resposta do modelo de linguagem
    response = client.chat.completions.create(

        # Modelo usado
        # Outros modelos estão disponiveis em https://platform.openai.com/settings/organization/limits
        model = 'gpt-3.5-turbo',

        messages=[
            {
                "role": "user",
                "content": {texto},
            },
        ],
        max_tokens=10,

    )

    return response.choices[0].message.content

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

        # Coloca a mensagem digitada pelo usuário na variável Python chamada gtp4_prompt.
        gpt4_prompt = f"\nUsuário: {user_message}\nChatbot:"   

        # Obtém a resposta do modelo executando a função gera_texto().
        chatbot_response = gera_texto(gpt4_prompt)

        # Imprime a resposta do chatbot.
        print(f"\nChatbot: {chatbot_response}")

# Execução do programa (bloco main) em Python

if __name__ == '__main__':
    main()
