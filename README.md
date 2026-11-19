# INFS605 Assignment 2 - IT Application Directory
City of Meridian - Internal IT Application Directory

---

## 🏗️ Project Architecture & File Structure

The project uses a modular architecture to separate user interface, data handling, and input validation:

* **`main.py`**: The application entry point. Initializes the Tkinter root window and launches the application loop.
* **`ui.py`**: Constructs the graphical user interface (GUI), layouts, buttons, entries, and Treeview display.
* **`data_manager.py`**: Manages all raw CSV read, write, update, and delete operations on the dataset.
* **`validation.py`**: Handles runtime user input validation and search filter checks before data is saved.
* **`applications.csv`**: Headerless CSV file that acts as the application's persistent database.

---

## 🛠️ Step-by-Step Setup Guide (VS Code)

### 1. Clone the Repository to Local VS Code
1. Copy the repository URL: `https://github.com/DreyzOla/INFS605-Assignment-2.git`
2. Open **VS Code**.
3. Open the Command Palette using `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (Mac).
4. Type **`Git: Clone`** and press **Enter**.
5. Paste the URL, press **Enter**, and select a local folder on your computer to save the repository.
6. When prompted by VS Code, click **Open** to load the cloned project workspace.

### 2. Run the Application
1. Open the integrated terminal in VS Code:
   * Right-click the `INFS605-Assignment-2` folder in the Explorer sidebar and select **Open in Integrated Terminal**, OR
   * Use shortcut `` Ctrl + ` `` (Windows) / `` Cmd + ` `` (Mac).
2. Execute `main.py` to launch the app:
   ```bash
   python main.py or python3 main.py on Mac


# Collaborator Git Workflow
Always run git pull BEFORE starting any work to ensure you have the latest code.
Always commit and git push once your changes are tested and ready so other collaborators can see your updates!


# Start of Work Session (Pull Latest Changes)
git pull

# Check Modified Files
git status

# Stage, Commit, and Push Your Changes
git add . - Stage all changed files
git commit -m "Brief description of work done"
git push.  - push your code into github

# Create personal branch and other procedures
1 git checkout -b name-of-your-branch
2 First time pushing this specific branch: git push --set-upstream origin feature-branch-name
3 For any subsequent pushes on this branch: git push

# Create & Merge Pull Request on GitHub
1 Open your repository on GitHub.

2 Click Compare & pull request next to your recently pushed branch.

3 Review your code diff, add a brief title/description, and click Create pull request.

4 Once reviewed or verified, click Merge pull request, then Confirm merge.

# Pull Merged Changes into Local main
1 git checkout main or manually select main
2 git pull

# Recommended Workflow Process

1 Keep the main branch as the clean, assignment-ready code.

2 For each new feature or code modification, pull the main branch and create a single-purpose branch (e.g., git checkout -b build-input-form).

3 Commit your code to GitHub and create a pull request.

4 Have someone else on the team test the changes before merging into the main branch.

5 Make sure the code works and integrates cleanly with the existing code without issues before merging into main.


#NOTE: if anything is unclear, gemini or chatgpt can clear up the questions.