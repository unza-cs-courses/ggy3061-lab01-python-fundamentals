"""
Lab 1 Hidden Tests - Python Fundamentals
These tests verify students used their UNIQUE variant values (not defaults/hardcoded).
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


# ============================================================================
# Test Class 1: Variant Configuration Verification
# ============================================================================

class TestHiddenVariantVerification:
    """Verify the variant config is valid and contains all required keys."""

    def test_variant_has_required_keys(self, variant_config):
        """Variant config should have all required parameter keys."""
        required_keys = [
            "sample_depth", "sample_mass", "sample_volume",
            "rock_type", "grade_value"
        ]
        for key in required_keys:
            assert key in variant_config["parameters"], (
                f"Variant config missing required key: {key}"
            )

    def test_sample_depth_in_range(self, expected_depth):
        """sample_depth should be in valid range (150-450)."""
        assert 150 <= expected_depth <= 450, (
            f"sample_depth {expected_depth} is outside valid range [150, 450]"
        )

    def test_sample_mass_in_range(self, expected_mass):
        """sample_mass should be in valid range (10.0-25.0)."""
        assert 10.0 <= expected_mass <= 25.0, (
            f"sample_mass {expected_mass} is outside valid range [10.0, 25.0]"
        )

    def test_sample_volume_in_range(self, expected_volume):
        """sample_volume should be in valid range (3.0-8.0)."""
        assert 3.0 <= expected_volume <= 8.0, (
            f"sample_volume {expected_volume} is outside valid range [3.0, 8.0]"
        )

    def test_rock_type_is_valid(self, expected_rock_type):
        """rock_type should be one of the valid options."""
        valid_types = ["Granite", "Basalt", "Sandstone", "Schist", "Gneiss"]
        assert expected_rock_type in valid_types, (
            f"rock_type '{expected_rock_type}' is not one of {valid_types}"
        )

    def test_grade_value_in_range(self, expected_grade):
        """grade_value should be in valid range (0.5-4.5)."""
        assert 0.5 <= expected_grade <= 4.5, (
            f"grade_value {expected_grade} is outside valid range [0.5, 4.5]"
        )


# ============================================================================
# Test Class 2: Variables - Variant Value Verification
# ============================================================================

class TestHiddenVariables:
    """Verify lab1_variables.py uses the student's actual variant values."""

    def test_output_contains_variant_depth(self, expected_depth):
        """Output should contain the student's assigned depth value."""
        result = run_script("lab1_variables.py")
        assert result.returncode == 0, f"Script failed: {result.stderr}"
        assert str(expected_depth) in result.stdout, (
            f"Expected depth value {expected_depth} not found in output. "
            "Make sure you replaced the placeholder with YOUR assigned value."
        )

    def test_output_contains_variant_grade(self, expected_grade):
        """Output should contain the student's assigned grade value."""
        result = run_script("lab1_variables.py")
        assert result.returncode == 0, f"Script failed: {result.stderr}"
        assert str(expected_grade) in result.stdout, (
            f"Expected grade value {expected_grade} not found in output. "
            "Make sure you replaced the placeholder with YOUR assigned value."
        )

    def test_output_contains_variant_rock_type(self, expected_rock_type):
        """Output should contain the student's assigned rock type."""
        result = run_script("lab1_variables.py")
        assert result.returncode == 0, f"Script failed: {result.stderr}"
        assert expected_rock_type in result.stdout, (
            f"Expected rock_type '{expected_rock_type}' not found in output. "
            "Make sure you replaced the placeholder with YOUR assigned value."
        )

    def test_correct_types_printed(self):
        """Output should display correct Python types for all variables."""
        result = run_script("lab1_variables.py")
        assert result.returncode == 0, f"Script failed: {result.stderr}"
        output_lower = result.stdout.lower()
        assert "<class 'int'>" in result.stdout or "int" in output_lower, (
            "Should show int type for depth"
        )
        assert "<class 'float'>" in result.stdout or "float" in output_lower, (
            "Should show float type for grade"
        )
        assert "<class 'str'>" in result.stdout or "str" in output_lower, (
            "Should show str type for rock_type"
        )
        assert "<class 'bool'>" in result.stdout or "bool" in output_lower, (
            "Should show bool type for processed"
        )

    def test_depth_is_not_default_placeholder(self):
        """Depth should NOT be the default placeholder value (225)."""
        result = run_script("lab1_variables.py")
        assert result.returncode == 0, f"Script failed: {result.stderr}"
        # Check for the specific default pattern: "Depth: 225,"
        # This catches students who did not replace the starter value.
        lines = result.stdout.lower().split('\n')
        for line in lines:
            if 'depth' in line and 'type' in line:
                assert '225' not in line or 'sample_depth' in line, (
                    "Depth still has the default placeholder value (225). "
                    "Replace it with YOUR assigned value from get_variant.py."
                )
                break


