import os
from parsers.resume_reader import extract_text
from utils.text_cleaner import clean_text

def process_resumes(folder_path):
    results = {}

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if file.endswith(".pdf") or file.endswith(".docx"):

            print(f"Processing: {file}")  # debug

            raw_text = extract_text(file_path)
            cleaned_text = clean_text(raw_text)

            results[file] = {
                "raw_text": raw_text,
                "cleaned_text": cleaned_text
            }

    return results