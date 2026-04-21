from ats_engine.extraction_engine import process_resumes

def test_extraction():
    results = process_resumes("data")

    assert isinstance(results, dict)
    print("✅ Test passed. Files processed:", len(results))


if __name__ == "__main__":
    test_extraction()