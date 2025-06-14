import os
from datetime import date

README_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "README.md")
START = "<!-- INTRO-START -->"
END = "<!-- INTRO-END -->"

start_date = date(2019, 8, 7)
experience_years = (date.today() - start_date).days / 365.25
exp_str = f"{experience_years:.1f}"

intro_content = f"""I am a Full-Stack Software Engineer with {exp_str} years of experience in designing and developing scalable applications using Java, Python, and JavaScript. My expertise spans backend frameworks like Django, Flask, FastAPI, Express, Nest.js, and Spring Boot, as well as modern frontend technologies such as React and Next.js. Additionally, I have deep knowledge of SQL (MySQL, PostgreSQL) and NoSQL (MongoDB, DynamoDB) databases, along with cloud computing, primarily on AWS.

I started my career at Startup as a solo software engineer, where I got opportunity to design, develop and deploy my first application to production, gaining valuable experience in product development from the ground up. Currently, at J.P. Morgan, I am actively contributing to AI/ML projects alongside full-stack development, enhancing my skills in machine learning integration into real-world applications.

I am passionate about mentorship and helping aspiring engineers and experienced professionals transition into full-stack, backend, and AI/ML roles."""

with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

start_idx = content.find(START)
end_idx = content.find(END, start_idx)
if start_idx == -1 or end_idx == -1:
    raise ValueError("Intro markers not found in README")

new_content = content[: start_idx + len(START)] + "\n" + intro_content + "\n" + content[end_idx:]

with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(new_content)
