# GitHub User Activity Tracker

This is a simple command-line tool built in Python to fetch and display the recent public activity of any GitHub user. It uses the official GitHub API to retrieve the data.

---

## Features

- Fetches the latest public events for a specified GitHub username.
- Provides a clean, human-readable summary of activities like pushes, repository stars/watches, and creations.

---

## Prerequisites

- Python 3
- The `requests` library

---

## Setup

1. **Clone the repository or download the script.**

2. **Install the required Python library:**
```bash
pip install requests
```

---

## Usage

Run the script from your terminal, passing the target GitHub username as an argument.

**Syntax:**
```bash
python3 github-activity.py <username>
```

**Example:**
```bash
python3 github-activity.py torvalds
```

### Example Output
```
torvalds pushed 1 commits to torvalds/linux.
torvalds did Create on torvalds/test-tars.
torvalds did Watch or Star on ggerganov/llama.cpp.
...
```