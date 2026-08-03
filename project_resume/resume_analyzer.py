import pandas as pd

# -----------------------------
# Skill Scores
# -----------------------------

skill_score = {
    "Python": 30,
    "SQL": 20,
    "Excel": 10,
    "Power BI": 20,
    "Machine Learning": 40,
    "Java": 15
}

# -----------------------------
# Calculate Resume Score
# -----------------------------

def calculate_score(skills):

    score = 0

    skills = skills.split(",")

    skills = [skill.strip() for skill in skills]

    for skill in skills:

        if skill in skill_score:
            score += skill_score[skill]

    return score


# -----------------------------
# Count Matching Skills
# -----------------------------

def count_matching_skills(skills, required_skills):

    skills = skills.split(",")

    skills = [skill.strip() for skill in skills]

    count = 0

    for skill in required_skills:

        if skill in skills:
            count += 1

    return count


# -----------------------------
# Missing Skills
# -----------------------------

def get_missing_skills(skills, required_skills):

    skills = skills.split(",")

    skills = [skill.strip() for skill in skills]

    missing = []

    for skill in required_skills:

        if skill not in skills:
            missing.append(skill)

    if len(missing) == 0:
        return "None"

    return ", ".join(missing)


# -----------------------------
# Hiring Decision
# -----------------------------

def hiring_decision(score):

    if score >= 100:
        return "Excellent ✅"

    elif score >= 80:
        return "Good 👍"

    elif score >= 60:
        return "Average ⚠"

    else:
        return "Rejected ❌"


# -----------------------------
# Main Analysis Function
# -----------------------------

def analyze_resumes(df, required_skills, min_experience):

    # Calculate Resume Score
    df["Resume Score"] = df["Skills"].apply(calculate_score)

    # Add Experience Bonus
    df["Resume Score"] = (
        df["Resume Score"]
        + (df["Experience"] * 5)
    )

    # Matching Skills
    df["Matching Skills"] = df["Skills"].apply(
        lambda x: count_matching_skills(
            x,
            required_skills
        )
    )

    # Missing Skills
    df["Missing Skills"] = df["Skills"].apply(
        lambda x: get_missing_skills(
            x,
            required_skills
        )
    )

    # Hiring Decision
    df["Decision"] = df["Resume Score"].apply(
        hiring_decision
    )

    # Sort by Resume Score
    ranked_df = df.sort_values(
        by="Resume Score",
        ascending=False
    )

    ranked_df = ranked_df.reset_index(drop=True)

    # Shortlist Candidates
    shortlisted_df = ranked_df[
        (ranked_df["Matching Skills"] >= 2) &
        (ranked_df["Experience"] >= min_experience)
    ]

    shortlisted_df = shortlisted_df.reset_index(drop=True)

    # Best Candidate
    best_candidate = ranked_df.iloc[0]

    return ranked_df, shortlisted_df, best_candidate