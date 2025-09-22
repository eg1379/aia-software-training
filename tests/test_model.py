import typing

import camia_model as model
import pytest

from aviation import transforms


@model.transform
def add(x: float, y: float) -> float:
    return x + y


@pytest.mark.parametrize("transform", transforms)
def test_transform_decorator(transform: model.StandardTransform[typing.Any, ...]) -> None:
    assert model.is_transform(transform)
