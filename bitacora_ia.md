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

## Reflexión final

Entiendo la separación entre parámetros, física, simulación y visualización, y puedo explicar las fuerzas, la integración de Euler y las reglas de rebote usadas. Debo estudiar mejor la consistencia dimensional de los coeficientes de arrastre y Magnus, y las limitaciones de la colisión simplificada con la red. Entregar código generado sin revisarlo podría conservar errores de unidades, condiciones de borde incorrectas o resultados visualmente plausibles pero físicamente inválidos.
