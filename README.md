# CTF Triage Assistant
An experimental small CLI tool for initial CTF challenge inspection.

This project is a learning-focused tool that helps automate repetitive first-look checks during CTF practice. It scans a challenge folder, collects basic file information, extracts readable strings, searches for flag-like patterns, and generatees a reproducible Markdown analysis report.


## Goals
- Build a small human-in-the-loop security learning tool
- Add LLM-assisted summarization and next-step suggestions (planned)


## Current Features

### Lv1: Basic Local Inspection

- Interactive challenge folder input
- Read `description.txt`
- Read one target file: `files/challenge.txt`
- Search for flag-like patterns using regular expressions
- Run basic inspection commands:
  - `file`
  - `strings`
- Generate a Markdown analysis report

### Lv2: Broader local inspection
- Support multiple files under files/
- Add file-type-aware inspection
- Add reusable command execution function
- Check whether external commands are available before running them
- Improve error handling
- Improve Analysis report file name
- 

## Current Limitations

- The current version analyzes one target file at `files/challenge.txt`.
- Multiple file support is planned for a future version.
- The tool does not submit flags or interact with CTF platforms.
- The current version uses interactive input instead of command-line arguments.


## Usage

Run the script from the project root:

```zsh
python3 ctf_assistant.py
```

When prompted, enter the challenge folder path:

```text
examples/sample_challenge
```

The expected challenge folder structure is:

```text
examples/sample_challenge/
  description.txt
  files/
    challenge.txt
    sample_code
    image_with_flag.jpg
    Letter_from_Lorem.txt
    Letter_from_Lorem.txt.zip
```

The tool generates a Markdown report under:

```text
reports/
```
Report filenames include the challenge name and timestamp, for example:
reports/sample_challenge_20260713__153003.md

## Example Output

```text
Challenge folder path: examples/sample_challenge
Flag-like string found!
['triage_test{sample_flag_for_testing}']

[file result]
examples/sample_challenge/files/challenge.txt: ASCII text

[strings result]
This is a sample challenge file.
Most of this file is just normal text.
The flag is hidden here:
triage_test{sample_flag_for_testing}
Good Luck!

Report written to: reports/analysis.md
```


## Roadmap

- [x] Lv1: Basic local triage
- [x] Lv2: Broader local inspection
- [ ] Lv3: Report improvements
- [ ] Lv4: LLM-assisted summary
- [ ] Lv5: Human-in-the-loop command execution
- [ ] Lv6: Optional challenge import workflow


## Notes

This project is intended for CTF practice, post-event review, and authorized learning environments.

The first version intentionally keeps the workflow simple and interactive so each part of the code is easy to understand. The tool is designed to support analysis, not replace human judgment.
