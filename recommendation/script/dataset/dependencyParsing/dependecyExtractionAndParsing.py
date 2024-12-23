import os
import re
import subprocess
import pandas as pd
import shutil

# Input and output file paths
INPUT_FILE = "build_successful_repos.csv"
OUTPUT_FILE = "output_dependencies.csv"
TEMP_DIR = "temp_repos"

# Ensure the temp directory exists
os.makedirs(TEMP_DIR, exist_ok=True)

def clone_repo(repo_url, target_dir):
    """
    Clone the repository from GitHub.
    """
    try:
        subprocess.run(["git", "clone", repo_url, target_dir], check=True)
        return True
    except subprocess.CalledProcessError:
        print(f"Failed to clone repository: {repo_url}")
        return True


def build_project(repo_dir):
    """
    Build the Android project using Gradle with dynamic path handling.
    """
    try:
        # Dynamically construct the gradlew path
        gradlew_path = os.path.abspath(os.path.join(repo_dir, "gradlew"))

        print(f"Building project: {repo_dir}")
        print(f"Gradle path: {gradlew_path}")

        # Add execute permission for gradlew
        subprocess.run(["chmod", "+x", gradlew_path], cwd=repo_dir, check=True)

        # Run the assembleDebug command
        subprocess.run([gradlew_path, "assembleDebug"], cwd=repo_dir, check=True)

        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to build project in: {repo_dir}")
        print(f"Error: {e}")
        return False
    except FileNotFoundError as e:
        print(f"File not found error: {e}")
        return False

def extract_dependency_tree(repo_dir):
    """
    Extract the dependency tree using Gradle.
    """
    try:
        gradlePath = os.path.abspath(os.path.join(repo_dir, "gradlew"))
        result = subprocess.run(
            [gradlePath, "app:dependencies"],
            cwd=repo_dir,
            stdout=subprocess.PIPE,
            text=True,
            check=True
        )
        print(f"Successfully to extract dependency tree for: {repo_dir}")
        return result.stdout
    except subprocess.CalledProcessError:
        print(f"Failed to extract dependency tree for: {repo_dir}")
        return None

def parse_and_save_dependency_tree(dependency_tree_output, output_path, repo_url):
    """
    Parse the dependency tree and save as CSV with the repository URL.
    """
    pattern = r"^.+--- (.+?):(.+?):(.+?)$"
    dependencies = []
    print("Values saving")

    for line in dependency_tree_output.splitlines():
        match = re.match(pattern, line.strip())
        if match:
            group, artifact, version = match.groups()
            dependencies.append({"Group": group, "Artifact": artifact, "Version": version})

    df = pd.DataFrame(dependencies)
    df["GitHub Link"] = repo_url
    df.to_csv(output_path, index=False)

    print("Values saved")

def delete_repo(repo_dir):
    """
    Delete the cloned repository.
    """
    try:
        shutil.rmtree(repo_dir)
    except Exception as e:
        print(f"Error deleting repository {repo_dir}: {e}")

def main():
    # Read input repositories
    repo_df = pd.read_csv(INPUT_FILE)
    all_dependencies = pd.DataFrame()

    for _, row in repo_df.iterrows():
        repo_url = row['Successful Repositories']
        repo_name = repo_url.split("/")[-1]
        repo_dir = os.path.join(TEMP_DIR, repo_name)

        print(f"Processing repository: {repo_url}")

        # Clone, build, extract, and clean up
        if clone_repo(repo_url, repo_dir):
            if build_project(repo_dir):
                dependency_tree_output = extract_dependency_tree(repo_dir)
                if dependency_tree_output:
                    temp_csv_path = os.path.join(TEMP_DIR, f"{repo_name}_dependencies.csv")
                    parse_and_save_dependency_tree(dependency_tree_output, temp_csv_path, repo_url)
                    # Append to combined DataFrame
                    df_temp = pd.read_csv(temp_csv_path)
                    all_dependencies = pd.concat([all_dependencies, df_temp], ignore_index=True)
            else:
                print(f"Skipping due to build failure: {repo_url}")
            # delete_repo(repo_dir)

    # Save combined output
    all_dependencies.to_csv(OUTPUT_FILE, index=False)
    print(f"Dependency data saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
