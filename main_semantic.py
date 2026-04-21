import os
import json
# Import your existing modules
from parsers.parser import extract_jd_data
from screening_ai.skill_extractor import extract_skills_with_scoring
from screening_ai.experience_parser import parse_experience_details
from parsers.education_parser import parse_education_and_certs
from scoring.relevance_score import calculate_relevance
# Import the new Day 12 module
from scoring.semantic_engine import calculate_semantic_similarity

def run_semantic_pipeline(resume_text, jd_text, jd_path):
    # 1. Reuse Day 6-11 logic
    jd_data = extract_jd_data(jd_path)
    if not jd_data: return None

    target_skills = ["Epidemiology", "Data Analysis", "Public Health", "Surveillance"]
    extracted_skills = extract_skills_with_scoring(resume_text) 
    candidate_skill_names = [s['skill'] for s in extracted_skills]
    exp_data = parse_experience_details(resume_text)
    edu_cert_data = parse_education_and_certs(resume_text)
    
    # 2. Day 11 Point-based Score
    rel_points = calculate_relevance(
        candidate_skill_names, 
        "Epidemiologist", # Placeholder role
        target_skills, 
        jd_data['job_role'], 
        exp_data.get("total_experience", 0),
        edu_cert_data['education']
    )

    # 3. Day 12 Semantic Similarity Score
    # This compares the WHOLE text of the resume to the WHOLE JD
    semantic_score = calculate_semantic_similarity(resume_text, jd_text)
    
    return {
        "job_role": jd_data['job_role'],
        "relevance_points": rel_points,
        "semantic_similarity": round(semantic_score * 100, 2), # Convert to percentage
        "experience_years": exp_data.get("total_experience", 0),
        "academic_profile": edu_cert_data
    }

if __name__ == "__main__":
    output_dir = "outputs"
    if not os.path.exists(output_dir): os.makedirs(output_dir)

    jd_folder = "data/job_descriptions/"
    resume_folder = "data/resumes/"
    day12_results = []

    if os.path.exists(jd_folder) and os.path.exists(resume_folder):
        for res_file in os.listdir(resume_folder):
            if res_file.endswith(".txt"):
                res_path = os.path.join(resume_folder, res_file)
                with open(res_path, 'r', encoding='utf-8') as f:
                    resume_text = f.read()

                for jd_file in os.listdir(jd_folder):
                    if jd_file.endswith(".txt"):
                        jd_path = os.path.join(jd_folder, jd_file)
                        with open(jd_path, 'r', encoding='utf-8') as f:
                            jd_text = f.read()
                        
                        # Process with Semantic Engine
                        result = run_semantic_pipeline(resume_text, jd_text, jd_path)
                        if result:
                            result['candidate'] = res_file
                            day12_results.append(result)

        # Sort by Semantic Similarity first
        day12_results.sort(key=lambda x: x['semantic_similarity'], reverse=True)

        output_path = os.path.join(output_dir, "day12_semantic_output.json")
        with open(output_path, 'w') as f:
            json.dump(day12_results, f, indent=4)
            
        print(f"Day 12 Success! Semantic results saved to {output_path}")