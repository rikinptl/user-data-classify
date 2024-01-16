# Data Fetch and Store Script

This Python script 🐍 is designed to fetch data from a specified URL 🌐 in various formats (JSON, CSV, YAML, XML) and store it in a structured directory based on timestamp 📅. The script utilizes the `requests` 📡, `csv` 📊, `json` 📋, `yaml` 🧾, `xml.etree` 🌳, `datetime` 🕰️, and `schedule` 🕒 modules for data retrieval, processing, and scheduling.

## Getting Started 🚀

### Prerequisites

- Python 3.x
- Dependencies (install via `pip install -r requirements.txt`)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/rikinptl/user-data-classify.git
    cd user-data-classify
    ```

2. Run the script:

    ```bash
    python script.py
    ```

### Usage 🤖

1. The script prompts you to enter the desired file format (csv, json, yaml, xml) that you want to fetch.

2. It fetches data from a specified URL (https://randomuser.me/api/) in the chosen format.

3. The data is stored in a structured directory based on timestamp.

4. The script is scheduled to run every 3 hours, allowing for periodic data retrieval and storage.

## Code Structure 🏗️

### classifier Class

- **`__init__(self, url: str, file_type: str)`**: Initializes the classifier with a URL and file type.
  
- **`pathmaker(self) -> str`**: Generates a structured directory and file name based on timestamp.

- **`fetchdata(self) -> requests.Response`**: Fetches data from the specified URL in the chosen format.

- **`storedata(self, data: requests.Response, file_path: str) -> None`**: Stores the fetched data in the specified file format (JSON, CSV, YAML, XML).

- **`job(fileformat) -> None` (Static Method)**: Allows the user to input the desired file format, creates a classifier object, fetches and stores data.

## Schedule Configuration 🕒

The script is configured to run periodically using the `schedule` module, ensuring automated and consistent data retrieval and storage.

### How It Works:

1. The `job` function is scheduled to run every 3 seconds (adjustable) using the `schedule.every(3).seconds` syntax.

2. The script continuously checks for pending scheduled jobs with `schedule.run_pending()`.

3. The script remains active, allowing scheduled jobs to execute at their designated intervals.

Feel free to modify the schedule parameters based on your specific requirements. If you have any further questions or adjustments, please let me know!

# Code Review and Learnings 📚

## Learnings:

1. **Exception Handling:**
   - Implemented handling for module not found and general exceptions.
   - Consider specifying specific exceptions for better error diagnostics.

2. **Dynamic Code Execution:**
   - Creative use of a dictionary and dynamic code execution (`exec`) for different file formats.

3. **File Handling:**
   - Effective handling of file creation and directory structuring based on timestamps.

4. **User Input Validation:**
   - Good practice to validate user input for the desired file format.

5. **Scheduling:**
   - Use of the `schedule` module for periodic data retrieval and storage is valuable for automation.

## Areas for Improvement:

1. **Repetition of Code:**
   - Repetition in fetching, storing, and scheduling. Consider refactoring to avoid redundancy.

2. **User Interaction:**
   - Relying on continuous user input. Consider adding more user-friendly interactions and options.

3. **Logging:**
   - Incorporate logging for detailed information about each execution for better debugging.

4. **Code Structure:**
   - Break down the script into smaller functions or classes for better maintainability.

5. **Exit Mechanism:**
   - Graceful exit mechanism instead of using `exit()` on exception handling.

6. **User Configurability:**
   - Explore options to allow users to configure aspects like the URL or scheduling intervals.

7. **Testing:**
   - Implement unit testing to ensure the correctness of individual components and functions.

8. **Parallel Processing:**
   - Explore parallel data fetching for potential performance improvements.

9. **Documentation:**
   - Add comments within the code to explain complex logic or functionality.

10. **Code Style:**
    - Adhere to consistent code style conventions for improved readability.

🍏 Feel free to customize and enhance the script based on these insights! 🍎
