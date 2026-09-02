from src.profile import intern_name, role, department, skills
from src.profile import print_profile


def test_profile_data():
    assert intern_name == "Shivam Jha"
    assert role == "Software Engineering Intern"
    assert department == "Engineering"
    assert len(skills) > 0
#python3 -m tests.test_profile


print_profile()