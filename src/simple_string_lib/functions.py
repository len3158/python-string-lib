def compare_versions(version1, version2):
    # Check if inputs are strings
    if not (isinstance(version1, str) and isinstance(version2, str)):
        raise TypeError("Both version1 and version2 must be strings.")

    # Try to convert version parts to integers, raise ValueError if conversion fails
    try:
        parts1 = [int(part) for part in version1.split('.')]
        parts2 = [int(part) for part in version2.split('.')]
    except ValueError:
        raise ValueError("Invalid version number format.")

    # Split the version strings into parts
    parts1 = [int(part) for part in version1.split('.')]
    parts2 = [int(part) for part in version2.split('.')]

    # Compare each part
    for part1, part2 in zip(parts1, parts2):
        if part1 < part2:
            return -1
        elif part1 > part2:
            return 1

    # If one string is longer and not equal to zero, it is greater
    if len(parts1) > len(parts2) and any(part != 0 for part in parts1[len(parts2):]):
        return 1
    elif len(parts2) > len(parts1) and any(part != 0 for part in parts2[len(parts1):]):
        return -1

    # Strings are equal
    return 0
