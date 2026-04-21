import json
from ats_engine.extraction_engine import process_resumes

folder_path = "data"

results = process_resumes(folder_path)

print(results["resume.pdf"]["cleaned_text"])
# Save output
with open("resume_output.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4,ensure_ascii=False)

print("✅ Extraction completed. Check output.json")