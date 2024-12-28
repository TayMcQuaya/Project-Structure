import os

def generate_ascii_tree(root_dir, output_file):
    """
    Generates an ASCII tree representing the directory structure of the given root directory.

    :param root_dir: The root directory to analyze.
    :param output_file: The path to the output text file.
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            def tree(dir_path, prefix=''):
                # Get list of directories and files
                try:
                    entries = sorted(os.listdir(dir_path))
                except PermissionError:
                    # Indicate permission issues and skip the directory
                    file.write(f"{prefix}└── [Permission Denied]\n")
                    return
                entries_count = len(entries)
                for index, entry in enumerate(entries):
                    path = os.path.join(dir_path, entry)
                    connector = '├── ' if index < entries_count - 1 else '└── '
                    file.write(f"{prefix}{connector}{entry}\n")
                    
                    if os.path.isdir(path):
                        extension = '│   ' if index < entries_count - 1 else '    '
                        tree(path, prefix + extension)
        
            # Write the root directory
            root_name = os.path.basename(os.path.abspath(root_dir))
            if root_name == '':
                # This handles the case when root_dir is a root like '/'
                root_name = root_dir
            file.write(f"{root_name}/\n")
            tree(root_dir)
        
        print(f"ASCII project structure has been written to '{output_file}'.")
    except IOError as e:
        print(f"Error writing to '{output_file}': {e}")

def manage_gitignore(root_dir, entries_to_ignore):
    """
    Creates or updates the .gitignore file in the root directory to include specified entries.

    :param root_dir: The root directory of the project.
    :param entries_to_ignore: A list of file or directory names to ignore.
    """
    gitignore_path = os.path.join(root_dir, '.gitignore')
    existing_entries = set()

    # If .gitignore exists, read its current entries
    if os.path.isfile(gitignore_path):
        try:
            with open(gitignore_path, 'r', encoding='utf-8') as gitignore_file:
                existing_entries = set(line.strip() for line in gitignore_file if line.strip() and not line.startswith('#'))
        except IOError as e:
            print(f"Error reading '.gitignore': {e}")
            return

    # Determine which entries need to be added
    new_entries = set(entries_to_ignore) - existing_entries

    if new_entries:
        try:
            with open(gitignore_path, 'a', encoding='utf-8') as gitignore_file:
                if os.path.isfile(gitignore_path) and os.path.getsize(gitignore_path) > 0:
                    gitignore_file.write('\n')  # Ensure there's a newline before appending
                for entry in sorted(new_entries):
                    gitignore_file.write(f"{entry}\n")
            print(f"Added {len(new_entries)} entries to '.gitignore'.")
        except IOError as e:
            print(f"Error writing to '.gitignore': {e}")
    else:
        print("'.gitignore' already contains all specified entries. No changes made.")

def main():
    import argparse

    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Analyze a project folder, create an ASCII tree text file, and manage .gitignore.')
    parser.add_argument('root_dir', nargs='?', default='.', help='The root directory of the project (default: current directory).')
    parser.add_argument('-o', '--output', default='project_structure.txt', help='The output text file (default: project_structure.txt).')

    args = parser.parse_args()

    # Get absolute path of the root directory
    root_directory = os.path.abspath(args.root_dir)
    
    # Check if the root directory exists
    if not os.path.isdir(root_directory):
        print(f"Error: The directory '{root_directory}' does not exist.")
        return

    output_file = os.path.join(root_directory, args.output)

    # Check if the output file exists
    if os.path.isfile(output_file):
        print(f"Existing '{args.output}' found and will be overwritten.")

    # Generate the ASCII tree
    generate_ascii_tree(root_directory, output_file)

    # Manage .gitignore
    entries_to_ignore = ['project_structure.py', 'project_structure.txt']
    manage_gitignore(root_directory, entries_to_ignore)

if __name__ == "__main__":
    main()
