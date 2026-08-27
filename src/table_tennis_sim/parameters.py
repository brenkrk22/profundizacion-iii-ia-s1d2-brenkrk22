"""Parámetros de la simulación en las unidades del script MATLAB original."""

from dataclasses import dataclass, field

import numpy as np
from numpy.typing import NDArray


@dataclass
class SimulationParameters:
    """Parámetros físicos y condiciones iniciales (g, mm, s y mN)."""

    ball_mass: float = 2.7
    ball_radius: float = 20.25
    table_restitution: float = 0.77
    net_restitution: float = 0.5
    drag: float = 2.7
    rot_drag: float = 350.0
    magnus: float = 0.01
    table_friction: float = 0.25
    table_length: float = 2740.0
    table_width: float = 1525.0
    table_height: float = 760.0
    net_height: float = 152.5
    net_extra: float = 180.0
    gravity: float = 9800.0
    dt: float = 0.005
    total_time: float = 1.5
    initial_position: NDArray[np.float64] = field(
        default_factory=lambda: np.array([0.0, 1525.0 / 2, 760.0 + 2 * 152.5])
    )
    initial_velocity: NDArray[np.float64] = field(
        default_factory=lambda: np.array([7000.0, -3000.0, -3000.0])
    )
    initial_omega: NDArray[np.float64] = field(
        default_factory=lambda: np.array([0.0, 0.0, 75.0]) * 2 * np.pi
    )

    @property
    def rotational_inertia(self) -> float:
        """Momento de inercia de la esfera según la aproximación original."""
        return (2.0 / 3.0) * self.ball_mass * self.ball_radius**2

    def validate(self) -> None:
        """Valida los parámetros que harían fallar la integración."""
        if self.ball_mass <= 0 or self.ball_radius <= 0:
            raise ValueError("La masa y el radio de la pelota deben ser positivos.")
        if self.dt <= 0 or self.total_time <= 0:
            raise ValueError("dt y total_time deben ser positivos.")
        for value in (self.table_restitution, self.net_restitution, self.table_friction):
            if value < 0:
                raise ValueError("Los coeficientes de restitución y fricción no pueden ser negativos.")
