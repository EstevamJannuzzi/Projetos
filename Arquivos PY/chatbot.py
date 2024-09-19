from openai import OpenAI

client = OpenAI(
    api_key= 'sk-guJKj0WyokCujrZBx01sxqnowoLuOD_78Udgb-oh29T3BlbkFJ6YuvRhCQQs0tmbOl1qmj9QdHGs9RnsHjK7iHIryegA'
)

def enviar_mensagem(pergunta):
    resposta = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {'role': 'user', 'content': pergunta}
        ]
    )

    return resposta.choices[0].message.content

while True:
    qtd = 80
    print('=' * qtd)
    print('\033[1;35mFale com nossa I.A.\033[m'.center(qtd + 10))
    print('=' * qtd)
    pergunta = str(input('Faça uma pergunta para \033[1;34mI.A.\033[m(Para terminar o programa digite \033[31mParar\033[m): ')).upper()
    if pergunta != 'PARAR':
        print(enviar_mensagem(pergunta))
    else:
        break
