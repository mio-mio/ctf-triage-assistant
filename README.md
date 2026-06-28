# CTF Triage Assistant
An experimental CLI tool for initial CTF challenge inspection　and reproducible Markdown reporting.

This project is a learning-focused tool that helps automate repetitive first-look checks during CTF practice. 
It scans a challenge folder, collects basic file information, extracts readable strings, searches for flag-like patterns, and generatees a reproducible Markdown analysis report.


## Goals
- Build a small human-in-the-loop security learning tool
- Add LLM-assisted summarization and next-step suggestions (planned)


## Current Features

### Lv1: Basic Local Triage

- Interactive challenge folder input
- Read `description.txt`
- Read one target file: `files/challenge.txt`
- Search for flag-like patterns using regular expressions
- Run basic inspection commands:
  - `file`
  - `strings`
- Generate a Markdown analysis report

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
```

The tool generates a Markdown report at:

```text
reports/analysis.md
```


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
- [ ] Lv2: LLM-assisted summary
- [ ] Lv3: Human-in-the-loop command execution
- [ ] Lv4: Optional challenge import workflow


## Notes

This project is intended for CTF practice, post-event review, and authorized learning environments.

The first version intentionally keeps the workflow simple and interactive so each part of the code is easy to understand. 
The tool is designed to support analysis, not replace human judgment.
