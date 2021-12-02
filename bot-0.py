#!./bin/env python
from  telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Le Token du bot
bot_token = '2055559214:QQGDltTVqZcDepp8VjNSEvn81MRtCwEh6i8'

# # L'instance qui recois les messages du bot
# updater = Updater(bot_token, use_context=True)

# # Ajout des differentes commandes disponible au updater pour qu'il puisse les gerer
# updater.dispatcher.add_handler(CommandHandler('Welcome', start))

# # Ajout de la gestion des mauvaise commandes au updater
# updater.dispatcher.add_handler(MessageHandler(Filters.text, mishandle))

# Commande de demarrage
def start(update, context):
    update.message.reply_text(
    """
    Bienvenue sur le bot officiel de Recycle Plus.

    Les commandes disponibles sont :
    - /inscription pour obtenir l'adresse du site
    - /demande_collecte pour obtenir la chaîne YouTube
    - /recompenses pour obtenir son profil Linkedin
    """
    )

# Gestion des messqge inatendus ou incorrect
def mishandle(update, context):
    message = 'Je n\'ai pas compris votre message "{0}"'.format(update.message.text)
    update.message.reply_text(message)


# Commande d'inscription
def inscription(update, context):
    message = "Veuillez vous inscrire si ce n'est âs encore fait"
    update.message.reply_text(message)

# Commande de demande de collecte
def collecte(update, context):
    message = "Faite une demande de collecte"
    update.message.reply_text(message)

# Commande de gestion des recompenses
def recompense(update, context):
    message = "Recuperew vos recompenses"
    update.message.reply_text(message)

# Programme principal
def main():
    # La classe Updater permet de lire en continu ce qu'il se passe sur le channel
    updater = Updater(bot_token, use_context=True)

    # Pour avoir accès au dispatcher plus facilement
    dp = updater.dispatcher

    # On ajoute des gestionnaires de commandes
    # On donne a CommandHandler la commande textuelle et une fonction associée
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("inscription", inscription))
    dp.add_handler(CommandHandler("collecte", collecte))
    dp.add_handler(CommandHandler("recompense", recompense))

    # Pour gérer les autres messages qui ne sont pas des commandes
    dp.add_handler(MessageHandler(Filters.text, mishandle))

    # Sert à lancer le bot
    updater.start_polling()

    # Pour arrêter le bot proprement avec CTRL+C
    updater.idle()


if __name__ == '__main__':
    main()