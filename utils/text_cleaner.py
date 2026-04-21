import re

def clean_text(text):
    """
    Clean resume text while preserving line-by-line structure.
    """

    # convert to lowercase if you want uniform casing
    text = text.lower()

    # remove non-ascii but keep line breaks
    text = re.sub(r'[^\x00-\x7F\n]+', ' ', text)

    # split into lines
    lines = text.splitlines()
    cleaned_lines = []

    for line in lines:
        # fix broken words (join split words across line breaks)
        line = re.sub(r'(\w)\n(\w)', r'\1\2', line)

        # normalize bullets
        line = line.replace("•", "-")

        # remove extra spaces/tabs
        line = re.sub(r'[ \t]+', ' ', line).strip()

        if line:  # skip empty lines
            cleaned_lines.append(line)

    # rejoin with line breaks preserved
    return "\n".join(cleaned_lines).strip()
