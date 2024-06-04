import random

def generate_commits(num_commits=729):
    with open("file.txt", "a") as file:
        for i in range(1, num_commits + 1):
            days_ago = random.randint(1, 10)
            commit_date = f"{days_ago} days ago"

            file.write(commit_date + "\n")  # Append with newline

            # Stage changes using safer `subprocess` for external commands
            import subprocess
            subprocess.run(["git", "add", "."])

            # Create informative commit message with timestamp
            commit_message = f"Automatic commit: {commit_date}"
            subprocess.run(["git", "commit", "-d", commit_date, "-m", commit_message])

# Example usage (adjust num_commits as needed)
generate_commits(729)
