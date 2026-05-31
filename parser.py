import re

def extract_and_structure(text):
    # Split into bullet points and achievements
    lines = text.split('\n')
    responsibilities = []
    achievements = []

    for line in lines:
        line = line.strip()
        if line.startswith('●'):
            responsibilities.append(line[1:].strip())
        elif line.startswith('•'):
            achievements.append(line[1:].strip())

    # Structure the data
    structured_data = {
        "Responsibilities": responsibilities,
        "Achievements": achievements
    }
    return structured_data

# Example usage
input_text = """
● Delivered lectures and hands-on demonstrations in Applied Thermodynamics to National Diploma (II) Marine Engineering
students, emphasizing real-world applications, energy systems behavior, and engineering problem-solving.
● Led practical training on outboard engine maintenance and repair, strengthening students’ technical competency in marine
machinery operation, diagnostics, and reliability practices.
● Contributed to academic materials review by participating in docket reviews, ensuring course materials remained current,
industry-relevant, and aligned with national engineering education standards.
● Organized and facilitated technical seminars in collaboration with the Nigerian Society of Engineers (NSE), enhancing students’
exposure to professional practice, engineering ethics, and emerging sustainability trends.
Achievement:
• Organized and led two engineering seminars for the School of Marine Engineering: “Roles of Engineers in Society” and “What is
Sustainability?” in partnership with NSE and COREN, promoting professional development and awareness of sustainability within
engineering practice.
• Achieved a 96% pass rate in Applied Thermodynamics, reflecting instructional effectiveness, curriculum rigor, and strong student
engagement.
"""

structured_output = extract_and_structure(input_text)

# Print as JSON
import json
print(json.dumps(structured_output, indent=2))
