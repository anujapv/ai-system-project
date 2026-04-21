# Day 11

import re

def parse_education_and_certs(text):
    """Detects degrees and certifications from resume text."""
    # 1. Regex for Degree Types & Fields
    degree_patterns = {
        "Masters": r"(?i)MPH|Master of Public Health|MSc|MD|MS",
        "Bachelors": r"(?i)MBBS|BDS|BSc Nursing|BAMS|BHMS|BSc",
        "PhD": r"(?i)PhD|Doctorate"
    }
    year_pattern = r"\b(?:19|20)\d{2}\b"
    extracted_edu = []
    # Normalizing Degree Names
    for degree_type, pattern in degree_patterns.items():
        match = re.search(pattern, text)
        if match:
            # We look for the year specifically near the degree or at the end of the line
            all_years = re.findall(year_pattern, text)
            extracted_edu.append({
                "degree": degree_type,
                "raw_match": match.group(),
                "year": all_years[-1] if all_years else "Unknown"
            })        
    # 3. Certification Extraction & Tagging
    cert_keywords = {
        "Clinical": ["CHO Certification", "Bridge Program", "GCP"],
        "Technical": ["Data Analyst Certification", "Tableau Certified"],
        "Public Health": ["FETP", "IDSP Training", "Sanitation Certificate"]
    }
    found_certs = []
    for category, keywords in cert_keywords.items():
        for kw in keywords:
            if kw.lower() in text.lower():
                found_certs.append({
                    "certification": kw,
                    "category": category # Tagging relevance
                })           
    return {
        "education": extracted_edu,
        "certifications": found_certs
    }