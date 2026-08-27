"""Pruebas mínimas de regresión para la simulación."""

from table_tennis_sim import SimulationParameters, run_simulation


def test_simulation_returns_consistent_shapes() -> None:
    params = SimulationParameters(total_time=0.1, dt=0.01)
    result = run_simulation(params)
    assert result.time.shape == (11,)
    assert result.position.shape == (11, 3)
    assert result.velocity.shape == (11, 3)
    assert result.angular_velocity.shape == (11, 3)


def test_gravity_reduces_vertical_velocity_before_collision() -> None:
    params = SimulationParameters(total_time=0.01, dt=0.005)
    result = run_simulation(params)
    assert result.velocity[1, 2] < result.velocity[0, 2]
