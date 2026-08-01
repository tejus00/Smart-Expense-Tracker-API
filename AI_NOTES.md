# AI_NOTES.md

## 1. Which parts of the code were AI-generated vs. written by you

### AI-assisted

- HTML templates for the home page, add expense page, and delete expense page.
- JavaScript Fetch API examples for communicating with the backend.
- Improved the HTML layout and navigation.
- Initial pytest examples.
- Created and modified the JSON dataset (`expenses.json`).

### Written/Customized by Me

- Organized the project into the required folder structure.
- Integrated all routes into a single Flask application.
- Developed the initial Flask REST API structure.
- Implemented CRUD endpoints (Add, View, Delete).
- Added search functionality by Expense ID and Category.
- Implemented expense grouping and total expense calculations.
- Fixed routing, import, and file path issues.
- Updated the test cases to match the final project structure.

---

## 2. What you validated, tested, or changed in the AI's output, and why

- Modified the file path of `expenses.json` from an absolute path to a relative path to make the application platform-independent.
- Adjusted the Flask routing and removed duplicate routes.
- Updated the imports after moving `app.py` into the `src` folder.
- Tested all API endpoints manually using the browser and automatically using pytest.
- Improved the HTML pages to display expense data in a table instead of raw JSON.
- Created separate pages for adding and deleting expenses to improve usability.
- Verified that all test cases passed successfully before finalizing the project.

---

## 3. Any AI suggestion you decided not to use, and why

- I did not use a database such as SQLite or PostgreSQL because the assignment specifically required JSON files and/or in-memory storage. Therefore, those AI suggestions were not applicable.
- Instead of relying on AI-generated backend implementations, I developed the Flask application myself because I am more familiar with Flask and wanted to ensure I understood the implementation.
- I chose not to use frontend frameworks such as React because the project requirements could be met effectively using HTML, CSS, and JavaScript, making additional frameworks unnecessary.
- I did not use some AI-suggested project structures and design approaches because they did not match the assignment requirements or the project's organization.
- During development, some AI-generated code resulted in directory structure, import, and implementation mismatches. I corrected the syntax, updated the imports, and reorganized the code to fit the final project structure.
