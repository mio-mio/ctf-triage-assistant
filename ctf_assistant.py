import re
import subprocess
from pathlib import Path

challenge_dir_input = input("Challenge folder path: ")
challenge_dir = Path(challenge_dir_input).expanduser()

if not challenge_dir.exists():
    print(f"Error: Challenge folder not found: {challenge_dir}")
    exit(1)

description_path = challenge_dir / "description.txt"
path = challenge_dir / "files" / "challenge.txt"

if not description_path.exists():
    print(f"Error: description.txt not found: {description_path}")
    exit(1)

if not path.exists():
    print(f"Error: challenge.txt not found: {path}")
    exit(1)

with open(path) as f:
    text = f.read()

with open(description_path) as f:
    description = f.read()

flag_candidates = re.findall(r"triage_test\{[^}]+\}", text)


if flag_candidates:
    print("Flag-like string found!")
    print(flag_candidates)
else:
    print("No flag-like string found.")


file_result = subprocess.run(
    ["file", str(path)],
    capture_output=True,
    text=True
)

print("[file result]")
print(file_result.stdout)

strings_result = subprocess.run(
    ["strings", str(path)],
    capture_output=True,
    text=True
)

print("[strings result]")
print(strings_result.stdout)

report = "# Analysis Report\n\n"

report += "## Description\n\n"
report += "```text\n"
report += description.strip()
report += "\n```\n\n"

report += "## Target File\n\n"
report += f"`{path}`\n\n"

report += "## Flag Candidates\n\n"
if flag_candidates:
    for flag in flag_candidates:
        report += f"- `{flag}`\n"
else:
    report += "No flag-like strings found.\n"
report += "\n"

report += "## file Result\n\n"
report += "```text\n"
report += file_result.stdout.strip()
report += "\n```\n\n"

report += "## strings Result\n\n"
report += "```text\n"
report += strings_result.stdout.strip()
report += "\n```\n"

output_path = Path("reports") / "analysis.md"
output_path.write_text(report, encoding="utf-8")

print(f"Report written to: {output_path}")

