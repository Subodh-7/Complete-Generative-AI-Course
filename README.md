# Complete Generative AI Course

## Course Name
**Complete Generative AI Course With LangChain and Hugging Face**

## Repository Purpose
This repository is a curated collection of code, notebooks, and notes created as part of a 23-day Generative AI learning journey. It covers foundational Python, LangChain, Hugging Face Transformers, and hands-on projects that build up to real-world generative AI applications.

The goal is to track daily progress, document learnings, and provide a reproducible environment for experimenting with LLMs, prompt engineering, embeddings, and agentic workflows.

## Folder Structure
```
Complete-Generative-AI-Course/
├── .gitignore              # Ignores virtual environments, caches, and OS files
├── README.md               # This file
├── app.py                  # Entry point for running the project
├── requirements.txt        # Python dependencies
├── venv/                   # Local virtual environment (ignored by Git)
├── .venv/                  # Alternative virtual environment (ignored by Git)
└── Day 1/                  # Daily learning folders
    └── Variables.ipynb     # Day 1 notebook: Python variables and operators
└── Day 2/                  # Daily learning folders
    └── Loops.ipynb         # Day 2 notebook: Control flow and loops
└── Day 3/                  # Daily learning folders
    └── Data_Structures.ipynb   # Day 3 notebook: Data structures (lists, tuples, dicts)
```

## Progress Tracker (23 Days)

| Day | Topic | Status |
|-----|-------|--------|
| 1 | Python Variables and Operators | ✅ Done |
| 2 | Control Flow and Loops | ✅ Done |
| 3 | Data Structures (Lists, Tuples, Dictionaries) | ✅ Done |
| 4 | Functions and Modules | ⏳ Pending |
| 5 | Functions | ✅ Done |
| 6 | Error Handling | ⏳ Pending |
| 7 | Object-Oriented Programming | ⏳ Pending |
| 8 | Introduction to LangChain | ⏳ Pending |
| 9 | Prompts and Prompt Templates | ⏳ Pending |
| 10 | Models (LLMs & Chat Models) | ⏳ Pending |
| 11 | Chains | ⏳ Pending |
| 12 | Agents and Tools | ⏳ Pending |
| 13 | Memory and State | ⏳ Pending |
| 14 | Indexes and Retrievers | ⏳ Pending |
| 15 | Embeddings | ⏳ Pending |
| 16 | Vector Stores | ⏳ Pending |
| 17 | Question Answering | ⏳ Pending |
| 18 | Text Summarization | ⏳ Pending |
| 19 | Hugging Face Transformers | ⏳ Pending |
| 20 | Fine-tuning and Inference | ⏳ Pending |
| 21 | Building a Generative AI App | ⏳ Pending |
| 22 | Evaluation and Testing | ⏳ Pending |
| 23 | Final Project & Deployment | ⏳ Pending |

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
