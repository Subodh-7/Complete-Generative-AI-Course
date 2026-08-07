# Complete Generative AI Course

## Course Name
**Complete Generative AI Course With LangChain and Hugging Face**

## Repository Purpose
This repository is a curated collection of code, notebooks, and notes created as part of a 23-day Generative AI learning journey. It covers foundational Python, LangChain, Hugging Face Transformers, and hands-on projects that build up to real-world generative AI applications.

The goal is to track daily progress, document learnings, and provide a reproducible environment for experimenting with LLMs, prompt engineering, embeddings, and agentic workflows.

## Folder Structure
```
Complete-Generative-AI-Course/
├── .gitignore
├── README.md
├── app.py
├── requirements.txt
├── Day 1/
│   ├── Variables.ipynb        # Day 1: Python Variables and Operators (✅ Done)
│   └── test.ipynb
├── Day 2/
│   ├── ConditionalStatements.ipynb  # Day 2: Control Flow - Conditionals (✅ Done)
│   ├── Datatypes.ipynb              # Day 2: Data Types (✅ Done)
│   ├── Loops.ipynb                  # Day 2: Control Flow and Loops (✅ Done)
│   └── Operators.ipynb              # Day 2: Operators (✅ Done)
├── Day 3/
│   └── Data Structures/
│       ├── Lists.ipynb      # Day 3: Data Structures - Lists (✅ Done)
│       └── Tuples.ipynb     # Day 3: Data Structures - Tuples (✅ Done)
├── Day 4/
│   └── Data Structures/
│       ├── Dictionaries.ipynb  # Day 4: Data Structures - Dictionaries (✅ Done)
│       └── ListExamples.ipynb  # Day 4: Data Structures - Lists (✅ Done)
├── Day 5/
│   └── Functions/
│       ├── functions.ipynb       # Day 5: Functions - Lambda, Map and Filter (✅ Done)
│       ├── examplesFunctions.ipynb
│       ├── Mapsfunction.ipynb
│       ├── Lambda.ipynb
│       ├── filterfunction.ipynb
│       └── sample.txt
├── Day 6/
│   └── Modules/        # Day 6: Python Modules and Standard Library (✅ Done)
│       ├── import.ipynb           # Importing modules, packages
│       ├── Standardlibrary.ipynb  # Standard library overview
│       ├── destination.txt
│       ├── example.csv
│       ├── source.txt
│       ├── test.py
│       └── package/
│           ├── __init__.py
│           ├── maths.py
│           └── subpackages/
│               ├── __init__.py
│               └── mult.py
├── Day 7/
│   └── File Handling/  # Day 7: File Handling (✅ Done)
│       ├── fileoperation.ipynb
│       ├── filepath.ipynb
│       ├── example.txt
│       ├── example.bin
│       ├── destination.txt
│       └── output.txt
├── Day 8/
│   └── Exception Handling/  # Day 8: Exception Handling (✅ Done)
│       ├── exception.ipynb
│       └── example1.txt
```

## Progress Tracker (25 Days)

| Day | Topic | Status |
|-----|-------|--------|
| 1 | Python Variables and Operators | ✅ Done |
| 2 | Control Flow and Loops | ✅ Done |
| 3 | Data Structures (Lists, Tuples, Dictionaries) | ✅ Done |
| 4 | Data Structures (Lists, Dictionaries) | ✅ Done |
| 5 | Functions (Lambda, Map, Filter) | ✅ Done |
| 6 | Modules and Standard Library | ✅ Done |
| 7 | File Handling | ✅ Done |
| 8 | Exception Handling | ✅ Done |
| 9 | Object-Oriented Programming | ✅ Done |
| 10 | Introduction to LangChain | ⏳ Pending |
| 11 | Prompts and Prompt Templates | ⏳ Pending |
| 12 | Models (LLMs & Chat Models) | ⏳ Pending |
| 13 | Chains | ⏳ Pending |
| 14 | Agents and Tools | ⏳ Pending |
| 15 | Memory and State | ⏳ Pending |
| 16 | Indexes and Retrievers | ⏳ Pending |
| 17 | Embeddings | ⏳ Pending |
| 18 | Vector Stores | ⏳ Pending |
| 19 | Question Answering | ⏳ Pending |
| 20 | Text Summarization | ⏳ Pending |
| 21 | Hugging Face Transformers | ⏳ Pending |
| 22 | Fine-tuning and Inference | ⏳ Pending |
| 23 | Building a Generative AI App | ⏳ Pending |
| 24 | Evaluation and Testing | ⏳ Pending |
| 25 | Final Project & Deployment | ⏳ Pending |

## Latest Progress

**Date:** 2026-08-05

**Newly Completed Day(s):** Day 8 - Exception Handling (completed on 2026-08-05 via commit `cd4e7ec`)

**Files Added in Latest Session:**
- Day 8/Exception Handling/exception.ipynb
- Day 8/Exception Handling/example1.txt

**Current Progress:** 8/25 Days Completed (32%)

**Next Topic:** Day 9 - Object-Oriented Programming (OOP in Python: Classes, Objects, Inheritance, Polymorphism, Encapsulation)

## Technologies Used
- **Python** - Core programming language
- **LangChain** - Framework for developing applications powered by language models
- **Hugging Face** - Transformers and datasets for NLP
- **Jupyter Notebooks** - Interactive development and experimentation
- **VS Code** - Code editor
- **Git** - Version control

## VS Code Configuration Fixes (Completed)
To restore full IntelliSense, Pylance, and Jupyter notebook code-completion support, we repaired the workspace's VS Code settings:

- Set `python.languageServer` to **Pylance**
- Enabled **quick suggestions**, **parameter hints**, **hover documentation**, and **inline completions**
- Configured auto-import and suggestion behavior for smoother coding
- Restored notebook-specific IntelliSense settings

These changes were applied in `.vscode/settings.json` and the Python language server was restarted, fully re-enabling code completion, auto-import, and documentation assistance.

## How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/Subodh-7/Complete-Generative-AI-Course.git
cd Complete-Generative-AI-Course
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```

### 5. Explore the notebooks
Open any notebook in a `Day N` folder using Jupyter:
```bash
jupyter notebook
```

## License
This repository is for educational purposes.