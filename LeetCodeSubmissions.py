import requests
import json
from pathlib import Path



with open("Header.json") as f:
    headers = json.load(f)
with open("response_offset0limit20lastkey.json") as f:
    submission_json = json.load(f)

submissionDict = submission_json['submissions_dump']

url = "https://leetcode.com/api/submissions/"

stuff = requests.get(url, headers=headers)


submission_json_request = stuff.json()['submissions_dump']

def create_problem_markdown(problem):
    problem_file_path = problem_dir / f"{problem['title'].replace(' ', '_')}.md"
    try:
        with open(problem_file_path, "w") as file:
            file.write(f"**Language:** {problem['lang']}\n")
            if(problem['lang'] == 'python3'):
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
print(create_problem_markdown(submission_json_request[0]).absolute())

