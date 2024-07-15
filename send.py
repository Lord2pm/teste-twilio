from twilio.rest import Client

account_sid = "ACfb8e605e8fb9b883965bbd5e7d45251c"
auth_token = "47630995e0ea2f7a974a61c0ab377a25"
client = Client(account_sid, auth_token)


def enviar_mensagem_whatsapp(mensagem, numero_destino):
    message = client.messages.create(
        body=mensagem,
        from_="whatsapp:+14155238886",  # Número do WhatsApp Sandbox do Twilio
        to=f"whatsapp:{numero_destino}",
    )
    return message.sid


# Exemplo de uso
numero_destino = "+244935613281"  # Número de destino no formato internacional
mensagem = "Olá, esta é uma mensagem de teste!"
message_sid = enviar_mensagem_whatsapp(mensagem, numero_destino)
print(f"Mensagem enviada com SID: {message_sid}")
