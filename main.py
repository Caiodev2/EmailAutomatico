import smtplib
from email.message import EmailMessage

#função para enviar o email
def envia_email(PessoaRemetente, senha, PessoaDestinado, assunto, corpo):
    email = EmailMessage()
    email['From'] = PessoaRemetente
    email["To"] = PessoaDestinado
    email['Subject'] = assunto
    email.set_content(corpo)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(PessoaRemetente, senha)
            smtp.send_message(email)
            print("E-mail enviado com sucesso")

    except Exception as e:
        print("Erro:" + e)

#input para usuário
print('------Enviar e-mail automaticamente------')
remetente = input("Digite seu e-mail(remetente): ")
senha = input("Digite sua senha: ")
destinado = input("Digite o e-mail do destinado: ")
assunto = input("Digite o assunto: ")
mensagem = input("Digite a mensagem(corpo): ")


#usando a função que envia o e-mail
envia_email(remetente, senha, destinado, assunto, mensagem)