"""
Lab 1 Visible Tests - Python Fundamentals
These tests verify basic functionality and correct use of assigned values.
"""

import subprocess
import sys
import math
from pathlib import Path

SRC_DIR = Path(__file__).parent.parent.parent / "src"


def run_script(script_name, input_data=None):
    """Run a Python script and capture output."""
    script_path = SRC_DIR / script_name
    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True,
        input=input_data,
        timeout=10
    )
    return result


class TestTask1Setup:
    """Tests for Task 1: Environment Verification"""

    def test_setup_file_exists(self):
        """lab1_setup.py file should exist"""
        assert (SRC_DIR / "lab1_setup.py").exists(), "lab1_setup.py not found in src/"

    def test_setup_runs_without_error(self):
        """lab1_setup.py should run without errors"""
        result = run_script("lab1_setup.py")
        assert result.returncode == 0, f"Script failed with error: {result.stderr}"

    def test_setup_prints_python_version(self):
        """lab1_setup.py should print Python version"""
        result = run_script("lab1_setup.py")
        assert "python version" in result.stdout.lower(), "Should print Python version"

    def test_setup_success_message(self):
        """lab1_setup.py should print success message"""
        result = run_script("lab1_setup.py")
        assert "successful" in result.stdout.lower(), "Should print success message"


class TestTask2Variables:
    """Tests for Task 2: Variables and Data Types"""

    # Default placeholder values in the starter — students MUST change these
    _STARTER_DEFAULTS = {"depth": "225", "grade": "0.88", "rock": "granite"}

    def test_variables_file_exists(self):
        """lab1_variables.py file should exist"""
        assert (SRC_DIR / "lab1_variables.py").exists(), "lab1_variables.py not found in src/"

    def test_variables_runs_without_error(self):
        """lab1_variables.py should run without errors"""
        result = run_script("lab1_variables.py")
        assert result.returncode == 0, f"Script failed with error: {result.stderr}"

    def test_values_are_not_defaults(self):
        """Student must replace placeholder values with their assigned values"""
        result = run_script("lab1_variables.py")
        output = result.stdout
        # If ALL three default placeholder values are still present, the
        # student hasn't customised their code yet.
        all_defaults = all(
            v in output.lower() for v in self._STARTER_DEFAULTS.values()
        )
        assert not all_defaults, (
            "You must replace the default values (depth=225, grade=0.88, "
            "rock_type='Granite') with YOUR assigned values from get_variant.py"
        )

    def test_prints_depth_with_type(self):
        """Should print depth with int type"""
        result = run_script("lab1_variables.py")
        assert "depth" in result.stdout.lower(), "Should print depth"
        assert "int" in result.stdout.lower(), "Should show int type"

    def test_prints_grade_with_type(self):
        """Should print grade with float type"""
        result = run_script("lab1_variables.py")
        assert "grade" in result.stdout.lower(), "Should print grade"
        assert "float" in result.stdout.lower(), "Should show float type"

    def test_prints_rock_type_with_type(self):
        """Should print rock type with str type"""
        result = run_script("lab1_variables.py")
        assert "rock" in result.stdout.lower(), "Should print rock type"
        assert "str" in result.stdout.lower(), "Should show str type"

    def test_prints_processed_with_type(self):
        """Should print processed status with bool type"""
        result = run_script("lab1_variables.py")
        assert "processed" in result.stdout.lower(), "Should print processed"
        assert "bool" in result.stdout.lower(), "Should show bool type"


