from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

bot = Flask(__name__)

@bot.route("/appsbot", methods=["POST"])
def whatsapp_bot():
    client = request.values.get("Body", "").lower()
    resp = MessagingResponse()
    reply = resp.message()

    if "hi" in client:
        reply.body("Thanks for contacting us..\n\nWelcome to our Matrimony, How we help you")
    elif "details for registration" in client:
        reply.body("For registration, a person must keep below details:\n\nAadhar Card\nCommunity Certificate\nPhoto copy\nBio data")
    elif "registration fee" in client:
        reply.body("For Registration : 750/-, For other details contact our office")
    elif "contact" in client:
        reply.body("Office : 0987654321")
    elif 'registration form' in client:
        media_url = 'https://drive.google.com/uc?export=download&id=1IHnXgzHPk3d'
        reply.body('Please fill the attached form.')
        reply.media(media_url)

    elif "வணக்கம்" in client:
        reply.body("வணக்கம், உங்களுக்கு என்ன உதவி வேண்டும்..!")
    elif "bye" in client:
        reply.body("Goodbye! Have a nice day..")
    else:
        reply.body("I'm a simple bot...! Please enter below visible sentence\n\ndetails for registration\ncontact\nregistration form\nregistration fee\n")

    return str(resp)

if __name__ == "__main__":
    bot.run(host="0.0.0.0", port=5000, debug=True)