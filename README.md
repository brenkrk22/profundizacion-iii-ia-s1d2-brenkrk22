# Simulación de pelota de tenis de mesa

Migración reproducible de un Live Script de MATLAB a Python. El modelo representa gravedad, arrastre, efecto Magnus, giro, rebotes sobre la mesa y una colisión simplificada con la red.

## Estructura

```text
proyecto-ia-tenis-mesa/
├── legacy/                 # Live Script MATLAB original, sin modificar
├── src/table_tennis_sim/   # Paquete Python de la simulación
├── notebooks/              # Interfaz interactiva con sliders
├── tests/                  # Verificaciones mínimas
├── docs/                   # Plan de migración
├── results/                # Resultados generados (no versionados)
├── bitacora_ia.md
└── requirements.txt
```

## Instalación

Requiere Python 3.10 o superior.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Uso rápido

Desde la raíz del repositorio, abre Jupyter:

```powershell
jupyter notebook notebooks/01_simulacion_interactiva.ipynb
```

El notebook importa el paquete local desde `src/`. Ejecuta todas las celdas y usa los sliders para regenerar la trayectoria 3D y las series temporales.

Para comprobar el núcleo sin notebook:

```powershell
$env:PYTHONPATH = "$PWD\src"
python -m pytest tests
```

## Parámetros ajustables

| Parámetro | Unidad | Rango del notebook |
| --- | --- | --- |
| Velocidades iniciales X, Y, Z | mm/s | X: 1000 a 10000; Y/Z: -6000 a 6000 |
| Giro inicial Z | rev/s | -150 a 150 |
| Arrastre | mN/(mm/s) | 0 a 6 |
| Magnus | mN/(mm/s²) | 0 a 0.05 |
| Restitución mesa/red | adimensional | 0 a 1 |
| Fricción de mesa | adimensional | 0 a 1 |
| Tiempo y paso | s | 0.2 a 3; 0.001 a 0.02 |

## Limitaciones conocidas

- Se conservan las unidades del modelo original (g, mm, s y mN), no unidades SI.
- La red se modela como una colisión simplificada.
- La integración usa Euler explícito; pasos grandes reducen la estabilidad.
- La animación cuadro a cuadro del Live Script no se migró: se priorizaron gráficos reproducibles e interactividad en el notebook.
- El `pitch = 23,5` del original se interpreta como 23.5 grados previstos; la coma es ambigua en MATLAB.

## Uso de IA generativa

La trazabilidad de las interacciones, decisiones y verificaciones está en [bitacora_ia.md](bitacora_ia.md).

## Autores

brenk sneider bohorquez vargas, kevin duque, caroline valentina garcia, karol venebides