class TestTask3Calculations:
    """Tests for Task 3: Arithmetic Expressions"""

    # Density from starter defaults: 11.6 / 7.8 ≈ 1.487179 → "1.49"
    _DEFAULT_DENSITY = "1.49"
    # Interval from starter defaults: 225 - 100 = 125
    _DEFAULT_INTERVAL = "125"

    def test_calculations_file_exists(self):
        """lab1_calculations.py file should exist"""
        assert (SRC_DIR / "lab1_calculations.py").exists(), "lab1_calculations.py not found in src/"

    def test_calculations_runs_without_error(self):
        """lab1_calculations.py should run without errors"""
        result = run_script("lab1_calculations.py")
        assert result.returncode == 0, f"Script failed with error: {result.stderr}"

    def test_calculations_not_defaults(self):
        """Student must use their assigned values, not starter defaults"""
        result = run_script("lab1_calculations.py")
        output = result.stdout
        has_default_density = self._DEFAULT_DENSITY in output
        has_default_interval = self._DEFAULT_INTERVAL in output
        assert not (has_default_density and has_default_interval), (
            "Your calculations use the default starter values. "
            "Replace mass, volume, and depth_end with YOUR values from get_variant.py"
        )

    def test_prints_density(self):
        """Should print density calculation"""
        result = run_script("lab1_calculations.py")
        assert "density" in result.stdout.lower(), "Should print density"
        assert "kg/m3" in result.stdout.lower(), "Should include units"

    def test_prints_drilling_interval(self):
        """Should print drilling interval"""
        result = run_script("lab1_calculations.py")
        assert "interval" in result.stdout.lower(), "Should print interval"
        assert "meters" in result.stdout.lower(), "Should include units"

    def test_prints_average_depth(self):
        """Should print average depth"""
        result = run_script("lab1_calculations.py")
        assert "average" in result.stdout.lower(), "Should print average"

    def test_prints_core_volume(self):
        """Should print core volume"""
        result = run_script("lab1_calculations.py")
        assert "core volume" in result.stdout.lower(), "Should print core volume"


class TestTask4Input:
    """Tests for Task 4: User Input and Output"""

    def test_input_file_exists(self):
        """lab1_input.py file should exist"""
        assert (SRC_DIR / "lab1_input.py").exists(), "lab1_input.py not found in src/"

    def test_input_runs_with_sample_data(self):
        """lab1_input.py should handle input correctly"""
        test_input = "GEO-001\nGranite\n2.5\n200\n"
        result = run_script("lab1_input.py", input_data=test_input)
        assert result.returncode == 0, f"Script failed: {result.stderr}"

    def test_input_shows_summary(self):
        """Should show sample summary"""
        test_input = "GEO-001\nGranite\n2.5\n200\n"
        result = run_script("lab1_input.py", input_data=test_input)
        assert "summary" in result.stdout.lower(), "Should print summary header"

    def test_classification_economic(self):
        """Should classify grade >= 2.0 as Economic"""
        test_input = "GEO-001\nGranite\n2.5\n200\n"
        result = run_script("lab1_input.py", input_data=test_input)
        assert "economic" in result.stdout.lower(), "Should show classification"

    def test_classification_subeconomic(self):
        """Should classify grade < 2.0 as Sub-economic"""
        test_input = "GEO-001\nGranite\n1.5\n200\n"
        result = run_script("lab1_input.py", input_data=test_input)
        assert "sub-economic" in result.stdout.lower(), "Should classify as sub-economic"


class TestTask5Strings:
    """Tests for Task 5: String Operations"""

    def test_strings_file_exists(self):
        """lab1_strings.py file should exist"""
        assert (SRC_DIR / "lab1_strings.py").exists(), "lab1_strings.py not found in src/"

    def test_strings_runs_without_error(self):
        """lab1_strings.py should run without errors"""
        result = run_script("lab1_strings.py")
        assert result.returncode == 0, f"Script failed: {result.stderr}"

    def test_prints_original_id(self):
        """Should print original sample ID"""
        result = run_script("lab1_strings.py")
        assert "geo-2024-001" in result.stdout.lower(), "Should print original ID"

    def test_prints_lowercase(self):
        """Should print lowercase version"""
        result = run_script("lab1_strings.py")
        assert "lowercase" in result.stdout.lower(), "Should show lowercase operation"

    def test_prints_replace(self):
        """Should demonstrate string replace"""
        result = run_script("lab1_strings.py")
        assert "replace" in result.stdout.lower(), "Should show replace operation"
        assert "sample" in result.stdout.lower(), "Should show replaced text"

    def test_prints_strip(self):
        """Should demonstrate strip method"""
        result = run_script("lab1_strings.py")
        assert "strip" in result.stdout.lower(), "Should show strip operation"

    def test_prints_slicing(self):
        """Should demonstrate string slicing"""
        result = run_script("lab1_strings.py")
        assert "year from id" in result.stdout.lower(), "Should show extracted year with label"
        assert "first 3 chars" in result.stdout.lower(), "Should show first 3 chars with label"
