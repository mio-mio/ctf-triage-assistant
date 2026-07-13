# CTF Triage Assistant

An experimental CLI tool for initial CTF challenge inspection.

This project is a learning-focused tool that helps automate repetitive first-look checks during CTF practice. It scans a challenge folder, collects basic file information, extracts readable strings, searches for flag-like patterns, and generates a reproducible Markdown analysis report.

## Goals

- Build a small human-in-the-loop security learning tool
- Gradually extend the tool with LLM-assisted summarization and human-in-the-loop workflows

## Design Philosophy

The project is developed incrementally. Each milestone focuses on a small, understandable improvement rather than building a fully autonomous solver from the beginning.


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

- Support multiple files under `files/`
- Run file-type-aware inspection commands
- Execute reusable inspection commands through a shared helper function
- Check whether external commands are available before execution
- Improve error handling for missing files and tools
- Generate timestamped Markdown analysis reports

### Inspection Commands

The current version supports:
- `file`
- `strings`
- `exiftool` *(image)*
- `readelf -h` *(ELF)*
- `objdump -f` *(ELF)*
- `unzip -v` *(ZIP)*

## Current Limitations

- The tool analyzes one challenge directory at a time.
- Batch analysis of multiple challenge directories is not yet supported.
- File-type-aware inspection currently relies on simple matching against `file` command output.
- Optional inspection commands must be installed separately.
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

Report filenames include the challenge name and timestamp, for example:

```text
reports/sample_challenge_20260713_153003.md
```

## Example Output

A sample generated report is available at:

`reports/sample_report.md`

## Roadmap

- [x] Lv1: Basic local triage
- [x] Lv2: Broader local inspection
- [ ] Lv3: Report and challenge metadata improvements
- [ ] Lv4: LLM-assisted summary
- [ ] Lv5: Human-in-the-loop command execution
- [ ] Lv6: Optional challenge import workflow
- [ ] Lv7: Batch challenge analysis

## Notes

This project is intended for CTF practice, post-event review, and authorized learning environments.

The project intentionally keeps the workflow simple and interactive so the implementation remains easy to understand while new features are added incrementally. The tool is designed to support analysis, not replace human judgment.
