import os
import subprocess


def create_project():
    # Step 1: Prompt for the parent directory path
    parent_dir = input("Enter the parent directory path: ")

    # Step 2: Prompt for project directory name
    project_name = input("Enter the project directory name: ")

    # Step 3: Sub-directories to be hard coded
    subdirectories = ["doc", "src", "data", "notes", "utils"]

    # Step 4: Files to be created
    files_to_create = [
        "README.md",
        "scribble_pad.md",
        ".env",
    ]

    # Step 5: Create project directory
    project_path = os.path.join(
        parent_dir, project_name.lower()
    )  # Convert to lowercase
    os.makedirs(project_path, exist_ok=True)  # Ensure parent directory exists

    # Step 6: Create subdirectories
    for subdir in subdirectories:
        subdir_path = os.path.join(project_path, subdir)
        os.makedirs(subdir_path, exist_ok=True)  # Ensure subdirectories are created
        # Create main.py and test.py within the "src" subdirectory
        if subdir == "src":
            with open(
                os.path.join(subdir_path, "main.py"), "w"
            ) as f:  # Convert to lowercase
                pass  # Create an empty main.py file
            with open(
                os.path.join(subdir_path, "test.py"), "w"
            ) as f:  # Convert to lowercase
                pass  # Create an empty test.py file

    # Step 7: Create files
    for file_name in files_to_create:
        file_path = os.path.join(
            project_path, file_name.lower()
        )  # Convert to lowercase
        with open(file_path, "w") as f:
            pass  # Create an empty file

    # Step 8: Copy content from root .gitignore to project .gitignore if it exists
    root_gitignore_path = os.path.join(parent_dir, ".gitignore")
    project_gitignore_path = os.path.join(project_path, ".gitignore")
    if os.path.exists(root_gitignore_path):
        with open(root_gitignore_path, "r") as src_file, open(
            project_gitignore_path, "w"
        ) as dest_file:
            dest_file.write(src_file.read())

    # Step 9: Open cmd window and load project directory
    subprocess.run(f"cd {project_path} && start cmd", shell=True)

    # Step 10: Create virtual environment and activate
    subprocess.run(
        f"cd {project_path} && python -m venv .venv && .venv\\Scripts\\activate",
        shell=True,
    )


if __name__ == "__main__":
    create_project()
