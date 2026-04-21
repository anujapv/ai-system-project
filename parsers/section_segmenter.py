# Day 8

import re

def segment_resume(text):
    """Identifies major resume sections using regex."""
    # Define common headers found in layouts 
    headers = {
        "skills": r"(?i)skills|competencies|technologies",
        "experience": r"(?i)work experience|employment|history",
        "education": r"(?i)education|academic background",
        "projects": r"(?i)projects|academic projects"
    }
    
    segments = {}
    # Split logic: find headers and tag the text blocks 
    for section, pattern in headers.items():
        if re.search(pattern, text):
            # In a full version, you would slice the text from one header to the next
            segments[section] = "Extracted text for " + section
            
    return segments