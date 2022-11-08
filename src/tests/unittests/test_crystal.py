import pytest 
from src.crystal.crystal_calculation import model

@pytest.mark.parametrize(
    "radius, origin",
    (
        [4, (0, 0)],
        [4.8, (0, 0)],
        [-6, (1, 7)],
        [8, (0.5, 0.3)],
        [5, (-4, -0.2)],
    )
)
def test_inject_circle(radius, origin):
    inj_cir = model.InjectionCircle(inject_radius=radius, origin=origin)
    particle = inj_cir.inject_particle()
    assert type(particle) == tuple
    assert type(particle[0]) == int
    assert type(particle[1]) == int
    assert len(particle) == 2
    second_particle = inj_cir.inject_particle()
    assert second_particle != particle

@pytest.mark.parametrize(
    "radius, result",
    (
        [4, 6], 
        [4.8, 7], 
        [6, 8],
        [-8, 10],
        [0.6, 3]
    )
)
def test_update_radius(radius, result):
    inj_cir = model.InjectionCircle(inject_radius=radius, origin=(0, 0))
    inj_cir.update_radius()
    assert inj_cir.inject_radius == result

def test_grow():
    pass