# ============================================================================
# Test Class 3: Calculations - Variant Value Verification
# ============================================================================

class TestHiddenCalculations:
    """Verify lab1_calculations.py uses the student's actual variant values."""

    def test_density_matches_variant(self, expected_mass, expected_volume):
        """Density calculation should use the student's variant mass and volume."""
        result = run_script("lab1_calculations.py")
        assert result.returncode == 0, f"Script failed: {result.stderr}"
        expected_density = expected_mass / expected_volume
        density_str = f"{expected_density:.2f}"
        assert density_str in result.stdout, (
            f"Expected density {density_str} (from mass={expected_mass}/volume={expected_volume}) "
            f"not found in output. Make sure you use YOUR assigned values."
        )

    def test_drilling_interval_uses_variant_depth(self, expected_depth):
        """Drilling interval should use the student's variant depth as depth_end."""
        result = run_script("lab1_calculations.py")
        assert result.returncode == 0, f"Script failed: {result.stderr}"
        expected_interval = expected_depth - 100  # depth_start = 100
        assert str(expected_interval) in result.stdout, (
            f"Expected drilling interval {expected_interval} "
            f"(depth_end={expected_depth} - depth_start=100) not found in output."
        )

    def test_average_depth_calculation(self, expected_depth):
        """Average depth should be correctly calculated from depth_start and depth_end."""
        result = run_script("lab1_calculations.py")
        assert result.returncode == 0, f"Script failed: {result.stderr}"
        expected_avg = (100 + expected_depth) / 2
        # Check for the average depth value (could be formatted as int or float)
        avg_str = f"{expected_avg:.1f}"
        avg_int_str = str(int(expected_avg)) if expected_avg == int(expected_avg) else None
        found = avg_str in result.stdout
        if avg_int_str:
            found = found or avg_int_str in result.stdout
        assert found, (
            f"Expected average depth {avg_str} not found in output. "
            f"Average of depth_start=100 and depth_end={expected_depth}."
        )

    def test_core_volume_calculation(self, expected_depth):
        """Core volume should use the correct drilling interval."""
        result = run_script("lab1_calculations.py")
        assert result.returncode == 0, f"Script failed: {result.stderr}"
        interval = expected_depth - 100
        radius = 0.05
        expected_volume = math.pi * radius ** 2 * interval
        vol_str = f"{expected_volume:.4f}"
        assert vol_str in result.stdout, (
            f"Expected core volume {vol_str} not found in output. "
            f"Using radius=0.05, interval={interval}."
        )

    def test_mass_is_not_default(self):
        """Mass should NOT be the default starter value (11.6)."""
        result = run_script("lab1_calculations.py")
        assert result.returncode == 0, f"Script failed: {result.stderr}"
        # Check if density matches the default mass/volume: 11.6/7.8 = 1.487179...
        default_density = f"{11.6 / 7.8:.2f}"  # "1.49"
        output = result.stdout
        # Only fail if BOTH default density and default interval are present
        if default_density in output and "125" in output:
            raise AssertionError(
                "Your calculations appear to use the default starter values "
                "(mass=11.6, volume=7.8). Replace them with YOUR assigned values."
            )

    def test_volume_is_not_default(self):
        """Volume should NOT be the default starter value (7.8)."""
        result = run_script("lab1_calculations.py")
        assert result.returncode == 0, f"Script failed: {result.stderr}"
        # The default density from 11.6/7.8 is 1.49
        # If that exact density is present AND the default interval,
        # the student hasn't changed their values
        default_density = f"{11.6 / 7.8:.2f}"
        output = result.stdout
        if default_density in output and "125" in output:
            raise AssertionError(
                "Your calculations appear to use the default starter values "
                "(mass=11.6, volume=7.8, depth_end=225). "
                "Replace them with YOUR assigned values from get_variant.py."
            )


