print("------------------------------------")
print("")
print(" Welcome to Digital Resume Builder!")
print("")
print("------------------------------------")
print("")
print("")
name = input("Enter your full name: ")
email = input("Enter your Email address: ")
phone_number = input("Enter your phone number: ")
location = input("Enter your current house location: ")
print("")
print("")
print("------------------------------------")
print("")
print("")
add_experience = input("Do you want to add work experience? (yes/no): ")

if add_experience.lower() == "yes":
    job_title = input("Enter your job title: ")
    company = input("Enter company name: ")
    years = input("Enter years worked (e.g., 2023–2024): ")

    experience = f"{job_title}, {company} ({years})"
else:
    experience = "No work experience added."
print("")
print("")
print("------------------------------------")
print("")
print("")
add_education = input("Do you want to add education details? (yes/no): ")

if add_education.lower() == "yes":
    degree = input("Enter your degree (e.g., Matric, BSCS): ")
    institute = input("Enter your institute name: ")
    year = input("Enter year of completion: ")

    education = f"{degree}, {institute} ({year})"
else:
    education = "No education info provided."
print("")
print("")
print("------------------------------------")
print("")
print("")
skills = input("Enter your skills (separated by commas): ")
print("")
print("")
print("------------------------------------")
print("")
print("")
print("Generating your resume...")

with open("resume.txt", "w", encoding="utf-8") as file:
    file.write("===========================\n")
    file.write(f"        {name}\n")
    file.write("===========================\n\n")

    file.write(f"📧 Email: {email}\n")
    file.write(f"📱 Phone: {phone_number}\n")
    file.write(f"📍 Location: {location}\n\n")

    file.write("💼 Work Experience:\n")
    file.write(f"- {experience}\n\n")

    file.write("🎓 Education:\n")
    file.write(f"- {education}\n\n")

    file.write("🛠 Skills:\n")
    file.write(f"{skills}\n")

print("✅ Resume generated successfully! Check resume.txt")