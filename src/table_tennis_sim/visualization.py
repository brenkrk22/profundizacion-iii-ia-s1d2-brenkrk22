"""Visualizaciones de la simulación con Matplotlib."""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure

from .parameters import SimulationParameters
from .simulation import SimulationResult


def plot_trajectory_3d(result: SimulationResult, params: SimulationParameters) -> Figure:
    """Dibuja mesa, red y trayectoria de la pelota en metros."""
    figure = plt.figure(figsize=(9, 6))
    axis = figure.add_subplot(projection="3d")
    x = result.position[:, 0] / 1000
    y = result.position[:, 1] / 1000
    z = result.position[:, 2] / 1000
    axis.plot(x, y, z, color="crimson", label="trayectoria")
    table_x, table_y = np.meshgrid([0, params.table_length / 1000], [0, params.table_width / 1000])
    table_z = np.full_like(table_x, params.table_height / 1000)
    axis.plot_surface(table_x, table_y, table_z, alpha=0.45, color="royalblue")
    net_x = params.table_length / 2000
    axis.plot(
        [net_x, net_x],
        [0, params.table_width / 1000],
        [params.table_height / 1000, (params.table_height + params.net_height) / 1000],
        color="black",
        linewidth=2,
        label="red",
    )
    axis.set(xlabel="X [m]", ylabel="Y [m]", zlabel="Z [m]", title="Trayectoria 3D")
    axis.set_box_aspect((params.table_length, params.table_width, params.table_length))
    axis.legend()
    return figure


def plot_time_series(result: SimulationResult) -> Figure:
    """Muestra posición, velocidad y velocidad angular contra tiempo."""
    figure, axes = plt.subplots(3, 1, figsize=(9, 9), sharex=True, constrained_layout=True)
    labels = ["x", "y", "z"]
    for index, label in enumerate(labels):
        axes[0].plot(result.time, result.position[:, index] / 1000, label=label)
        axes[1].plot(result.time, result.velocity[:, index] / 1000, label=label)
        axes[2].plot(result.time, result.angular_velocity[:, index] / (2 * np.pi), label=label)
    axes[0].set(ylabel="Posición [m]", title="Posición")
    axes[1].set(ylabel="Velocidad [m/s]", title="Velocidad")
    axes[2].set(xlabel="Tiempo [s]", ylabel="Vel. angular [rev/s]", title="Velocidad angular")
    for axis in axes:
        axis.grid(True, alpha=0.3)
        axis.legend(ncol=3)
    return figure
