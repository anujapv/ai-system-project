# Day 10

import re

def parse_experience_details(text):
    """Extracts durations and calculates total experience."""
    # Find years in the text (e.g., 2023-2025)
    years = re.findall(r"\b(20\d{2})\b", text)
    
    if len(years) >= 2:
        # Simple math: Max year - Min year 
        total_years = int(max(years)) - int(min(years))
    else:
        total_years = 0
        
    return {"total_experience": total_years}

def calculate_relevance(candidate_skills, jd_skills):
    """Computes relevance score for specific job roles."""
    # Mathematical set intersection for relevance
    match_count = len(set(candidate_skills) & set(jd_skills))
    relevance_score = (match_count / len(jd_skills)) if jd_skills else 0
    return round(relevance_score, 2)