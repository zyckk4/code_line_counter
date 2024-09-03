import argparse
import csv
import os

language_extensions = {
    "ps1": "PowerShell",
    "cs": "C#",
    "java": "Java",
    "js": "JavaScript",
    "ts": "TypeScript",
    "py": "Python",
    "cpp": "C++",
    "h": "C++",
    "c": "C",
    "rb": "Ruby",
    "php": "PHP",
    "html": "HTML",
    "css": "CSS",
    "go": "Go",
    "rs": "Rust",
    "swift": "Swift",
    "kt": "Kotlin",
    "m": "Objective-C",
    "scala": "Scala",
    "sh": "Shell",
    "bat": "Batch",
    "sql": "SQL",
    "r": "R",
    "dart": "Dart",
    "lua": "Lua",
    "md": "Markdown"
}

def count_lines(path, recursive):
    results = {}
    total_lines = 0
    total_empty_lines = 0
    total_non_empty_lines = 0

    if recursive:
        walker = os.walk(path)
    else:
        walker = [(path, [], os.listdir(path))]

    for root, dirs, files in walker:
        for file in files:
            extension = file.split(".")[-1].lower()
            if extension in language_extensions:
                language = language_extensions[extension]
                line_count = 0
                empty_line_count = 0
                non_empty_line_count = 0
                try:
                    with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f:
                        for line in f:
                            line_count += 1
                            if line.strip() == "":
                                empty_line_count += 1
                            else:
                                non_empty_line_count += 1

                    total_lines += line_count
                    total_empty_lines += empty_line_count
                    total_non_empty_lines += non_empty_line_count

                    if language in results:
                        results[language]['lines'] += line_count
                        results[language]['empty_lines'] += empty_line_count
                        results[language]['non_empty_lines'] += non_empty_line_count
                    else:
                        results[language] = {
                            'lines': line_count,
                            'empty_lines': empty_line_count,
                            'non_empty_lines': non_empty_line_count
                        }
                except Exception as e:
                    print(f"Failed to read file: {os.path.join(root, file)}")

    return total_lines, total_empty_lines, total_non_empty_lines, results

def output_results(total_lines, total_empty_lines, total_non_empty_lines, results, generate_csv, csv_filename):
    print(f"Total Lines: {total_lines}")
    print(f"Total Empty Lines: {total_empty_lines}")
    print(f"Total Non-Empty Lines: {total_non_empty_lines}")
    for language, counts in results.items():
        print(f"{language}: {counts['lines']} (Empty: {counts['empty_lines']}, Non-Empty: {counts['non_empty_lines']})")

    if generate_csv:
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Language", "Total Lines", "Empty Lines", "Non-Empty Lines"])
            for language, counts in results.items():
                writer.writerow([language, counts['lines'], counts['empty_lines'], counts['non_empty_lines']])
            writer.writerow(["Total", total_lines, total_empty_lines, total_non_empty_lines])

def main():
    parser = argparse.ArgumentParser(description="Count lines of code in directories.")
    parser.add_argument('paths', type=str, nargs='*', default=['.'], help='Paths to the directories to be scanned.')
    parser.add_argument('-r', '--recursive', action='store_true', help='Recursively scan directories.')
    parser.add_argument('--csv', action='store_true', help='Generate CSV output.')
    parser.add_argument('--csv-name', type=str, default='code_lines_count.csv', help='Name of the CSV file.')
    args = parser.parse_args()

    total_lines = 0
    total_empty_lines = 0
    total_non_empty_lines = 0
    aggregated_results = {}

    for path in args.paths:
        lines, empty_lines, non_empty_lines, results = count_lines(path, args.recursive)
        total_lines += lines
        total_empty_lines += empty_lines
        total_non_empty_lines += non_empty_lines

        for language, counts in results.items():
            if language in aggregated_results:
                aggregated_results[language]['lines'] += counts['lines']
                aggregated_results[language]['empty_lines'] += counts['empty_lines']
                aggregated_results[language]['non_empty_lines'] += counts['non_empty_lines']
            else:
                aggregated_results[language] = counts

    output_results(total_lines, total_empty_lines, total_non_empty_lines, aggregated_results, args.csv, args.csv_name)

if __name__ == "__main__":
    main()
