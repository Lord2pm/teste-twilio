from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
import validators

from sigma_api import login


app = Flask(__name__)
app.secret_key = "1234567890"


@app.route("/")
def index():
    return "<h1>Olá mundo</h1>"


@app.route("/whatsapp", methods=["GET", "POST"])
def sms_reply():
    if "i" not in session:
        session["i"] = 0
        session["email"] = None
        session["senha"] = None

    resp = MessagingResponse()
    sender = request.values.get("From", "").replace("whatsapp:", "")
    i = session["i"]

    if i == 0:
        resp.message(
            "Olá, eu sou a IAN (Inteligência Artificial Natural da Rede Industrial)"
        )
        resp.message("Digite apenas o seu e-mail. Exemplo: luismuhele@gmail.com")
        session["i"] += 1
    elif i == 1:
        session["email"] = request.values.get("Body", "").strip()
        resp.message("Digite apenas a sua senha. Exemplo: 12345678")
        session["i"] += 1
    elif i == 2:
        session["senha"] = request.values.get("Body", "")
        email = session["email"]
        senha = session["senha"]

        if not validators.email(email):
            resp.message("O e-mail digitado é inválido. Digite o e-mail novamente!")
            session["i"] = 1
        else:
            if login(email, senha):
                resp.message("Usuário logado com sucesso")
                resp.message(
                    "1 - Solicitação de serviço\n2 - Ordem de serviço\n\nEscolha uma opção:"
                )
                session["i"] += 1
            else:
                resp.message(
                    "E-mail ou senha incorrectos. Volte a digitar o seu e-mail!"
                )
                session["i"] = 1
    elif i == 3:
        servico = request.values.get("Body", "")
        email = session["email"]

        if servico == "1":
            resp.message(f"Dados da solicitação de serviço de {email} | {sender}")
        elif servico == "2":
            resp.message(f"Dados da ordem de serviço de {email} | {sender}")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
