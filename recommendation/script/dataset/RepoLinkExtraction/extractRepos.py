import csv
import os
import re
import subprocess

# Constants
REPO_URL = "https://github.com/binaryshrey/Awesome-Android-Open-Source-Projects.git"  # Path to the local clone of the android-foss repository
OUTPUT_CSV = "github_links.csv"  # Name of the output CSV file
PROJECT_DIR = "/Users/ateeb/PycharmProjects/AndroidApplicationCompilation/app-links1"  # Where the repo will be cloned

def clone_repo():
    """Clone the Android project."""
    if not os.path.exists(PROJECT_DIR):
        subprocess.run(["git", "clone", REPO_URL, PROJECT_DIR], check=True)
    else:
        print("Project directory already exists. Skipping clone.")

def extract_github_links(repo_path):
    """
    Extract GitHub repository links from the android-foss repository files.

    :param repo_path: Path to the local clone of the android-foss repository.
    :return: List of GitHub repository URLs.
    """
    github_links = []
    for root, _, files in os.walk(repo_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Only process text files
            if file.endswith((".md", ".txt", ".yaml", ".json")):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Use regex to find GitHub links in Markdown and plain URLs
                    links = re.findall(r"https?://github\.com/[a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+", content)
                    github_links.extend(links)
    return list(set(github_links))  # Remove duplicates


def save_to_csv(links, output_file):
    """
    Append GitHub links to a CSV file without losing existing data, and remove duplicates.

    :param links: List of GitHub repository URLs.
    :param output_file: Name of the output CSV file.
    """
    existing_links = set()

    # Check if the CSV file already exists and read existing links
    if os.path.exists(output_file):
        try:
            with open(output_file, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip the header row
                existing_links.update(row[0] for row in reader if row)  # Add existing links
        except Exception as e:
            print(f"Error reading existing CSV file: {str(e)}")

    # Combine new links with existing links and remove duplicates
    all_links = existing_links.union(set(links))

    # Save the combined list back to the CSV file
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["GitHub Links"])  # Write header row
            for link in sorted(all_links):  # Sort for consistency
                writer.writerow([link])
        print(f"GitHub links successfully saved to {output_file}. Total links: {len(all_links)}")
    except Exception as e:
        print(f"Error saving to CSV: {str(e)}")

def main():
    # Extract GitHub links
    clone_repo()
    github_links = extract_github_links(PROJECT_DIR)
    print(f"Found {len(github_links)} GitHub links.")

    # Save to CSV
    save_to_csv(github_links, OUTPUT_CSV)


if __name__ == "__main__":
    main()
