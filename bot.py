import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import polinom
import secu
import grafoSimple
import requests

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(message)s')
logger = logging.getLogger(__name__)


def image(update, context, url):
    img = open(url, "rb")
    chat_id = update.message.chat_id
    update.message.bot.sendPhoto(chat_id=chat_id, photo=img)
    logger.info("Se ha enviado la imagen correctamente")


def latex(update, context, formula, file):
    formula = formula.replace('\n', ' ')
    r = requests.get('http://latex.codecogs.com/png.latex?\dpi{{300}} {formula}'.format(formula=formula))
    f = open(file, 'wb')
    f.write(r.content)
    f.close()

    chat_id = update.message.chat.id
    try:
        context.bot.send_photo(chat_id=chat_id, photo=open('equation.png', 'rb'))
        logger.info("Se ha enviado la ecuación correctamente")
    except Exception as e:
        logger.info("Error en el envio de la ecuación por Latex")
        update.message.reply_text("Disculpa, no he logrado procesar la ecuación en Latex. \n \n {}".format(formula))


def start(update, context):
    opciones = [[InlineKeyboardButton("Forma de solución de un polinomio ", callback_data='op1')],
                [InlineKeyboardButton("Subsecuencia de Fibonacci", callback_data='op2')],
                [InlineKeyboardButton("Grafo simple no dirigido", callback_data='op3')]]
    reply_markup = InlineKeyboardMarkup(opciones)
    name = update.message.from_user.first_name
    update.message.reply_text("¡Hola, {} \U0001F44B! Mi nombre es Celda 37 y es un placer ayudarte.\n"
                              "Soy un bot creado para desarrollar los conocimientos adquiridos en Estructuras Discretas. \n"
                              "Escoge la operación la cual quieras ver sus instrucciones  \U0001F604:".format(name),
                              reply_markup=reply_markup)


def ayuda(update, context):
    update.message.reply_text(
        "Soy un bot creado por el grupo Celda 37 de la clase de Estructuras Discretas de la Universidad del Norte. \n \n"
        "Puedo realizar varias tareas : \n \n"
        "\t /start - Da inicio al bot \n"
        "\t /ayuda - Describe que hacen los comandos del bot \n"
        "\t /menu - Despliega un /menu instructivo de opciones interactivo \n \n"
        "Además, estoy programado para hacer tres tareas más específicas : \n \n"
        "\t /poli - Forma de la solución de un polinomio dado coeficientes \n"
        "\t /sec - Subsecuencia de Fibonacci a partir de una secuencia \n"
        "\t /grafo - Creación de un grafo simple no dirigido \n \n"
        "Para comenzar puedes desplegar el /menu iterativo")


def menu(update, context):
    opciones = [[InlineKeyboardButton("Solución de un polinomio caracteristico de RR", callback_data='op1')],
                [InlineKeyboardButton("Subsecuencia de Fibonacci", callback_data='op2')],
                [InlineKeyboardButton("Grafo simple no dirigido", callback_data='op3')]]
    reply_markup = InlineKeyboardMarkup(opciones)
    update.message.reply_text("A continuación se despliega el /menu de instrucciones de los comandos. \n"
                              "Presiones el comando el cual quiere conocer su funcionamiento: ",
                              reply_markup=reply_markup)


def menuButton(update, context):
    query = update.callback_query
    query.answer()
    answer = query.data
    chat_id = query.message.chat_id
    if answer == "op1":
        polinomio(chat_id, query)
    elif answer == "op2":
        secuencia(chat_id, query)
    elif answer == "op3":
        grafoS(chat_id, query)


def polinomio(chat_id, query):
    query.message.reply_text("Inicia colocando el comando /poli \n"
                             "En el mismo mensaje, sin enviar, da un espacio e ingrese con comas y con corchetes los coeficientes y casos bases [a, b, c]; [d, e] \n "
                             "Recuerda que los parámetros son: coeficientes del polinomio y casos base de la RR, respectivamente, separados por \";\" \n \n"
                             "Ejemplo : \n"
                             "\t \t Dada la RR: f(n) = 6f(n - 1) - 9f(n - 2);   f(0) = 0,  f(1) = 1 \n"
                             "\t \t Los parámetros de entrada serian : \n"
                             "\t \t /poli [1, -6, 9]; [0, 1] \n \n"
                             "Celda 37 se encargará de mostrar cual sería la forma de la solución dado los coeficientes del polinomio. \n"
                             "También, mostrara la expresión con los valores de las constantes dado los casos bases.")


