# Day 6,7

import json
import os

def extract_jd_data(file_path):
    """Reads a .txt job description and structures it."""
    # Check if the file actually exists to avoid FileNotFoundError
    if not os.path.exists(file_path):
        print(f"Error: The file {file_path} was not found.")
        return None

    with open(file_path, 'r', encoding='utf-8') as file:
        full_text = file.read()

    # Day 7: Structured metadata for the pipeline
    filename = os.path.basename(file_path)
    structured_jd = {
        "job_role": filename.replace(".txt", "").replace("_", " "),
        "raw_text": full_text,
        "processed_at": "2026-04-20"
    }
    return structured_jd