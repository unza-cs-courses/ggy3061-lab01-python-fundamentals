#!/usr/bin/env python3
"""
Deterministic Variant Computation for GGY3061 Assignments

This module computes student variants on-the-fly based on the repository name.
No pre-committed variant file is required - values are derived deterministically.

Usage:
    # As a script (for students to see their values):
    python scripts/get_variant.py
    
    # As a module (for tests):
    from scripts.get_variant import get_my_variant, get_variant_for_student
    variant = get_my_variant()
    params = variant['parameters']
"""

import hashlib
import random
import json
import os
import subprocess
from pathlib import Path
from typing import Dict, Any, Optional


# ============================================================================
# CONFIGURATION - Must match across all assignments
# ============================================================================

SEED_SALT = "GGY3061_2026"
ASSIGNMENT_ID = "lab01"
VARIANT_STRATEGY = "grouped"
NUM_GROUPS = 10


# ============================================================================
# VARIANT COMPUTATION (Deterministic)
# ============================================================================

def compute_seed(student_id: str) -> int:
    """Compute deterministic seed from student identifier."""
    combined = f"{ASSIGNMENT_ID}:{SEED_SALT}:{student_id}"
    hash_bytes = hashlib.sha256(combined.encode()).digest()
    return int.from_bytes(hash_bytes[:8], byteorder='big')


def compute_group(seed: int) -> int:
    """Assign student to a variant group."""
    return seed % NUM_GROUPS


def generate_parameters(rng, group_id):
    """Generate Lab 1 specific parameters deterministically."""
    return {
        'sample_depth': rng.randint(150, 450),
        'sample_mass': round(rng.uniform(10.0, 25.0), 1),
        'sample_volume': round(rng.uniform(3.0, 8.0), 1),
        'rock_type': rng.choice(['Granite', 'Basalt', 'Sandstone', 'Schist', 'Gneiss']),
        'grade_value': round(rng.uniform(0.5, 4.5), 2),
    }


def get_variant_for_student(student_id: str) -> Dict[str, Any]:
    """
    Compute the variant for a given student ID.
    
    Args:
        student_id: Student's GitHub username or identifier
        
    Returns:
        Dict with student_id, variant_seed, group_id, and parameters
    """
    seed = compute_seed(student_id)
    group_id = compute_group(seed) if VARIANT_STRATEGY != 'unique' else None
    
    # Create seeded random instance for reproducibility
    rng = random.Random(seed)
    
    # Generate parameters
    parameters = generate_parameters(rng, group_id)
    
    return {
        'student_id': student_id,
        'variant_seed': seed,
        'group_id': group_id,
        'parameters': parameters
    }


# ============================================================================
# STUDENT IDENTIFICATION
# ============================================================================

def get_repo_name() -> Optional[str]:
    """Get the repository name from git or environment."""
    github_repo = os.environ.get('GITHUB_REPOSITORY')
    if github_repo:
        return github_repo.split('/')[-1]
    
    try:
        result = subprocess.run(
            ['git', 'remote', 'get-url', 'origin'],
            capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            url = result.stdout.strip()
            repo = url.rstrip('.git').split('/')[-1]
            return repo
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    
    return Path.cwd().name


def extract_username_from_repo(repo_name: str) -> str:
    """Extract the student username from the repository name."""
    if not repo_name:
        return "unknown"
    parts = repo_name.split('-')
    if len(parts) > 1:
        return parts[-1]
    return repo_name


def get_my_username() -> str:
    """Get the current student's username from the repo name."""
    repo_name = get_repo_name()
    if repo_name:
        return extract_username_from_repo(repo_name)
    return "unknown"


def get_my_variant() -> Dict[str, Any]:
    """Get the variant for the current student (auto-detected from repo name)."""
    username = get_my_username()
    return get_variant_for_student(username)


# ============================================================================
# CLI - For students to see their values
# ============================================================================

def print_assignment_values():
    """Print the student's assignment values in a friendly format."""
    variant = get_my_variant()
    params = variant['parameters']
    
    print("=" * 60)
    print("YOUR ASSIGNMENT VALUES - Lab 1: Python Fundamentals")
    print("=" * 60)
    print(f"\nStudent: {variant['student_id']}")
    print(f"Variant Group: {variant['group_id']}")
    print()
    print("Use these EXACT values in your code:")
    print("-" * 40)

    print(f"  sample_depth  = {params['sample_depth']}     # meters (int)")
    print(f"  sample_mass   = {params['sample_mass']}    # kg (float)")
    print(f"  sample_volume = {params['sample_volume']}     # cubic meters (float)")
    print(f"  rock_type     = '{params['rock_type']}'  # string")
    print(f"  grade_value   = {params['grade_value']}    # percentage (float)")
    print("-" * 40)
    print()
    print("These values are UNIQUE to you. Using someone else's")
    print("values will cause hidden tests to FAIL.")
    print()
    print("JSON format (for reference):")
    print(json.dumps(variant, indent=2))


if __name__ == "__main__":
    print_assignment_values()
