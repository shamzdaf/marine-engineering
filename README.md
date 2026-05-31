# Marine Engineering Achievements & Responsibilities

A structured repository to document and showcase professional achievements, responsibilities, and contributions in **marine engineering education, training, and academic leadership**.

---

## **About**

This repository automates the extraction, structuring, and presentation of professional data for **Sunday Anwansedo**, focusing on:

- **Teaching & Training**: Applied Thermodynamics, outboard engine maintenance, and marine machinery.
- **Academic Leadership**: Docket reviews, seminar organization, and curriculum alignment.
- **Professional Development**: Collaboration with NSE (Nigerian Society of Engineers) and COREN.

---

## **Features**

- **Automated Parsing**: Extracts responsibilities and achievements from raw text.
- **Structured Output**: Generates JSON, Markdown, or Python dictionaries for further use.
- **Portfolio Ready**: Easily adaptable for CVs, LinkedIn, or academic reports.

---

## **Repository Structure**

```
marine-engineering/
├── data/
│   ├── raw_text.txt          # Input text (responsibilities & achievements)
│   └── structured_output.json # Parsed and formatted output
├── scripts/
│   └── parser.py             # Python script for parsing and structuring
├── README.md                 # Project overview and usage
└── LICENSE                   # License (e.g., MIT)
```

---

## **Getting Started**

### **Prerequisites**

- Python 3.8+
- No additional libraries required (uses built-in `re` and `json` modules).

### **Installation**

1. Clone the repository:
  ```bash
   git clone https://github.com/your-username/marine-engineering.git
   cd marine-engineering
  ```
2. Run the parser:
  ```bash
   python scripts/parser.py
  ```

---

## **Example Input & Output**

### **Input (`data/raw_text.txt`)**

```text
● Delivered lectures and hands-on demonstrations in Applied Thermodynamics to National Diploma (II) Marine Engineering students, emphasizing real-world applications, energy systems behavior, and engineering problem-solving.
● Led practical training on outboard engine maintenance and repair, strengthening students’ technical competency in marine machinery operation, diagnostics, and reliability practices.
● Contributed to academic materials review by participating in docket reviews, ensuring course materials remained current, industry-relevant, and aligned with national engineering education standards.
● Organized and facilitated technical seminars in collaboration with the Nigerian Society of Engineers (NSE), enhancing students’ exposure to professional practice, engineering ethics, and emerging sustainability trends.
Achievement:
• Organized and led two engineering seminars for the School of Marine Engineering: “Roles of Engineers in Society” and “What is Sustainability?” in partnership with NSE and COREN, promoting professional development and awareness of sustainability within engineering practice.
• Achieved a 96% pass rate in Applied Thermodynamics, reflecting instructional effectiveness, curriculum rigor, and strong student engagement.
```

### **Output (`data/structured_output.json`)**

```json
{
  "Responsibilities": [
    "Delivered lectures and hands-on demonstrations in Applied Thermodynamics to National Diploma (II) Marine Engineering students, emphasizing real-world applications, energy systems behavior, and engineering problem-solving.",
    "Led practical training on outboard engine maintenance and repair, strengthening students’ technical competency in marine machinery operation, diagnostics, and reliability practices.",
    "Contributed to academic materials review by participating in docket reviews, ensuring course materials remained current, industry-relevant, and aligned with national engineering education standards.",
    "Organized and facilitated technical seminars in collaboration with the Nigerian Society of Engineers (NSE), enhancing students’ exposure to professional practice, engineering ethics, and emerging sustainability trends."
  ],
  "Achievements": [
    "Organized and led two engineering seminars for the School of Marine Engineering: “Roles of Engineers in Society” and “What is Sustainability?” in partnership with NSE and COREN, promoting professional development and awareness of sustainability within engineering practice.",
    "Achieved a 96% pass rate in Applied Thermodynamics, reflecting instructional effectiveness, curriculum rigor, and strong student engagement."
  ]
}
```

---

## **Customization**

- **Add More Data**: Edit `data/raw_text.txt` with additional bullet points.
- **Extend the Script**: Modify `scripts/parser.py` to include:
  - Keyword extraction (e.g., skills like "thermodynamics", "marine machinery").
  - Export to CSV or Markdown tables.
  - Integration with LaTeX for academic reports.

---

## **Use Cases**

1. **CV/Resume Generation**: Automatically format achievements for job applications.
2. **Academic Reporting**: Generate structured reports for tenure or accreditation.
3. **Portfolio Website**: Use the JSON output to populate a personal website.

---

## **Contributing**

Contributions are welcome! Open an issue or submit a pull request for:

- Bug fixes.
- New features (e.g., NLP-based parsing, visualization tools).
- Improved documentation.

---

## **License**

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.
