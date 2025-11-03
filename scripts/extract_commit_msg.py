#!/usr/bin/env python3
"""Extract commit message and title for GitHub Actions output."""
import os
import uuid
from pathlib import Path

# Read commit message from file or use default
commit_msg_path = Path("data/commit_message.txt")
if commit_msg_path.exists():
    commit_msg = commit_msg_path.read_text().strip()
else:
    commit_msg = "chore: refresh cybersecurity brief"

# Extract title (first line)
title = commit_msg.split('\n')[0]

# Write to GitHub Actions output using unique delimiters
delimiter_msg = f"ghadelimiter_{uuid.uuid4().hex}"
delimiter_title = f"ghadelimiter_{uuid.uuid4().hex}"

with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as handle:
    handle.write(f"message<<{delimiter_msg}\n")
    handle.write(commit_msg + "\n")
    handle.write(f"{delimiter_msg}\n")
    handle.write(f"title<<{delimiter_title}\n")
    handle.write(title + "\n")
    handle.write(f"{delimiter_title}\n")
