from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    baseline_activities = deepcopy(activities)

    # Arrange: reset global in-memory state before each test.
    activities.clear()
    activities.update(deepcopy(baseline_activities))

    yield

    activities.clear()
    activities.update(deepcopy(baseline_activities))
