import re


def is_valid_windows_path(path_string):
    """
    Checks if a string is a syntactically valid Windows path.
    This does not check if the path actually exists on the filesystem.
    """
    if not isinstance(path_string, str):
        return False

    # Check for invalid characters in Windows paths
    # Characters like <, >, :, ", /, \, |, ?, * are generally not allowed
    # in file or directory names, and some are path separators.
    # We're focusing on invalid characters within path components, not separators.
    invalid_chars_pattern = r'[<>:"|?*]'
    if re.search(invalid_chars_pattern, path_string):
        return False

    # Check for reserved device names (e.g., CON, PRN, AUX, NUL, COM1-9, LPT1-9)
    # These names are invalid as file or directory names, especially at the root of a drive or as a standalone component.
    reserved_names = [
        "CON", "PRN", "AUX", "NUL",
        "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
        "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"
    ]
    # Split path into components to check for reserved names
    path_components = re.split(r'[\\/]', path_string)
    for component in path_components:
        if component.upper() in reserved_names:
            return False

    # Basic check for drive letter format (e.g., C:\)
    # This is a simplification; more robust checks might be needed for UNC paths etc.
    if len(path_components) > 0 and len(path_components[0]) == 2 and path_components[0][1] == ':' and path_components[0][0].isalpha():
        # Valid drive letter, continue checks
        pass
    elif len(path_components) > 0 and path_components[0] == '': # UNC path or absolute path from root
        pass
    elif len(path_string) > 0 and path_string[0] == '\\': # Relative path from current drive root or UNC
        pass
    elif len(path_string) > 0 and path_string[0].isalpha() and len(path_string) > 1 and path_string[1] == ':': # Drive letter without a backslash
        pass
    elif len(path_string) > 0 and path_string[0] != '\\' and path_string[0] != '/': # Relative path
        pass
    else:
        return False # Doesn't seem to start like a valid path

    # Check for path length limits (Windows paths have a MAX_PATH limit, typically 260 characters)
    # This is a soft check as the actual limit can vary (e.g., with long path support enabled)
    if len(path_string) > 260:
        return False

    return True