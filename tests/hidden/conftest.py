"""
Pytest configuration for Lab 1 hidden tests.
Loads variant configuration and provides fixtures for verifying
students used their unique assigned values.
"""

import json
import pytest
from pathlib import Path


# Path to student source files
SRC_DIR = Path(__file__).parent.parent.parent / "src"


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
    """Return expected depth value from variant config."""
    return variant_config["parameters"]["sample_depth"]


@pytest.fixture
def expected_mass(variant_config):
    """Return expected mass value from variant config."""
    return variant_config["parameters"]["sample_mass"]


@pytest.fixture
def expected_volume(variant_config):
    """Return expected volume value from variant config."""
    return variant_config["parameters"]["sample_volume"]


@pytest.fixture
def expected_rock_type(variant_config):
    """Return expected rock type from variant config."""
    return variant_config["parameters"]["rock_type"]


@pytest.fixture
def expected_grade(variant_config):
    """Return expected grade value from variant config."""
    return variant_config["parameters"]["grade_value"]


@pytest.fixture
def alternative_values():
    """
    Provide alternative valid parameter values for testing against hardcoded answers.
    These are different from the defaults in the starter code, ensuring students
    who hardcode values instead of using their variant will fail these checks.
    """
    return {
        "sample_depth": 375,
        "sample_mass": 19.3,
        "sample_volume": 6.1,
        "rock_type": "Schist",
        "grade_value": 3.78
    }
