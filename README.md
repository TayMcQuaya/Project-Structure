# Project Structure Analyzer

A simple Python script to analyze your project directory, generate an ASCII tree representation of its structure, and manage `.gitignore` to exclude the script, the generated structure file, and common dependency directories from version control.

## Features

- **ASCII Tree Generation**: Creates a clear and organized ASCII tree of your project's folder and file hierarchy.
- **.gitignore Management**: Automatically adds `project_structure.py`, `project_structure.txt`, and common dependency directories (like `node_modules`, `venv`, etc.) to your `.gitignore` to prevent them from being tracked by Git.
- **Overwrite Capability**: Safely overwrites the existing `project_structure.txt` each time the script is run to ensure the latest structure is captured.
- **Hidden Files Exclusion**: Excludes all hidden files and directories (those starting with `.`) from the ASCII tree, except for `.gitignore`.
- **Permission Handling**: Gracefully handles directories with restricted permissions by indicating access issues in the output.
- **Custom Exclusions**: Allows users to specify additional directories to exclude via command-line arguments.

## Installation

### Prerequisites

- **Python 3.x**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository

```bash
git clone https://github.com/yourusername/project-structure-analyzer.git
cd project-structure-analyzer
```

*Alternatively, you can download the `project_structure.py` script directly.*

## Usage

Navigate to the directory containing the `project_structure.py` script and run the following command:

```bash
python project_structure.py [root_dir] [-o OUTPUT] [-e EXCLUDE ...]
```

### Arguments

- `root_dir` (optional): The root directory of your project to analyze. Defaults to the current directory (`.`).
- `-o`, `--output` (optional): The name of the output text file. Defaults to `project_structure.txt`.
- `-e`, `--exclude` (optional): Additional directories to exclude from the ASCII tree and `.gitignore`.

### Examples

1. **Analyze the Current Directory and Output to `project_structure.txt`**:

    ```bash
    python project_structure.py
    ```

2. **Specify a Different Project Directory**:

    ```bash
    python project_structure.py /path/to/your/project
    ```

3. **Specify a Different Output File**:

    ```bash
    python project_structure.py /path/to/your/project -o structure_output.txt
    ```

4. **Exclude Additional Directories**:

    ```bash
    python project_structure.py /path/to/your/project -e logs temp
    ```

5. **Combine All Options**:

    ```bash
    python project_structure.py ./my_project -o my_project_structure.txt -e logs temp
    ```

### Sample Output

After running the script, your `project_structure.txt` might look like this:

```
my_project/
├── README.md
├── setup.py
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── docs/
│   ├── index.md
│   └── installation.md
├── .gitignore
└── .env
```

## `.gitignore` Management

The script ensures that both `project_structure.py` and `project_structure.txt` are listed in your `.gitignore`, along with common dependency directories. If `.gitignore` already exists, these entries will be appended without duplication. If it doesn't exist, a new `.gitignore` file will be created with the necessary entries.

**Generated `.gitignore` Example**:

```
.DS_Store
.env
.idea/
.pytest_cache/
.vscode/
coverage/
dist/
node_modules/
project_structure.py
project_structure.txt
venv/
__pycache__/
*.egg-info
build/
logs/
temp/
```

## Troubleshooting

- **No Output File Generated**:
  - Ensure you have the necessary permissions to read the directories and write to the output file location.
  - Check for any error messages in the terminal that might indicate permission issues.

- **Permission Denied Messages in Output**:
  - The script indicates directories it cannot access. You may need to run the script with elevated permissions or adjust directory permissions accordingly.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).

