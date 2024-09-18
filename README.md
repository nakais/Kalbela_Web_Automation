# Kalbela Automation Project

This project is designed to automate the testing of the [Kalbela](https://www.kalbela.com/) website using **Selenium** and **Python**. The framework includes behavior-driven development (BDD) using **pytest** and generates an **Allure report** for test results visualization.

## Project Structure

The following structure outlines the main directories and files:
```
KalbelaAutomation/
├── page_objects/
│   ├── __init__.py       # (This is important!)
│   ├── top_section.py    # Your TopSection class is defined here
│   ├── navigation_section.py  # Your NavigationSection class is defined here
├── tests/
│   ├── __init__.py       # Optional but good practice
│   ├── test_top_section.py
│   ├── test_navigation_section.py
├── pytest.ini            # Add this file to define project root for pytest
└── .venv/
```

- **page_objects/**: Contains the Page Object Model (POM) classes for different sections of the website.
- **tests/**: Contains the test cases, organized by website sections or features.
- **.venv/**: Virtual environment for the project dependencies.
- **pytest.ini**: Configuration file for pytest.

## Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/KalbelaAutomation.git
   cd KalbelaAutomation
   ```
2. Set up a virtual environment (optional):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .\.venv\Scripts\activate   # Windows
   ```
3. Install dependencies:
   ```bash
   pip install selenium pytest allure-pytest
   ```
4. Run Tests: To run the tests, use the following command:
   ```bash
   pytest tests/
    ```
5. Generate Allure Report: After running the tests, you can generate an Allure report:
   ```bash
   pytest tests/ --alluredir=allure-results
   allure serve reports/
   ```
## Recording Video
Watch the project demo here: 
https://www.loom.com/share/6f1fc93d08e14cceaeafe07bf2348545?sid=cdaadc15-20fc-4855-9f0f-226bc46fb440

## Notes
* Ensure the required web drivers are installed for Selenium (e.g., ChromeDriver).
* This project uses Python 3.12 and pytest for testing
  


   
