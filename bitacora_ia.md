# Bitácora de IA generativa

## Interacción 1

- Fecha: 2026-08-27.
- Herramienta usada: Codex.
- Objetivo: diagnosticar el Live Script de MATLAB sin modificarlo.
- Prompt resumido: leer `TableTennisTests.mlx`, resumir responsabilidades, unidades, riesgos y módulos Python propuestos.
- Resultado obtenido: se identificaron gravedad, arrastre, Magnus, giro, rebotes, colisión con red, animación y gráficas; también la ambigüedad de `pitch = 23,5`.
- Cambios aceptados: plan de migración en `docs/plan_migracion.md` y conservación del original en `legacy/`.
- Cambios rechazados: reescribir o eliminar el archivo MATLAB original.
- Verificación realizada: se extrajo y comparó el código fuente del Live Script; se revisaron variables y reglas de colisión.
- Commit asociado: `docs: add migration plan for MATLAB simulation`.

## Interacción 2

- Fecha: 2026-08-27.
- Herramienta usada: Codex.
- Objetivo: traducir el núcleo numérico a módulos Python, sin animación.
- Prompt resumido: separar parámetros, física, integración y visualización; devolver las series temporales requeridas.
- Resultado obtenido: paquete `src/table_tennis_sim/` con `SimulationParameters`, `run_simulation` y funciones de colisión.
- Cambios aceptados: integración Euler y ecuaciones preservadas del Live Script.
- Cambios rechazados: convertir unidades a SI sin una validación física adicional; implementar una red más compleja sin evidencia del modelo original.
- Verificación realizada: prueba con simulación corta: formas de tiempo y estados consistentes, y disminución de velocidad vertical por gravedad antes de la colisión. Se detectó y corrigió un conflicto de nombres entre una matriz y la función de aceleración angular.
- Commit asociado: `feat: implement core table tennis simulation in Python` y `test: add basic simulation checks`.

## Interacción 3

- Fecha: 2026-08-27.
- Herramienta usada: Codex.
- Objetivo: crear una interfaz de exploración sin duplicar la física en el notebook.
- Prompt resumido: crear sliders para velocidades, giro, arrastre, Magnus, restitución, fricción, tiempo y paso; regenerar gráficas visibles.
- Resultado obtenido: `notebooks/01_simulacion_interactiva.ipynb` importa el paquete desde `src/` y define los sliders requeridos.
- Cambios aceptados: trayectoria 3D y series de posición, velocidad y velocidad angular con Matplotlib.
- Cambios rechazados: copiar el algoritmo de simulación dentro del notebook.
- Verificación realizada: se validó la estructura JSON del notebook, se instalaron las dependencias en `.venv`, pasaron dos pruebas automatizadas y se generaron y revisaron las gráficas. Se corrigió el dibujo de la red 3D, que inicialmente aparecía como una diagonal.
- Commit asociado: `feat: add interactive simulation notebook with sliders` y `fix: render net as a 3D plane`.

## Interacción 4

- Fecha: 2026-08-27.
- Herramienta usada: Chat GPT
- Objetivo: Seccionar el código con títulos para mejor entendimiento 
- Prompt resumido: Con el siguiente código que te proporcioné, elimina el clear cada que se actualiza un slider. Además coloca títulos para cada apartado del código y que se entienda mejor el código para alguien que no sepa programar.
- Resultado obtenido: https://drive.google.com/file/d/1azfOre6CYLLI6Jcec6f7dyW1BLjYf0Mq/view?usp=sharing, enlace a Código en Colab/Jupyter.
- Cambios aceptados: Los títulos o seccionado del código.
- Cambios rechazados: Copiar cada detalle dado por la IA.
- Verificación realizada: Una vez administrados los títulos dependiendo del apartado, se verificó si las divisiones y explicaciones estaban correctas.
- Commit asociado: `docs: seccionar y documentar codigo con titulos explicativos`.
  
## Reflexión final

Se entiende cómo está organizado el proyecto, especialmente la separación entre los parámetros, la parte física, la simulación y la visualización. Es posible explicar las fuerzas utilizadas y las condiciones de rebote de la pelota. Pero todavía se deben revisar de mejor manera las unidades de los coeficientes de arrastre y del efecto Magnus para que sean consistentes, además de comprender las limitaciones que tiene la representación de la red. Es importante no confiar completamente en el código generado por IA sin revisarlo, ya que podría tener errores en las unidades, las condiciones de rebote o generar resultados que se vean correctos, pero que realmente no representen bien el comportamiento físico.
