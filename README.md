# Bot-Telegram

El bot debe implementar las funcionalidades descritas a continuación. Es \textbf{obligatorio} un comando \texttt{\textbackslash ayuda} que describa qué hace el bot y qué comandos tiene. Además, en cada punto debe haber validación de los datos ingresados por el usuario. Cada comando debe mostrar o facilitar la comprensión del formato o la forma en que el usuario ingresa los datos.

\begin{itemize}
    \item Recibir los coeficientes de un polinomio característico de una relación de recurrencia y mostrar cuál sería la forma de la solución. Por ejemplo, el bot debe responder al usuario algo de la forma $f(n)=c_0\cdot 2^n+
    c_1\cdot n\cdot 3^n+c_2\cdot 3^n$.
    
    \item \textbf{[Bono +0.2]} Reciba también los casos base de la recurrencia y muestre la expresión con los valores de las constantes ($c_0,\,c_1,\,\dots,$).
    
    \item El usuario digita una secuencia de números enteros mayores o iguales a 0, ordenados de menor a mayor. El bot debe responder al usuario con una subsecuencia de la ingresada por el usuario de tal modo que la subsecuencia pueda considerarse como una secuencia de Fibonacci. Por ejemplo:
    El usuario digita \texttt{2 3 4 5 7 11 13 18 22 29} y el bot responde con la subsecuencia \texttt{3 4 7 11 18 29} o también podría responder con la subsecuencia \texttt{2 3 5}.
    
    \item La entrada del usuario consiste en 3 números: El número de vértices ($V$), número de aristas ($E$) y máximos de aristas por vértice ($K$). En este punto deben crear un grafo simple no dirigido con $V$ vértices, y $E$ aristas asignadas aleatoriamente, de tal modo que ningún vértice tenga un grado mayor a $K$. El bot debe retornar una imagen del grafo.
\end{itemize}
