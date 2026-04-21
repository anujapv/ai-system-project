# Day 9

def extract_skills_with_scoring(text):
    """Extracts skills and assigns confidence scores."""
    # Master dictionary built from your JD PDF [cite: 1, 9, 12]
    skill_dict = {
        "Epidemiology": ["disease patterns", "outbreak investigation", "surveillance"],
        "Data Analysis": ["r", "spss", "python", "statistics"],
        "Public Health": ["immunization", "preventive care", "sanitation"]
    }
    
    extracted_results = []
    text_lower = text.lower()
    
    for skill, synonyms in skill_dict.items():
        score = 0.0
        # Check for main skill
        if skill.lower() in text_lower:
            score += 0.7 
        # Handle variations/synonyms 
        for syn in synonyms:
            if syn in text_lower:
                score += 0.3
        
        if score > 0:
            extracted_results.append({
                "skill": skill,
                "confidence_score": min(score, 1.0) # Normalize to 1.0 
            })
            
    return extracted_results