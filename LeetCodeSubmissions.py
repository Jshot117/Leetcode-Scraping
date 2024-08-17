import datetime
import requests
import json
import time
from pathlib import Path


with open("Header.json") as f:
    headers = json.load(f)

url = "https://leetcode.com/api/submissions/"

stuff = requests.get(url, headers=headers)

submission_json_request = stuff.json()


def create_problem_markdown(problem):
    problem_file_path = problem_dir / f"{problem['title'].replace(' ', '_')}.md"
    try:
        with open(problem_file_path, "w") as file:
            file.write(f"date : {datetime.datetime.fromtimestamp(problem['timestamp']).strftime("%a %d %b %Y, %I:%M%p")}\n")
            file.write(f"**Language:** {problem['lang']}\n") if problem['lang'] != "pythondata" else file.write(f"**Language:** python3\n")
            file.write(f"[Submission URL](https://leetcode.com{problem['url']})\n")
            if problem["lang"] == "python3":
                file.write(f"```python\n{problem['code']}```")
            elif problem["lang"] == "pythondata":
                file.write(f"```python\n{problem['code']}```")
            else:
                file.write(f"```{problem['lang']}\n{problem['code']}```")
            
            
        print(f"Successfully Created file: {problem_file_path}")
    except Exception as e:
        print(f"error creating file: {problem_file_path}\n{e}")
    return problem_file_path


base_dir = input("Enter the base directory path: ")
base_dir = Path(base_dir)
problem_dir = base_dir / "Problems"
problem_dir.mkdir(parents=True, exist_ok=True)
offset = len(submission_json_request["submissions_dump"])
while submission_json_request["has_next"]:
    for submission in submission_json_request["submissions_dump"]:
        if submission["status_display"] == "Accepted":
            create_problem_markdown(submission).absolute()
    payload = {"offset": offset}
    request_data = requests.get(url, headers=headers, params = payload)
    submission_json_request = request_data.json()
    # To avoid getting blocked by the server
    time.sleep(2.5)
    offset += len(submission_json_request["submissions_dump"])
