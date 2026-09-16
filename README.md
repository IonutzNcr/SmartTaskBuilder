# SmartTaskBuilder

SmartTaskBuilder is a small CLI prototype for managing a personal todo list with a lightweight AI layer.
The project was created as a learning experiment and proof of concept for combining:

- task tracking,
- profile management,
- categories,
- search/filter/sort features,
- and AI-generated task suggestions.

## Status

This project is currently a prototype and is considered abandoned.
It was built as a personal experimentation project and is not maintained as a production-ready application.
The codebase still contains rough edges, unfinished features, and incomplete persistence logic.

## What it tries to do

- manage tasks by category,
- support multiple profiles,
- display tasks in a CLI table,
- search tasks by content,
- filter and sort tasks,
- generate tasks from a prompt using OpenAI,
- persist data locally in JSON files.

## Main structure

```text
smartTaskBuilder/
├── README.md
├── cliapplication/
│   ├── core.py
│   ├── sitecustomize.py
│   ├── modules/
│   │   ├── App.py
│   │   ├── Category.py
│   │   ├── Command.py
│   │   ├── Displayer.py
│   │   ├── EventListener.py
│   │   ├── Filter.py
│   │   ├── OpenAi.py
│   │   ├── Printer.py
│   │   ├── Profile.py
│   │   ├── Searcher.py
│   │   ├── Sorter.py
│   │   ├── Storage.py
│   │   ├── Task.py
│   │   ├── tasks.json
│   │   └── properties.json
│   └── tests/
│       ├── test_filtering.py
│       ├── test_init_task.py
│       ├── test_pandas.py
│       └── test_sorting.py
└── .venv/
```

## Features attempted

The following ideas were explored during the prototype phase:

- add / delete task
- search tasks
- create categories
- create profiles
- switch profiles
- dynamic sorting and filtering
- AI-generated task suggestions
- basic persistence to JSON

## Known limitations

This prototype is not considered complete.
Important limitations include:

- fragile import structure,
- non-robust persistence,
- imperfect OpenAI integration,
- partial or inconsistent filtering/sorting behavior,
- debugging prints left in the code,
- no proper production-level CLI lifecycle,
- no guarantee of long-term compatibility or maintenance.

## Notes

This repository should be treated as a historical prototype and a learning project rather than as a stable application.
It may still be useful for reference, experimentation, or future rework.

## Setup

This project is a prototype and is not maintained actively. To run it locally, you need:

1. Python 3.13+
2. A virtual environment
3. The required Python packages
4. An OpenAI API key stored in the environment variable `OPENAI_API_KEY`

### 1) Create a virtual environment

From the project root:

```bash
cd /home/yoyo/smartTaskBuilder
python3 -m venv .venv
```

### 2) Activate the virtual environment

```bash
cd /home/yoyo/smartTaskBuilder
. .venv/bin/activate
```

### 3) Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install openai python-dotenv pandas pytest
```

### 4) Set the environment variable

On Linux/macOS:

```bash
export OPENAI_API_KEY="your_openai_api_key_here"
```

To keep it for the current shell session only, the command above is enough.
For a more permanent setup, you can add it to your shell profile or create a `.env` file at the project root.

Example `.env`:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Note: the project uses `python-dotenv`, so if a `.env` file exists in the project and is loaded correctly, it can be used automatically.

### 5) Run the app

```bash
cd /home/yoyo/smartTaskBuilder/cliapplication
python3 core.py
```

If you are already inside the activated venv, this is enough. If not, first activate the venv:

```bash
cd /home/yoyo/smartTaskBuilder
. .venv/bin/activate
cd cliapplication
python3 core.py
```

## Important

This project is not actively maintained and should not be expected to be production-ready.
It is kept here mainly for archival and reference purposes.
