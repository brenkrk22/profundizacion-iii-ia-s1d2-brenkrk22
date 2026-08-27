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
