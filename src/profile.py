intern_name = "Shivam Jha"
role = "Software Engineering Intern"
department = "Engineering"

skills = [
    "Python",
    "Git",
    "GitHub",
    "Software Engineering"
]


def print_profile():
    print(f"Name: {intern_name}")
    print(f"Role: {role}")
    print(f"Department: {department}")
    print("Skills:")

    for skill in skills:
        print(f"- {skill}")


if __name__ == "__main__":
    print_profile()