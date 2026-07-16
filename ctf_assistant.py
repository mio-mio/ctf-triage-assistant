import re
import shutil
import subprocess
import json
from pathlib import Path
from datetime import datetime

# Command Function
def run_inspection_command(command_parts, target_path):
    command_name = command_parts[0]

    if shutil.which(command_name) is None:
        return {
            "status": "error",
            "text": f"Error: {command_name} is not available."
        }
    
    result = subprocess.run(
        command_parts + [str(target_path)],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return {
            "status": "error",
            "text": result.stderr or f"Error: {command_name} failed."
        }
    
    return {
        "status": "success",
        "text": result.stdout
    }

# Load Metadata
def load_metadata(challenge_dir):
    metadata_path = challenge_dir / "metadata.json"

    if not metadata_path.exists():
        return {}
    
    try:
        metadata = json.loads(
            metadata_path.read_text(encoding="utf-8")
        )
    except (OSError, json.JSONDecodeError) as error:
        print(f"Warning: Could not read metadata.json : {error}")
        return {}
    
    if not isinstance(metadata, dict):
        print("Note: metadata.json was skipped. Please use {} at the top level.")
        return {}
    
    return metadata

# For Report Generation
def generate_markdown_report(analysis_result):
    report = ""
    report += "# Analysis Report\n\n"
        
    if analysis_result["metadata"]:
        report += "## Challenge Metadata\n\n"

        for key, value in analysis_result["metadata"].items():
            report += f"- {key.title()}: {value}\n"
        report += "\n"

    report += "## Description\n\n"
    report += "```text\n"
    report += analysis_result["description"].strip()
    report += "\n```\n\n"

    return report

# For command result
def report_command_result(command_name, target_result):
    report = ""
    report += f"### {command_name}\n\n"
    report += f"Status: `{target_result['status']}`\n\n"
    report += "```text\n"
    report += target_result["text"].strip()
    report += "\n```\n\n"
    
    return report

# Challenge Folder Path Input
challenge_dir_input = input("Challenge folder path: ")
challenge_dir = Path(challenge_dir_input).expanduser()
files_dir = challenge_dir / "files"

# Error check
if not challenge_dir.exists():
    print(f"Error: Challenge folder not found: {challenge_dir}\n")
    exit(1)

if not files_dir.exists():
    print(f"Error: Files folder not found: {files_dir}\n")
    exit(1)

# Description
description_path = challenge_dir / "description.txt"

if description_path.exists():
    with open(description_path) as f:
        description = f.read()
else:
    description = "No description provided."

target_files = []

for path in sorted(files_dir.iterdir()):

    if path.is_file():
        target_files.append(path)

if not target_files:
    print("No files were found in the files folder.")
    exit(1)


metadata = load_metadata(challenge_dir)
analysis_result = {
    "description": description,
    "metadata": metadata
}

# Generate Report
report = generate_markdown_report(analysis_result)

# Inspect Files in Folder
for target_file in target_files:
   # CLI output
    print("◎ Target File ◎")
    print(target_file.name)
    print("\n")

    # Report output
    report += "## Target File\n\n"
    report += f"`{target_file.name}`\n\n"

    file_command_result = run_inspection_command(["file"], target_file)
    strings_command_result = run_inspection_command(["strings"], target_file)

    file_result = file_command_result["text"]
    strings_result = strings_command_result["text"]

    # Find Flag-like String
    flag_candidates = re.findall(r"triage_test\{[^}]+\}", strings_result)
    flag_candidates = list(dict.fromkeys(flag_candidates))

    # CLI output
    if flag_candidates:
        print(f"Flag-like string found in {target_file.name}!")
        print(flag_candidates)
        print("\n")

    else:
        print(f"No flag-like string found in {target_file.name}.")
        print("\n")

    # Report Continue
    report += "## Flag Candidates\n\n"
    if flag_candidates:
        for flag in flag_candidates:
            report += f"- `{flag}`\n"
    else:
        report += "No flag-like strings found.\n"
    report += "\n"

    # CLI output
    print("[file_result]")
    print(file_result)
    print("\n")

    # Report output
    report += report_command_result("file", file_command_result)
    report += report_command_result("strings", strings_command_result)

    file_info = file_result.lower()
    if "image" in file_info:
        exiftool_command_result = run_inspection_command(["exiftool"], target_file)
        exiftool_result = exiftool_command_result["text"]

        # CLI output
        print("[exiftool]")
        print(exiftool_result)
        print("\n")

        # Report output
        report += report_command_result("exiftool", exiftool_command_result)

    elif "elf" in file_info:
        readelf_command_result = run_inspection_command(["readelf", "-h"], target_file)
        objdump_command_result = run_inspection_command(["objdump", "-f"], target_file)

        readelf_result = readelf_command_result["text"]
        objdump_result = objdump_command_result["text"]

        # CLI output
        print("[readelf -h]")
        print(readelf_result)
        print("\n")
        
        print("[objdump -f]")
        print(objdump_result)
        print("\n")

        # Report output
        report += report_command_result("readelf -h", readelf_command_result)
        report += report_command_result("objdump", objdump_command_result)


    elif "zip" in file_info:
        unzip_v_command_result = run_inspection_command(["unzip", "-v"], target_file)
        unzip_v_result = unzip_v_command_result["text"]

        # CLI output
        print("[unzip -v]")
        print(unzip_v_result)
        print("\n")

        # Report output
        report += report_command_result("unzip", unzip_v_command_result)

report_dir = Path("reports")
report_dir.mkdir(exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
report_time = f"{challenge_dir.name}_{timestamp}.md"
output_path = report_dir / report_time
output_path.write_text(report, encoding="utf-8")

print(f"Report written to: {output_path}")
