from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from config import TOKEN
import bot
# Nombre del bot: ImplementacionED_Bot


def main():
# Establecemos una conexión entre el programa y el bot
    updater = Updater(TOKEN, use_context = True)  # Insertamos el Token del bot
    dp = updater.dispatcher

# Estableciendo los comandos que ejecutará el bot
    # Inicio del bot
    dp.add_handler(CommandHandler("start", bot.start))
    # Maneja la ayuda que provee programa para su funcionamiento
    dp.add_handler(CommandHandler("ayuda", bot.ayuda))
    # Menú de instrucciones para un manejo más fácil
    dp.add_handler(CommandHandler("menu", bot.menu))
    dp.add_handler(CallbackQueryHandler(bot.menuButton, pattern = "op1"))
    dp.add_handler(CallbackQueryHandler(bot.menuButton, pattern = "op2"))
    dp.add_handler(CallbackQueryHandler(bot.menuButton, pattern = "op3"))
    # Recibir los coeficientes de un polinomio y muestra la forma de la solución
    dp.add_handler(CommandHandler("poli", bot.poli))
    # Creación de un grafo simple no dirigido con V vértices, y E aristas asignadas aleatoriamente
    dp.add_handler(CommandHandler("grafo", bot.grafo))
    # Subsecuencia de Fibonacci a partir de una secuencia
    dp.add_handler(CommandHandler("sec", bot.sec))
    # Control de errores
    dp.add_error_handler(bot.error)

# Iniciamos el bot
    updater.start_polling()
# Mantener el bot ejecutándose hasta que ocurra una interrupción (ctrl + c, error)
    updater.idle()


if __name__ == '__main__':
    main()
