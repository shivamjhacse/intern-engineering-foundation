from src.profile import intern_name, role, department, skills
from src.profile import print_profile


def test_profile_data():
    assert intern_name == "Shivam Jha"
    assert role == "Software Engineering Intern"
    assert department == "Engineering"
    assert len(skills) > 0


def test_profile_has_skills():
    assert "Python" in skills
    assert "Git" in skills
    assert "GitHub" in skills
#python3 -m tests.test_profile
#python3 -m pytest

print_profile()