# Code Line Counter

**Code Line Counter** is a Python script designed to count lines of code in specified directories. It can count total lines, empty lines, and non-empty lines for various programming languages. The script supports recursive scanning of directories, multiple paths input, and optional CSV export of the results.

## Features

- Count total, empty, and non-empty lines of code.
- Supports multiple programming languages such as Python, JavaScript, C++, Java, and more.
- Scan multiple directories simultaneously.
- Option to recursively scan directories.
- Option to export results to a CSV file with customizable file name.

## Supported Languages

This script currently supports counting lines in files with the following extensions:

`ps1, cs, java, js, ts, py, cpp, h, c, rb, php, html, css, go, rs, swift, kt, m, scala, sh, bat, sql, r, dart, lua, md`

You can modify extensions listed in dict `language_extensions` in the script as you wish.

## Usage

### Prerequisites

- Python 3.x

### Running the Script

To use the script, run the following command in your terminal:

```bash
python code_count.py [paths] [options]
```

### Arguments

- `paths`: Space-separated paths of directories to scan. Defaults to the current directory if not specified.

### Options

- `-r, --recursive`: Recursively scan directories.
- `--csv`: Generate CSV output of the results.
- `--csv-name <filename>`: Specify the name of the CSV file (default is `code_lines_count.csv`).

### Examples

1. Count lines in the current directory without recursion:

   ```bash
   python code_count.py
   ```

2. Count lines in multiple directories recursively:

   ```bash
   python code_count.py /path/to/dir1 /path/to/dir2 -r
   ```

3. Count lines and save the results to a custom CSV file:

   ```bash
   python code_count.py /path/to/dir -r --csv --csv-name results.csv
   ```

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your contributions are always welcome!

## License

This project is licensed under the MIT License.
