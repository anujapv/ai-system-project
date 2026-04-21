def check_education_match(candidate_degrees, required_degree):
    """Matches candidate degree against JD requirements."""
    for edu in candidate_degrees:
        if edu['degree'] == required_degree:
            return 1.0 # Perfect Match
    return 0.5 

def calculate_relevance(candidate_skills, candidate_role, jd_skills, jd_role, total_exp, candidate_edu=None):
    """
    Integrated Scoring Logic:
    - Role match: +2
    - Skill match: +1 per skill
    - Experience threshold: +1
    - Education Match: +1 (Only applied if candidate_edu is provided)
    """
    score = 0
    threshold = 3 
    
    # 1. Role match (+2)
    if jd_role.lower() in candidate_role.lower():
        score += 2
        
    # 2. Skill match (+1 per skill)
    # Using set intersection for efficient matching
    matched_skills = set(candidate_skills) & set(jd_skills)
    score += len(matched_skills)
            
    # 3. Experience threshold (+1)
    if total_exp >= threshold:
        score += 1
        
    # 4. Education Match (+1) - Day 11 Logic
    # Only calculate this if education data is passed to the function
    if candidate_edu is not None:
        # We use your logic to check for a Masters degree
        for edu in candidate_edu:
            if edu['degree'] == "Masters":
                score += 1
                break
            
    return score