import os
import json
from parsers.parser import extract_jd_data
from parsers.section_segmenter import segment_resume
from screening_ai.skill_extractor import extract_skills_with_scoring
from screening_ai.experience_parser import parse_experience_details
from parsers.education_parser import parse_education_and_certs
from scoring.relevance_score import calculate_relevance

def run_ai_recruitment_pipeline(resume_text, jd_path):
    # Day 6 & 7: JD Parsing [cite: 7]
    jd_data = extract_jd_data(jd_path)
    if not jd_data:
        return None

    # Target skills for comparison [cite: 13, 15, 3]
    target_skills = ["Epidemiology", "Data Analysis", "Public Health", "Surveillance"]
    
    # Day 8: Segmentation [cite: 8]
    resume_sections = segment_resume(resume_text)
    
    # Day 9: Skill Extraction [cite: 9]
    extracted_skills = extract_skills_with_scoring(resume_text) 
    candidate_skill_names = [s['skill'] for s in extracted_skills]
    
    # Day 10: Experience Parsing [cite: 10]
    exp_data = parse_experience_details(resume_text)
    candidate_prev_role = "Epidemiologist" 
    
    # Day 11: Education & Certification Parsing [cite: 11]
    # MOVED UP: This must be defined before calling calculate_relevance
    print(f"Step 5: Parsing Education for {os.path.basename(jd_path)}...")
    edu_cert_data = parse_education_and_certs(resume_text)
    
    # Day 10 & 11: Weighted Relevance Calculation [cite: 10, 11]
    # Now edu_cert_data['education'] is available for the 6th argument
    rel_score = calculate_relevance(
        candidate_skill_names, 
        candidate_prev_role, 
        target_skills, 
        jd_data['job_role'], 
        exp_data.get("total_experience", 0),
        edu_cert_data['education']
    )
    
    return {
        "job_role": jd_data['job_role'],
        "relevance_score": rel_score,
        "matched_skills": extracted_skills,
        "experience_years": exp_data.get("total_experience", 0),
        "academic_profile": edu_cert_data
    }

if __name__ == "__main__":
    # 1. Define folder paths
    output_folder = "outputs"
    output_filename = "day11_output.json"
    output_path = os.path.join(output_folder, output_filename)
    
    jd_folder = "data/job_descriptions/"
    resume_folder = "data/resumes/" 

    # 2. Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created new folder: {output_folder}")

    all_rankings = []

    # Check if both data folders exist
    if os.path.exists(jd_folder) and os.path.exists(resume_folder):
        
        # OUTER LOOP: Iterate through each resume
        for res_file in os.listdir(resume_folder):
            if res_file.endswith(".txt"):
                resume_path = os.path.join(resume_folder, res_file)
                
                with open(resume_path, 'r', encoding='utf-8') as f:
                    resume_text = f.read()
                
                print(f"--- Processing Candidate: {res_file} ---")

                # INNER LOOP: Match current resume against every JD
                for jd_file in os.listdir(jd_folder):
                    if jd_file.endswith(".txt"):
                        jd_path = os.path.join(jd_folder, jd_file)
                        
                        result = run_ai_recruitment_pipeline(resume_text, jd_path)
                        
                        if result:
                            # Tag the result with the candidate's filename
                            result['candidate_filename'] = res_file
                            all_rankings.append(result)

        # 3. Final Sorting and Saving
        # Sort by relevance_score (Highest matches first)
        all_rankings.sort(key=lambda x: x['relevance_score'], reverse=True)

        with open(output_path, 'w') as f:
            json.dump(all_rankings, f, indent=4)
            
        print(f"\nSuccess! Processed {len(all_rankings)} total combinations.")
        print(f"Results saved to: {output_path}")
        
    else:
        if not os.path.exists(jd_folder):
            print(f"Error: JD directory {jd_folder} not found.")
        if not os.path.exists(resume_folder):
            print(f"Error: Resume directory {resume_folder} not found.")