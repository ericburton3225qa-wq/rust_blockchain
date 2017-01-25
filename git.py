import os
import subprocess
import random
from datetime import datetime, timedelta
 

 
# Start and end dates
start_date = datetime(2017, 1, 24)
end_date = datetime.now()
 
# Example commit messages (extend as you like)
commit_messages = [
    "feat: add initial function",
    "fix: update response parser",
    "docs: add installation guide",
    "refactor: clean up utils",
    "chore: update dependencies",
    "feat: support user sessions",
    "test: add unit tests for nlp module",
    "fix: typo in README",
    "feat: improve training pipeline",
    "chore: update requirements.txt",
    "refactor: optimize message handling",
    "docs: update usage examples",
    "fix: handle empty input gracefully",
    "feat: add logging support",
    "test: extend test coverage"
]
 
current_date = start_date
 
while current_date < end_date:
    # Randomize step (3–7 days)
    step = random.randint(5, 12)
 
    # Randomize commit time during the day
    commit_time = current_date.replace(
        hour=random.randint(9, 20),  # between 9AM–8PM
        minute=random.randint(0, 59),
        second=random.randint(0, 59)
    )
    commit_date = commit_time.strftime("%Y-%m-%d %H:%M:%S")
 
    # Pick a random commit message
    message = random.choice(commit_messages)
 
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = commit_date
    env["GIT_COMMITTER_DATE"] = commit_date
 
    # Append to a file so there is something to commit
    with open("history.log", "a") as f:
        f.write(f"{commit_date} - {message}\n")
 
    subprocess.run(["git", "add", "."], env=env)
    subprocess.run(["git", "commit", "-m", message], env=env)
 
    current_date += timedelta(days=step)
 
# Push all commits
subprocess.run(["git", "push", "origin", "main"])