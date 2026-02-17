#!/usr/bin/env python3
"""
Lab 1 - Task 5: String Operations
GGY3061 Python Programming for Earth Sciences

Instructions:
1. Demonstrate various string manipulation methods
2. Use your assigned rock_type from get_variant.py in the description

TODO: Complete the string operations below
"""

# Sample data
sample_id = 'GEO-2024-001'
description = '  High grade sample  '  # You can modify this to include your rock_type

# --- Example (given) ---
print(f'Original ID: {sample_id}')

# --- Operation 1: Case conversion ---
# TODO: Print the lowercase version of sample_id
# Expected output format:  Lowercase: geo-2024-001
# Hint: use the .lower() string method


# --- Operation 2: Replace ---
# TODO: Replace "GEO" with "SAMPLE" in sample_id and print the result
# Expected output format:  Replace: SAMPLE-2024-001
# Hint: use the .replace() string method


# --- Operation 3: Stripping whitespace ---
# TODO: Print description before and after stripping whitespace
# Expected output:
#   Before strip: "  High grade sample  "
#   After strip: "High grade sample"
# Hint: use the .strip() string method


# --- Operation 4: String slicing ---
# TODO: Extract the year (characters at positions 4 through 7) from sample_id
# Expected output format:  Year from ID: 2024
# Hint: use slice notation sample_id[start:end]

# TODO: Extract the first 3 characters from sample_id
# Expected output format:  First 3 chars: GEO
# Hint: use slice notation sample_id[:end]


# --- Operation 5: String concatenation ---
# TODO: Combine sample_id and the stripped description with ' - ' between them
# Expected output format:  Full name: GEO-2024-001 - High grade sample
# Hint: use + to join strings, and .strip() to remove whitespace from description

