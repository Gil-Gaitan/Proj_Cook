**Setup**:
This is a working documentation = formatting is a subprocess.
---

### **Setup: Environment and Repository Setup**
1. **Environment**
   - Update python3 and pip
   - Set up IDE
   - Install essential packages:
         `pytest`    Testing framework to verify code
         `black`     Automatic code formatter
         `flake8`    Linter to check for Python syntax and style
      CLI command: pip3 install black flake8 pytest

   - Initial Test Run
         1. Create a test file
         2. Run the test
      If you see a check mark, it's good!

      Note: This helps scalability. Documentation? They can be integrated into pipelines so they are reuseable. THey provide clear error messages. Parameterized testing = testing with multiple sets of input values. They can simulate external dependencies. Will it work with more complex applications? Includes regression testing.

2. **Git and GitHub Setup**
   - Initialize a Git repository on the hub
   - Create a new repository locally with CLI command: git init
   - And then to link it to the git repo: git remote add origin https://github.com/Gil-Gaitan/Proj_Cook.git
   - Walk through basic Git commands (`git add`, `commit`, `push`, `pull`) and best practices for commits.
   - Set up a `.gitignore` file to avoid tracking unnecessary files.

3. **Project Structure**
   - Create a clean folder structure with separate directories for **sorting**, **searching**, **arrays**, **strings**, and so on.
   - Add a `README.md` file for each section, briefly explaining the contents and algorithms.

4. **Development Tools**
   - Set up and configure `pytest` for unit testing to ensure that each solution works as expected.
   - Configure `black` and `flake8` for code formatting and linting to help you maintain clean, readable code.

5. **Initial GitHub Push**
   - Push your setup to GitHub with an initial commit message, and we’ll make sure the structure is clean and ready to go.

6. **Setting Up Coding Templates**
   - Create a basic Python file template with standard code sections (imports, main logic, helper functions).
   - Set up basic comments and docstrings to guide you on documenting each new function.

---
