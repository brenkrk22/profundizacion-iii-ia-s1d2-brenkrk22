"""Integración temporal de la simulación."""

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

from .parameters import SimulationParameters
from .physics import (
    angular_acceleration,
    collides_with_net,
    collides_with_table,
    linear_acceleration,
    resolve_net_collision,
    resolve_table_collision,
)


@dataclass
class SimulationResult:
    """Series temporales generadas por la simulación."""

    time: NDArray[np.float64]
    position: NDArray[np.float64]
    velocity: NDArray[np.float64]
    acceleration: NDArray[np.float64]
    orientation: NDArray[np.float64]
    angular_velocity: NDArray[np.float64]
    angular_acceleration: NDArray[np.float64]


def run_simulation(params: SimulationParameters | None = None) -> SimulationResult:
    """Ejecuta Euler explícito conservando la lógica del Live Script MATLAB."""
    params = params or SimulationParameters()
    params.validate()
    time = np.arange(0.0, params.total_time + params.dt / 2, params.dt)
    steps = len(time)
    position = np.zeros((steps, 3))
    velocity = np.zeros((steps, 3))
    acceleration = np.zeros((steps, 3))
    orientation = np.zeros((steps, 3))
    angular_velocity = np.zeros((steps, 3))
    angular_acceleration_values = np.zeros((steps, 3))
    position[0] = params.initial_position
    velocity[0] = params.initial_velocity
    angular_velocity[0] = params.initial_omega

    for index in range(1, steps):
        acceleration[index] = linear_acceleration(velocity[index - 1], angular_velocity[index - 1], params)
        velocity[index] = velocity[index - 1] + acceleration[index] * params.dt
        position[index] = position[index - 1] + velocity[index] * params.dt
        angular_acceleration_values[index] = angular_acceleration(angular_velocity[index - 1], params)
        angular_velocity[index] = angular_velocity[index - 1] + angular_acceleration_values[index] * params.dt
        orientation[index] = orientation[index - 1] + angular_velocity[index] * params.dt

        if collides_with_table(position[index], params):
            position[index], velocity[index], angular_velocity[index] = resolve_table_collision(
                position[index], velocity[index], angular_velocity[index], params
            )
        if collides_with_net(position[index], params):
            velocity[index], angular_velocity[index] = resolve_net_collision(
                velocity[index], angular_velocity[index], params
            )

    return SimulationResult(time, position, velocity, acceleration, orientation, angular_velocity, angular_acceleration_values)
