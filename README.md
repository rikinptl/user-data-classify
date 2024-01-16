# Data Fetch and Store Script

This Python script is designed to fetch data from a specified URL in various formats (JSON, CSV, YAML, XML) and store it in a structured directory based on timestamp. The script utilizes the `requests`, `csv`, `json`, `yaml`, `xml.etree`, `datetime`, and `schedule` modules for data retrieval, processing, and scheduling.

## Getting Started

### Prerequisites

- Python 3.x
- Dependencies (install via `pip install -r requirements.txt`)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Run the script:

    ```bash
    python script.py
    ```

### Usage

1. The script prompts you to enter the desired file format (csv, json, yaml, xml) that you want to fetch.

2. It fetches data from a specified URL (https://randomuser.me/api/) in the chosen format.

3. The data is stored in a structured directory based on timestamp.

4. The script is scheduled to run every 3 seconds, allowing for periodic data retrieval and storage.

## Code Structure

- `classifier` class: Defines a classifier for handling data retrieval and storage.
- `pathmaker` method: Generates a structured directory and file name based on timestamp.
- `fetchdata` method: Fetches data from the specified URL in the chosen format.
- `storedata` method: Stores the fetched data in the specified file format (JSON, CSV, YAML, XML).
- `job` function: Allows the user to input the desired file format, creates a classifier object, fetches and stores data.

## Schedule Configuration