def secuencia(chat_id, query):
    query.message.reply_text("Inicia colocando el comando /sec \n"
                             "En el mismo mensaje, sin enviar, da un espacio e ingresa con comas y con corchetes la secuencia [a, b, c, d, ...] \n"
                             "Recuerda que debes ingresar números enteros mayores o iguales a 0 y ordenados de menor a mayor. \n "
                             "Si no estan ordenados, Celda 37 se encargara de ordenarlos. \n \n"
                             "Ejemplo : \n"
                             "\t \t /sec [2, 3, 4, 5, 7, 11, 13, 18, 22, 29] \n \n"
                             "Celda 37 se encargará de encontrar una subsecuencia que pueda considerarse como una secuencia de Fibonacci, es decir, que "
                             "un número de la sucesión sea la suma de sus dos inmediatamente anteriores, exceptuando los dos primeros.")


def grafoS(chat_id, query):
    query.message.reply_text("Inicia colocando el comando /grafo \n"
                             "En el mismo mensaje, sin enviar, da un espacio e ingresa con comas y con o sin corchetes los 3 parámetros [v, a, k] \n"
                             "Recuerda que los parámetros son: número de vertices, número de aristas y máximo de aristas por vértice, respectivamente. \n "
                             "Cabe recalcar que el mayor número de aristas esta dado por 2a <= v(v - 1), donde k <= v - 1, si se coloca un k > v - 1"
                             "este automaticamente lo reestablecera como k = v - 1 al ser un grafo simple. \n \n"
                             "Ejemplo : \n"
                             "\t \t /grafo [9, 20, 5] \n"
                             "\t \t /grafo 9, 20, 5 \n \n"
                             "Celda 37 se encargará de crear un grafo simple no dirigido con vertices y aristas aleatorias respetando los parámetros.")


def poli(update, context):
    name = update.message.chat["first_name"]
    logger.info(f"El usuario {name} ha solicitado un polinomio")
    text = update.message.text
    text = text.replace("/poli", "").strip()
    partes = text.split(';')
    try:
        p1 = partes[0]
        p2 = partes[1]
        if len(partes) > 2:
            logger.info("Se introdujo mas parametros de los debidos")
            update.message.reply_text("Solo se consideraran los 3 primeros parámetros.")
    except Exception as e:
        logger.info("Ha ocurrido un error en la cantidad de parametros del polinomio")
        update.message.reply_text("Por favor, digite la cantidad de parámetros correctamente. \n"
                                  "Se recomienda mirar el /menu de instrucciones.")
        return
    try:
        coef = eval(p1.strip())
        ini = eval(p2.strip())
        try:
            respuesta = polinom.mainPolinomio(coef, ini)
        except Exception as e:
            logger.info("La Relación de Recurrencia no es homogénea o no se puede solucionar")
            update.message.reply_text("La Relación de Recurrencia no es homogénea o no se puede solucionar.")
            return
        logger.info("Se ha ejecutado el polinomio con {}".format(text))
        update.message.reply_text("La forma de la solución de la Relación de Recurrencia dado sus coeficientes es :")
        latex(update, context, respuesta[0], 'equation.png')
        update.message.reply_text(
            "La expresión, con los valores de las constantes, del polinomio característico de la Relación de Recurrencia es :")
        latex(update, context, respuesta[1], 'equation.png')
    except Exception as e:
        logger.info("Ha ocurrido un error en los parárametros del polinomio con {}".format(text))
        update.message.reply_text("Por favor, digite los parámetros del polinomio correctamente. \n"
                                  "Se recomienda mirar el /menu de instrucciones.")