# ============================================================================
# Test Class 4: Input - Variant Threshold Verification
# ============================================================================

class TestHiddenInput:
    """Verify lab1_input.py handles input and classification correctly."""

    def test_handles_variant_grade_threshold(self, expected_grade):
        """Script should correctly classify using the variant's grade value."""
        result = run_script(
            "lab1_input.py",
            input_data=f"GEO-TEST\nGranite\n{expected_grade}\n200\n"
        )
        assert result.returncode == 0, f"Script failed: {result.stderr}"
        output_lower = result.stdout.lower()
        if expected_grade >= 2.0:
            assert "economic" in output_lower, (
                f"Grade {expected_grade} >= 2.0 should be classified as Economic"
            )
        else:
            assert "sub-economic" in output_lower, (
                f"Grade {expected_grade} < 2.0 should be classified as Sub-economic"
            )

    def test_classification_at_boundary(self):
        """Grade exactly at 2.0 should be classified as Economic."""
        result = run_script(
            "lab1_input.py",
            input_data="GEO-BOUNDARY\nBasalt\n2.0\n300\n"
        )
        assert result.returncode == 0, f"Script failed: {result.stderr}"
        output_lower = result.stdout.lower()
        # At exactly 2.0, classification should be "Economic" (not "Sub-economic")
        assert "economic" in output_lower, (
            "Grade exactly at 2.0 should be classified as Economic"
        )
        # Make sure it's not "sub-economic"
        # Split check: if "sub-economic" is present, that's wrong for grade=2.0
        if "sub-economic" in output_lower:
            raise AssertionError(
                "Grade exactly at 2.0 should be 'Economic', not 'Sub-economic'. "
                "Check your comparison: use >= 2.0 for Economic."
            )

    def test_summary_output_format(self):
        """Summary output should contain all entered values in correct format."""
        result = run_script(
            "lab1_input.py",
            input_data="GEO-FORMAT\nSandstone\n3.25\n400\n"
        )
        assert result.returncode == 0, f"Script failed: {result.stderr}"
        output = result.stdout
        output_lower = output.lower()
        assert "summary" in output_lower, "Should print 'Summary' header"
        assert "geo-format" in output_lower, "Should display the sample ID"
        assert "sandstone" in output_lower, "Should display the rock type"
        assert "3.25" in output, "Should display the grade value"
        assert "400" in output, "Should display the depth value"

    def test_with_alternative_input_values(self, alternative_values):
        """Script should work with alternative valid input values."""
        alt_grade = alternative_values["grade_value"]
        alt_depth = alternative_values["sample_depth"]
        alt_rock = alternative_values["rock_type"]
        result = run_script(
            "lab1_input.py",
            input_data=f"GEO-ALT\n{alt_rock}\n{alt_grade}\n{alt_depth}\n"
        )
        assert result.returncode == 0, f"Script failed: {result.stderr}"
        output_lower = result.stdout.lower()
        assert "summary" in output_lower, "Should print summary for alternative values"
        assert "economic" in output_lower, (
            f"Grade {alt_grade} should produce a classification"
        )


# ============================================================================
# Test Class 5: Strings - Operation Verification
# ============================================================================

