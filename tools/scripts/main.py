# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import os
import subprocess
import json
import shutil
import csv

# Paths and constants
REPO_URL = "https://github.com/ateebakhtar/Munazam-A-StudentOrganizer.git"  # Replace with repo URL
PROJECT_DIR = "/Users/ateeb/PycharmProjects/AndroidApplicationCompilation/android-app"  # Where the repo will be cloned
OUTPUT_FILE = "apk_analysis_results.json"  # Output file
APK_ANALYZER_PATH = "/Users/ateeb/Library/Android/sdk/cmdline-tools/latest/bin/apkanalyzer"  # Update to your apkanalyzer path

def clone_repo():
    """Clone the Android project."""
    if not os.path.exists(PROJECT_DIR):
        subprocess.run(["git", "clone", REPO_URL, PROJECT_DIR], check=True)
    else:
        print("Project directory already exists. Skipping clone.")

def build_apks():
    os.chdir(PROJECT_DIR)

    # Build the first APK
    subprocess.run(["./gradlew", "assembleDebug"], check=True)
    apk1_path = os.path.join(PROJECT_DIR, "app/build/outputs/apk/debug/app-debug-v1.apk")
    original_apk_path = os.path.join(PROJECT_DIR, "app/build/outputs/apk/debug/app-debug.apk")
    shutil.copyfile(original_apk_path, apk1_path)  # Copy the first APK to a new location

    # Optional: Make a modification in the project (e.g., update versionCode or resources)
    print("Modify the project here if needed...")

    # Build the second APK
    subprocess.run(["./gradlew", "assembleDebug"], check=True)
    apk2_path = os.path.join(PROJECT_DIR, "app/build/outputs/apk/debug/app-debug-v2.apk")
    shutil.copyfile(original_apk_path, apk2_path)  # Copy the second APK to a new location

    os.chdir("..")  # Return to the original directory

    return apk1_path, apk2_path

def compare_apks(apk1_path, apk2_path):
    """Compare two APKs using apkanalyzer and return the raw output."""
    try:
        result = subprocess.run(
            [APK_ANALYZER_PATH, "apk", "compare", "--files", apk1_path, apk2_path],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return result.stdout.strip()  # Return raw output if successful
        else:
            raise Exception(f"Error during APK comparison: {result.stderr.strip()}")

    except Exception as e:
        return f"Exception occurred during APK comparison: {str(e)}"

def save_to_csv(data, output_file):
    """
    Save the filtered APK data to a CSV file.

    :param data: List of dictionaries with file information (size and path).
    :param output_file: Path to the CSV file.
    """
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Write header
            writer.writerow(["Original Size", "Compressed Size", "Difference", "File Path"])

            # Write filtered data
            for row in data:
                writer.writerow([row['original_size'], row['compressed_size'], row['difference'], row['path']])

        print(f"Data successfully saved to {output_file}")
    except Exception as e:
        print(f"Error saving data to CSV: {str(e)}")

def parse_and_filter_apk_data(raw_output):
    """
    Parse and filter the raw APK analyzer output.

    :param raw_output: String output from APK analyzer.
    :return: List of dictionaries containing filtered file data.
    """
    filtered_data = []
    for line in raw_output.strip().splitlines():
        parts = line.split('\t')
        if len(parts) == 4:
            original_size, compressed_size, difference, path = parts
            if not path.startswith('/res') and not path.startswith('/META-INF'):
                filtered_data.append({
                    "original_size": original_size,
                    "compressed_size": compressed_size,
                    "difference": difference,
                    "path": path
                })
    return filtered_data

def main():
    clone_repo()

    apk1, apk2 = build_apks()
    raw_output = compare_apks(apk1, apk2)

    # Filter the data
    filtered_data = parse_and_filter_apk_data(raw_output)

    # Save to CSV
    output_csv_path = "filtered_apk_data.csv"
    save_to_csv(filtered_data, output_csv_path)


if __name__ == "__main__":
    main()



