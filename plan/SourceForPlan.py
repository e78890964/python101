
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# Using built-in fonts (no external TTF required)

# Weekly plan with tasks and theory
data = [
    ["Week", "Topics and Tasks", "Sample Problems", "Resources (Practice)", "Resources (Theory)"],

    ["1",
     "Installing Python, IDE. Variables, input-output, data types.",
     "1) Hello, world!\n2) Read a name and print a greeting.\n3) Sum of two numbers.",
     '<a href="https://stepik.org/course/67">Stepik</a><br/>'
     '<a href="https://www.codewars.com/">Codewars</a>',
     '<a href="https://docs.python.org/3/tutorial/">Python Documentation</a><br/>'
     '<a href="https://www.youtube.com/watch?v=rfscVS0vtbw">YouTube: Python Crash Course</a>'],

    ["2",
     "Conditional statements, loops.",
     "1) Check if a number is even.\n2) Multiplication table.\n3) Numbers from 1 to N.",
     '<a href="https://leetcode.com/">LeetCode</a>',
     '<a href="https://realpython.com/python-conditional-statements/">RealPython: if-else</a>'],

    ["3",
     "Functions, working with modules.",
     "1) factorial(n).\n2) Maximum of three numbers.\n3) Use sqrt() from math.",
     '<a href="https://stepik.org/course/512">Stepik Algorithms</a>',
     '<a href="https://realpython.com/defining-your-own-python-function/">RealPython: functions</a>'],

    ["4",
     "Strings and collections.",
     "1) Reverse a string.\n2) Unique elements of a list.\n3) Count letters.",
     '<a href="https://www.codewars.com/">Codewars</a>',
     '<a href="https://realpython.com/python-strings/">RealPython: strings</a><br/>'
     '<a href="https://docs.python.org/3/tutorial/datastructures.html">Documentation: collections</a>'],

    ["5",
     "Files (txt, JSON, CSV).",
     "1) Count lines in a file.\n2) Write a list to CSV.\n3) Load JSON.",
     '<a href="https://pandas.pydata.org/">Pandas</a>',
     '<a href="https://docs.python.org/3/tutorial/inputoutput.html">Documentation: files</a>'],

    ["6",
     "OOP: classes, inheritance.",
     "1) Class Dog.\n2) Class Student.\n3) Class Shape + Circle, Square.",
     '<a href="https://stepik.org/course/187">Stepik: OOP</a>',
     '<a href="https://realpython.com/python3-object-oriented-programming/">RealPython: OOP</a>'],

    ["7",
     "Exceptions, decorators, generators.",
     "1) Division by zero.\n2) Logging decorator.\n3) Fibonacci generator.",
     '<a href="https://leetcode.com/">LeetCode</a>',
     '<a href="https://realpython.com/python-exceptions/">Exceptions</a><br/>'
     '<a href="https://realpython.com/primer-on-python-decorators/">Decorators</a>'],

    ["8",
     "API and parsing.",
     "1) Get USD exchange rate.\n2) Parse news.\n3) Save JSON.",
     '<a href="https://www.crummy.com/software/BeautifulSoup/">BeautifulSoup</a>',
     '<a href="https://realpython.com/python-requests/">Requests</a>'],

    ["9",
     "Flask: web applications.",
     "1) Hello in browser.\n2) /about page.\n3) Display name from URL.",
     '<a href="https://flask.palletsprojects.com/">Flask</a>',
     '<a href="https://realpython.com/tutorials/flask/">Flask articles</a>'],

    ["10",
     "Testing and automation.",
     "1) pytest factorial().\n2) Rename files.\n3) unittest for calculator.",
     '<a href="https://docs.pytest.org/en/stable/">pytest</a>',
     '<a href="https://realpython.com/pytest-python-testing/">pytest theory</a>'],

        ["11",
     "Git and GitHub.",
     "1) Create a repository.\n2) Commit + README.md.\n3) Push to GitHub.",
     '<a href="https://learngitbranching.js.org/">Learn Git Branching</a>',
            '<a href="https://git-scm.com/book/en/v2">Pro Git book</a>'],

    ["12",
     "Interview preparation.",
     "1) Binary search.\n2) Implement a stack.\n3) 5 LeetCode Easy problems.",
     '<a href="https://neetcode.io/">NeetCode</a>',
      '<a href="https://roadmap.sh/python">Python Roadmap</a><br/>'
      '<a href="https://refactoring.guru/design-patterns/python">Design Patterns</a>'],
]
# Create the document
pdf_file = "python_timeline_with_theory.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=A4, rightMargin=10, leftMargin=10, topMargin=20, bottomMargin=20)
styles = getSampleStyleSheet()
# Convert all cells (except header) into Paragraphs for proper wrapping
for row in range(1, len(data)):
    for col in range(len(data[row])):
        data[row][col] = Paragraph(str(data[row][col]), styles['BodyText'])

# Table
table = Table(data, colWidths=[40, 110, 150, 110, 110])
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, -1), "LEFT"),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica"),
    ("FONTSIZE", (0, 0), (-1, 0), 9),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
    ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
    ("WORDWRAP", (0, 0), (-1, -1), True),
]))

# Save PDF
doc.build([table])

print(f"PDF created: {pdf_file}")