class TestHiddenStrings:
    """Verify lab1_strings.py implements all required string operations."""

    def test_string_operations_correct(self):
        """String operations output should be present and correct."""
        result = run_script("lab1_strings.py")
        assert result.returncode == 0, f"Script failed: {result.stderr}"
        output = result.stdout
        # Original ID should be present
        assert "GEO-2024-001" in output, "Should print the original sample ID"

    def test_lowercase_conversion_present(self):
        """Should include lowercase version of the sample ID."""
        result = run_script("lab1_strings.py")
        assert result.returncode == 0, f"Script failed: {result.stderr}"
        output_lower = result.stdout.lower()
        assert "lowercase" in output_lower, "Should label the lowercase operation"
        assert "geo-2024-001" in result.stdout.lower(), (
            "Should show lowercase version of GEO-2024-001"
        )

    def test_replace_operation_present(self):
        """Should include a replace operation replacing GEO with SAMPLE."""
        result = run_script("lab1_strings.py")
        assert result.returncode == 0, f"Script failed: {result.stderr}"
        output = result.stdout
        assert "replace" in output.lower(), "Should label the replace operation"
        assert "SAMPLE" in output, (
            "Should show result of replacing 'GEO' with 'SAMPLE'"
        )

    def test_strip_and_slicing_operations(self):
        """Should include strip and slicing operations."""
        result = run_script("lab1_strings.py")
        assert result.returncode == 0, f"Script failed: {result.stderr}"
        output = result.stdout
        output_lower = output.lower()
        assert "strip" in output_lower, "Should label the strip operation"
        # Slicing: year extraction and first 3 chars
        assert "2024" in output, "Should extract year '2024' via slicing"
        assert "GEO" in output, "Should extract first 3 characters 'GEO' via slicing"


# ============================================================================
# Test Class 6: Integration - Cross-Script Verification
# ============================================================================

class TestHiddenIntegration:
    """Verify all scripts work together and variant values are consistent."""

    def test_all_scripts_run_without_errors(self):
        """All 5 source scripts should execute without errors."""
        scripts = [
            "lab1_setup.py",
            "lab1_variables.py",
            "lab1_calculations.py",
            "lab1_strings.py",
        ]
        for script in scripts:
            result = run_script(script)
            assert result.returncode == 0, (
                f"{script} failed with error: {result.stderr}"
            )
        # lab1_input.py needs input data
        result = run_script(
            "lab1_input.py",
            input_data="GEO-INT\nGranite\n2.5\n200\n"
        )
        assert result.returncode == 0, (
            f"lab1_input.py failed with error: {result.stderr}"
        )

    def test_variable_types_consistent(self):
        """Variable types in lab1_variables.py should be consistent and correct."""
        result = run_script("lab1_variables.py")
        assert result.returncode == 0, f"Script failed: {result.stderr}"
        output = result.stdout
        # Check that the type annotations appear in the output
        type_checks = {
            "int": False,
            "float": False,
            "str": False,
            "bool": False,
        }
        for line in output.split('\n'):
            line_lower = line.lower()
            for t in type_checks:
                if t in line_lower:
                    type_checks[t] = True
        for t, found in type_checks.items():
            assert found, (
                f"Type '{t}' not found in lab1_variables.py output. "
                "All four types (int, float, str, bool) should be displayed."
            )

    def test_variant_values_appear_across_scripts(
        self, expected_depth, expected_mass, expected_rock_type
    ):
        """Variant values should appear in the output of relevant scripts."""
        # Check depth in variables script
        var_result = run_script("lab1_variables.py")
        assert var_result.returncode == 0
        assert str(expected_depth) in var_result.stdout, (
            f"Depth {expected_depth} should appear in lab1_variables.py output"
        )

        # Check rock_type in variables script
        assert expected_rock_type in var_result.stdout, (
            f"Rock type '{expected_rock_type}' should appear in lab1_variables.py output"
        )

        # Check mass-derived density in calculations script
        calc_result = run_script("lab1_calculations.py")
        assert calc_result.returncode == 0
        # The depth-derived interval should appear
        expected_interval = str(expected_depth - 100)
        assert expected_interval in calc_result.stdout, (
            f"Drilling interval {expected_interval} (from depth={expected_depth}) "
            "should appear in lab1_calculations.py output"
        )
