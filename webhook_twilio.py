from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_message = request.form.get('Body')  # Obtener el contenido del mensaje entrante

    # Aquí puedes implementar tu lógica para generar una respuesta automática
    response_text = "¡Hola! Esta es una respuesta automática."
    print(incoming_message)
    response = MessagingResponse()
    response.message(response_text)  # Crear una respuesta

    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
