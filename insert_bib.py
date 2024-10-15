def insert_file_content(readme_path, file_to_insert):
    # Read README.md content
    with open(readme_path, 'r') as readme:
        readme_content = readme.readlines()

    # Read the content of the file to be inserted
    with open(file_to_insert, 'r') as file:
        insert_content = file.read()

    # Find the marker in README.md where the file content should be inserted
    new_content = []
    marker = f"<!-- {file_to_insert} start -->" 
    inside_marker = False
    for line in readme_content:
        if marker in line and not inside_marker:
            new_content.append(line)
            new_content.append(insert_content)  # Insert the file content here
            inside_marker = True
        elif marker in line and inside_marker:
            inside_marker = False
        elif not inside_marker:
            new_content.append(line)
            
    # Write back to README.md
    with open(readme_path, 'w') as readme:
        readme.writelines(new_content)


# Example usage
insert_file_content('README.md', 'bib.html')