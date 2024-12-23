import os
import subprocess
import shutil
import csv

import pandas as pd

from testFileCreation import save_successful_repo

REPO_LIST_FILE = "repo_list.csv"  # Input file containing a list of GitHub repository URLs
PROJECT_DIR = "/tmp/android-project"  # Temporary project directory for cloning repositories
OUTPUT_FILE = "build_successful_repos.csv"  # Output CSV file to save successful repo URLs
ORIGINAL_WORKING_DIR = ""


def clone_repo(repo_url):
    try:
        # Ensure target directory is clean
        if os.path.exists(PROJECT_DIR):
            shutil.rmtree(PROJECT_DIR)  # Clean up any previous project

        # Clone the repository
        result = subprocess.run(
            ["git", "clone", repo_url, PROJECT_DIR],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print(f"Cloned repository: {repo_url}\n{result.stdout.decode()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone repository {repo_url}: {e.stderr.decode()}")
        return False
    except Exception as e:
        print(f"Unexpected error cloning repository {repo_url}: {str(e)}")
        return False


def build_apk():
    """
    Build the APK using Gradle.

    :return: True if the APK build was successful, False otherwise.
    """
    try:
        os.chdir(PROJECT_DIR)
        subprocess.run(["chmod", "+x", "./gradlew"], check=True)
        # Run the build command
        subprocess.run(["./gradlew", "assembleDebug"], check=True)
        print("APK built successfully.")
        return True
    except Exception as e:
        print(f"Failed to build APK: {str(e)}")
        return False
    finally:
        os.chdir("..")  # Return to the original directory


def delete_repo():
    """
    Delete the cloned repository to free up space.
    """
    try:
        if os.path.exists(PROJECT_DIR):
            shutil.rmtree(PROJECT_DIR)
            print("Deleted project directory.")
    except Exception as e:
        print(f"Error deleting project directory: {str(e)}")


def main():
    """
    Process each repository in the list, check if it builds successfully, and save results.
    """
    try:
        # Save original working directory
        ORIGINAL_WORKING_DIR = os.getcwd()

        # Read the list of repositories
        repo_df = pd.read_csv(REPO_LIST_FILE)
        print(repo_df)

        # DataFrames for successful and failed repositories
        df_successful = pd.DataFrame(columns=["Successful Repositories"])
        df_failed = pd.DataFrame(columns=["Repository URL", "Failure Reason"])

        for _, row in repo_df.iterrows():
            repo_url = row['GitHub Links'].strip()
            print(f"Processing repository: {repo_url}")

            # Clone the repository
            if clone_repo(repo_url):
                # Build the APK
                if build_apk():
                    print(f"Successfully built APK: {repo_url}")

                    # Append to the successful repositories DataFrame
                    df_successful = pd.concat(
                        [df_successful, pd.DataFrame({"Successful Repositories": [repo_url]})],
                        ignore_index=True
                    )
                else:
                    # Append to the failed repositories DataFrame with build failure reason
                    df_failed = pd.concat(
                        [df_failed, pd.DataFrame({"Repository URL": [repo_url], "Failure Reason": ["Build Failed"]})],
                        ignore_index=True
                    )

                # Delete the cloned repo
                delete_repo()
            else:
                # Append to the failed repositories DataFrame with clone failure reason
                df_failed = pd.concat(
                    [df_failed, pd.DataFrame({"Repository URL": [repo_url], "Failure Reason": ["Clone Failed"]})],
                    ignore_index=True
                )

        # Print and save results
        print("Successful Repositories:")
        print(df_successful)

        print("Failed Repositories:")
        print(df_failed)

        os.chdir(ORIGINAL_WORKING_DIR)

        # Save DataFrames to CSV files
        df_successful.to_csv(OUTPUT_FILE, index=False)
        df_failed.to_csv("build_failed_repos.csv", index=False)

    except Exception as e:
        print(f"Error processing repository list: {str(e)}")


if __name__ == "__main__":
    main()
