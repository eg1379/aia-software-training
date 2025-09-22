import typing

import pytest

from aviation import transforms
from aviation._engine import SystemsModel


@pytest.fixture
def systems_model() -> SystemsModel:
    return SystemsModel(transforms)


@pytest.mark.parametrize(
    ("inputs", "output", "expected"),
    [
        (
            {"passengers_per_year": 5_000_000_000.0, "days_per_year": 365.0},
            "passengers_per_day",
            13_698_630.0,
        ),
        (
            {
                "days_per_year": 365.0,
                "passengers_per_year": 5_000_000_000.0,
                "seats_per_aircraft": 200.0,
                "flights_per_aircraft_per_day": 3.0,
            },
            "required_global_fleet",
            22_831.0,
        ),
        (
            {
                "passengers_per_day": 13_698_630.0,
                "seats_per_aircraft": 200.0,
                "flights_per_aircraft_per_day": 3.0,
            },
            "required_global_fleet",
            22_831.0,
        ),
    ],
)
def test_transform_evaluation(
    systems_model: SystemsModel,
    inputs: dict[str, typing.Any],
    output: str,
    expected: typing.Any,  # noqa: ANN401
) -> None:
    assert systems_model.evaluate(inputs, output) == pytest.approx(expected, abs=1.0)
