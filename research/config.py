import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
DATA_DIR = os.path.join(ROOT, "research/data")


def set_project_root(levels_up=1, print_root: bool = False):
    """
    Sets the working directory to the project root.

    Parameters:
    levels_up (int): Number of levels to go up in the directory structure to reach the root.
    """
    current_dir = os.getcwd()
    project_root = os.path.abspath(os.path.join(current_dir, *[".."] * levels_up))
    os.chdir(project_root)

    if print_root:
        print(project_root)
