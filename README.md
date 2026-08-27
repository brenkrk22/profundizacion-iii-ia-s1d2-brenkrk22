## Autores
- Caroline Valentina García Pereira
- Karol Michelle Benavides Castillo
- Kevin Duque Delgado
- Brenk Sneider Bohorquez Vargas

## Fecha de entrega
27 de Agosto del 2026 a las 20:00 p.m.

# Simulación de pelota de tenis de mesa
Migración reproducible de un Live Script de MATLAB a Python. El modelo representa gravedad, arrastre, efecto Magnus, giro, rebotes sobre la mesa y una colisión simplificada con la red.

## Video - Simulación código, simulador de mesa de Tennis
https://youtu.be/c2V1b7xJp5s?si=VaL09WgXj73y7wI5

## Objetivo
Se procura pasar la simulación de tenis de mesa que estaba en MATLAB a Python, tratando de mantener su funcionamiento principal. Se busca agregar una interfaz con sliders que permita cambiar algunos parámetros y ver de forma gráfica cómo estos afectan el movimiento y la trayectoria de la pelota.

## Estructura
La estructura fue definida por el docente durante la clase. Esto con el fin de mantener una organización clara del proyecto,  facilitando la comprensión de la documentación para el lector, permitiendo dar a conocer la separación entre el código original, la simulación desarrollada en Python, la interfaz interactiva y las pruebas.

```text
proyecto-ia-tenis-mesa/
├── docs/                   # Plan de migración
├── legacy/                 # Live Script MATLAB original, sin modificar
├── notebooks/              # Interfaz interactiva con sliders
├── results/                # Resultados generados (no versionados)
├── src/table_tennis_sim/   # Paquete Python de la simulación
├── tests/                  # Verificaciones mínimas
├── .gitignore
├── README.md
├── bitacora_ia.md
└── requirements.txt
```
Para que se entienda de mejor manera cada apartado, a continuación se hará una breve descripción del contenido de la documentación.

* **Docs/** Documentación y proceso de migración es decir de Matlab a Python, y de ahí a Codex.
* **Legacy/** Contiene el código original de MATLAB proporcionado por el docente, se conserva como referencia y no se modifica.
* **Notebooks/** Cuaderno desarrollado en Jupyter; interfaz interactiva de la mesa de tenis modificable con base a sliders, presenta la trayectoria en 3D y además muestra las gráficas posición (m), velocidad, velocidad angular, con respecto al tiempo, todo adaptable a los valores registrados en los sliders.
* **Results/** Destinada a almacenar resultados generados de la simulación.
* **src/** Carpeta del código principal en Python.
* **tests/** Se guardan las modificaciones y pruebas que se le han hecho al código.

* **.gitignore/** Carpetas que Git debe ignorar y no subir al repositorio.
* **README.md/** Prácticamente es la documentación donde se especifican los segmentos del trabajo y su elaboración.
* **bitacora_ia.md/** Registra el uso de IA, interacciones con Codex, objetivos de cada interacción, resultados, cambios aceptados o rechazados, y verificaciones realizadas.
* **requirements.txt/** Especifica las bibliotecas necesarias para ejecutar el proyecto: NumPy, Matplotlib, ipywidgets y Jupyter.
  
## Instalación
Antes de la instalación se deben leer los archivos correspondientes para comprender las funciones de cada una de las aplicaciones que integran el proceso.
Como primer paso se debe abrir PowerShell y procesar los comandos:
- winget install --id Git.Git -e  //para instalación de Github.
- winget install --id Microsoft.VisualStudioCode -e //instalación de Visual Studio Code en caso de tenerlo.
- winget install --id Python.Python.3.14 -e //para instalación de Python.
- winget install --id GitHub.cli -e //instalacipon de GitHub CLI.

Se procede a verificar las versiones instaladas:
git --version.
python --version.
gh --version.

Se agrega Codex según la guía de chatGPT:
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"

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
- Requiere de un entorno en específico, Python versión 3.10 o superior.

## Uso de IA generativa

La trazabilidad de las interacciones, decisiones y verificaciones está en [bitacora_ia.md](bitacora_ia.md).