def sec(update, context):
    name = update.message.chat["first_name"]
    logger.info(f"El usuario {name} ha solicitado una secuencia")
    text = update.message.text
    text = text.replace("/sec ", "").strip()
    try:
        secuen = sorted(eval(text))
        if secuen[0] < 0:
            logger.info("Si ingresaron datos no positivos en el parámetro")
            update.message.reply_text("Por favor, digite solo números positivos, mayores o iguales a 0.")
            return
        try:
            resp = secu.mainSecuancia(secuen)
            if len(resp) == 0:
                logger.info("La secuencia ingresada no cuenta con subsecuencia de Fibonacci")
                update.message.reply_text("La secuencia no cuenta con alguna subsecuencia que "
                                          "podamos considerara como subsecuencia de Fibonacci.")
                return
        except Exception as a:
            logger.info("Ha ocurrido un error al solucionar la secuencia")
            update.message.reply_text(
                "Nos disculpamos, ocurrió un error en la búsqueda de la subsecuancia de Fibonacci. \n"
                "Intente con otra secuencia, por favor.")
            return
        logger.info("Se ha ejecutado la secuancia correctamente con {}".format(text))
        update.message.reply_text(
            "La subsecuencia más larga, que podemos considerar como una secuencia de Fibonacci, encontrada fue \n \n {}".format(
                resp))
    except Exception as e:
        logger.info("Ha ocurrido un error en los parámetros de la secuencia con {}".format(text))
        update.message.reply_text("Por favor, digite la secuencia correctamente. \n"
                                  "Se recomienda mirar el /menu de instrucciones.")


def grafo(update, context):
    name = update.message.chat["first_name"]
    logger.info(f"El usuario {name} ha solicitado un grafo")
    text = update.message.text
    text = text.replace("/grafo ", "").strip()
    try:
        graph = eval(text)
        vertices = int(graph[0])
        aristas = int(graph[1])
        limite = int(graph[2])
        if vertices <= 0 or aristas <= 0 or limite <= 0:
            logger.info("Ha ingresado parámetros con números no positivos.")
            update.message.reply_text("Por favor, ingrese números positivos en los parárametros.")
            return
        if len(graph) > 3:
            logger.info("Ha ingresado mas parámetros de los debidos")
            update.message.reply_text("Al ingresar más parámetros de los pedidos, solo se tomaran en cuenta los 3 primeros.")
        if aristas > (vertices * (vertices - 1)) // 2:
            logger.info("Ha ocurrido un error, aristas > (vertices * (vertice - 1))// 2")
            update.message.reply_text(
                "El número de aristas no puede ser mayor a (v * (v - 1))// 2 = {}. Le recomendamos mirar el /menu de instrucciones.".format(
                    (vertices * (vertices - 1)) // 2))
            return
        if limite <= (vertices - 1) and aristas > (vertices * limite) // 2:
            logger.info("Ha ocurrido un error, aristas > (vertices * limite)// 2")
            update.message.reply_text(
                "El número de aristas no puede ser mayor a (v * k)// 2 = {}. Le recomendamos mirar el /menu de instrucciones.".format(
                    (vertices * limite) // 2))
            return
        if limite > vertices - 1:
            limite = vertices - 1

        bool = grafoSimple.mainGrafo(vertices, aristas, limite)
        if bool:
            logger.info("Se ha ejecutado el grafo correctamente con {}".format(text))
            update.message.reply_text("El grafo simple no dirigido con {} vértices, y {} aristas asignadas aleatoriamente es : ".format(vertices, aristas))
            image(update, context, "grafo.png")
        else:
            logger.info("Ha ocurrido un error en la busqueda del grafo")
            update.message.reply_text("Nos disculpamos, ocurrió un error en la búsqueda del grafo, al utilizar asignación al azar. \n"
                                      "Le recomendamos usar un número de aristas menor o seguir intentando hasta que la aleatoriedad le favorezca.")
            return
    except Exception as e:
        logger.info("Ha ocurrido un error en los parámetros del grafo con {}".format(text))
        update.message.reply_text("Por favor, digite los parámetros del grafo correctamente. \n"
                                  "Se recomienda mirar el /menu de instrucciones.")


def error(update, context):
    logger.warning('La solicitud "%s" causó el error "%s"', update, context.error)
