Juego de Memoria en Pygame

Este código es un juego de memoria en Pygame donde el jugador debe encontrar los pares de numeros iguales. 
El juego comienza con una pantalla inicial que ofrece al jugador la opción de empezar o salir. 
Al elegir "Sí", se muestran las cartas brevemente durante 5 segundos para que el jugador pueda memorizarlas. 
Las cartas se generan aleatoriamente con símbolos emparejados y se distribuyen en un tablero de 4x4. 
El jugador hace clic en las cartas para revelarlas; si dos cartas tienen el mismo símbolo, permanecen reveladas.
El juego muestra el número de coincidencias y los intentos realizados. 
Cuando se encuentran todos los pares, se muestra un mensaje de victoria y el juego vuelve a la pantalla inicial.
Se utiliza una estructura de clases para manejar las cartas, cada una con su propio estado (revelada o encontrada), 
y el flujo del juego está controlado por un bucle principal que actualiza la pantalla y maneja eventos de entrada del usuario.

Requisitos
Para ejecutar el juego se necesita: 
Python 3 instalado en tu sistema.
Pygame instalado. Si no lo tienes, puedes instalarlo ejecutando:
  ```bash
  pip install pygame
