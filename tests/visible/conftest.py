"""
Pytest configuration for Lab 1 visible tests.
Loads variant configuration if available.
"""

import json
import pytest
from pathlib import Path


@pytest.fixture(scope="session")
def variant_config():
    """Load student's variant configuration."""
    config_path = Path(__file__).parent.parent.parent / ".variant_config.json"
    if config_path.exists():
        with open(config_path) as f:
            return json.load(f)
    # Default values for testing without variant config
    return {
        "parameters": {
            "sample_depth": 250,
            "sample_mass": 15.5,
            "sample_volume": 5.2,
            "rock_type": "Granite",
            "grade_value": 2.45
        }
    }


@pytest.fixture
def expected_depth(variant_config):
    """Return expected depth value."""
    return variant_config["parameters"]["sample_depth"]


@pytest.fixture
def expected_mass(variant_config):
    """Return expected mass value."""
    return variant_config["parameters"]["sample_mass"]


@pytest.fixture
def expected_volume(variant_config):
    """Return expected volume value."""
    return variant_config["parameters"]["sample_volume"]


@pytest.fixture
def expected_rock_type(variant_config):
    """Return expected rock type."""
    return variant_config["parameters"]["rock_type"]


@pytest.fixture
def expected_grade(variant_config):
    """Return expected grade value."""
    return variant_config["parameters"]["grade_value"]
