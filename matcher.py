def match_score(resume, jd):
    jd_keywords = jd.lower().split()
    resume_skills = resume.get("skills", [])
    match = set(jd_keywords).intersection(set(resume_skills))
    return round(len(match) / len(jd_keywords) * 100, 2) if jd_keywords else 0