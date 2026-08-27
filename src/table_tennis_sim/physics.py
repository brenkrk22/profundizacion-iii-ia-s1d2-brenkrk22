"""Modelo físico y colisiones de la pelota."""

import numpy as np
from numpy.typing import NDArray

from .parameters import SimulationParameters


def linear_acceleration(
    velocity: NDArray[np.float64], omega: NDArray[np.float64], params: SimulationParameters
) -> NDArray[np.float64]:
    """Devuelve aceleración por gravedad, arrastre lineal y efecto Magnus."""
    force = (
        params.gravity * params.ball_mass * np.array([0.0, 0.0, -1.0])
        - params.drag * velocity
        + params.magnus * np.cross(omega, velocity)
    )
    return force / params.ball_mass


def angular_acceleration(omega: NDArray[np.float64], params: SimulationParameters) -> NDArray[np.float64]:
    """Devuelve aceleración angular por arrastre rotacional lineal."""
    return -params.rot_drag * omega / params.rotational_inertia


def collides_with_table(position: NDArray[np.float64], params: SimulationParameters) -> bool:
    """Indica si el centro de la pelota atraviesa la superficie útil de la mesa."""
    return (
        0 < position[0] < params.table_length
        and 0 < position[1] < params.table_width
        and position[2] < params.table_height + params.ball_radius
    )


def resolve_table_collision(
    position: NDArray[np.float64], velocity: NDArray[np.float64], omega: NDArray[np.float64], params: SimulationParameters
) -> tuple[NDArray[np.float64], NDArray[np.float64], NDArray[np.float64]]:
    """Corrige penetración y aplica fricción rotación-traslación y restitución."""
    position = position.copy()
    velocity = velocity.copy()
    omega = omega.copy()
    position[2] = params.table_height + params.ball_radius
    delta_linear_rotation = np.cross(omega, np.array([0.0, 0.0, params.ball_radius])) - np.array(
        [velocity[0], velocity[1], 0.0]
    )
    velocity += params.table_friction * delta_linear_rotation
    omega += params.table_friction * np.cross(delta_linear_rotation, np.array([0.0, 0.0, 1.0])) / params.ball_radius
    velocity[2] = -params.table_restitution * velocity[2]
    return position, velocity, omega


def collides_with_net(position: NDArray[np.float64], params: SimulationParameters) -> bool:
    """Indica la colisión simplificada con el plano de la red."""
    return (
        params.table_length / 2 - params.ball_radius <= position[0] <= params.table_length / 2 + params.ball_radius
        and -params.net_extra < position[1] < params.table_width + params.net_extra
        and params.table_height + params.ball_radius < position[2] < params.table_height + params.net_height + params.ball_radius
    )


def resolve_net_collision(velocity: NDArray[np.float64], omega: NDArray[np.float64], params: SimulationParameters) -> tuple[NDArray[np.float64], NDArray[np.float64]]:
    """Refleja la velocidad X y amortigua el giro, como el script original."""
    velocity = velocity.copy()
    velocity[0] = -params.net_restitution * velocity[0]
    return velocity, params.net_restitution * omega
