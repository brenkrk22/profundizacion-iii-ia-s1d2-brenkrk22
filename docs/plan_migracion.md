# Plan de migración: MATLAB a Python

## Diagnóstico

El Live Script original simula una pelota de tenis de mesa en unidades de g, mm, s y mN. En un único archivo combina constantes, integración numérica, colisiones, animación 3D y gráficas. La función `plotTable` también mezcla el dibujo de la mesa con los datos instantáneos de la pelota.

## Módulos propuestos

| Módulo | Responsabilidad |
| --- | --- |
| `parameters.py` | Parámetros físicos, dimensiones, tiempo y condiciones iniciales. |
| `physics.py` | Fuerzas, aceleraciones y reglas de colisión. |
| `simulation.py` | Integración temporal y resultado de la simulación. |
| `visualization.py` | Trayectoria 3D y series temporales con Matplotlib. |

## Entradas y salidas

- Entradas: `SimulationParameters`, posición, velocidad y velocidad angular iniciales.
- Salidas: tiempo, posición, velocidad, aceleración, orientación, velocidad angular y aceleración angular.

## Criterios mínimos de verificación

1. El resultado tenga matrices de forma `(n_pasos, 3)` y el tiempo sea creciente.
2. La gravedad reduzca la componente vertical de velocidad antes de una colisión.
3. Un rebote dentro de los límites de la mesa invierta la velocidad vertical y aplique restitución.
4. La ejecución produzca las cuatro visualizaciones requeridas sin animación.
5. El notebook llame al paquete de `src/`, sin duplicar la física.

## Riesgos conocidos y decisiones

- El original declara `pitch = 23,5;`; en MATLAB la coma separa expresiones. En Python se usa el valor previsto `23.5`.
- Las constantes se mantienen inicialmente en g, mm, s y mN para preservar el comportamiento del modelo. No son unidades SI y la consistencia física del arrastre/Magnus debe validarse experimentalmente.
- La detección de red es simplificada: solo refleja la componente X y amortigua el giro.
- Se usa Euler explícito, como en el script original; pasos demasiado grandes pueden volver inestable la simulación.

## Flujo de trabajo para desarrollar la migración
MATLAB original → Organizar el código → Definir parámetros → Desarrollar físicas → Generar simulación → Añadir gráficas → Agregar sliders → Pruebas → Comparar → Documentación

## Plan de migración
Para hacer la migración de MATLAB a Python, primero se revisó el código original para entender cómo estaba hecha la simulación y qué partes eran necesarias para que siguiera funcionando de la misma manera.

**1.MATLAB original**
Primero se toma el archivo TableTennisTests.mlx y se revisa su funcionamiento. Se identifican las variables, los parámetros, las ecuaciones y el movimiento de la pelota.

**2.Organizar el código**
Se crea la estructura del proyecto en Python. El código original de MATLAB queda en legacy, mientras que la nueva versión se organiza dentro de src/table_tennis_sim. El notebook queda en notebooks para poder ejecutar la simulación de una forma más sencilla.

**3.Definir parámetros**
Los parámetros utilizados en MATLAB se pasan al archivo parameters.py. En este paso también se revisan los valores y las unidades para evitar que cambien los resultados en caso que se cometa una equivocación.

**4. Desarrollar físicas**
Las ecuaciones utilizadas para calcular el movimiento de la pelota se llevan a Python. En physics.py se organizan las funciones relacionadas con la gravedad, el arrastre y el efecto Magnus.

**5.Generar simulación**
Luego se desarrolla simulation.py, donde se realiza el cálculo de la trayectoria de la pelota. Se mantiene el método de Euler utilizado en el modelo original y se agregan las condiciones necesarias para los rebotes.

**6. Añadir gráficas**
La visualización se organiza en visualization.py. Aquí se generan las gráficas necesarias para poder observar la trayectoria y analizar el comportamiento de la pelota.

**7. Agregar sliders**
Cuando la simulación ya funciona, se lleva al notebook 01_simulacion_interactiva.ipynb. Allí se agregan sliders para cambiar algunos parámetros y observar cómo cambia la trayectoria de la pelota.

**8. Pruebas**
Se realizan pruebas básicas con test_simulation.py para comprobar que la simulación funcione y que las funciones principales entreguen resultados esperados.

**9. Comparar**
Finalmente, se comparan los resultados obtenidos en Python con el funcionamiento esperado del código de MATLAB. Si se encuentran diferencias, se revisan los cálculos, las unidades o los parámetros utilizados.

**10. Documentación**
Por último, se documenta el proceso de migración y el uso de la IA en bitacora_ia.md, además de dejar en el README.md la información necesaria para entender y ejecutar el proyecto.
