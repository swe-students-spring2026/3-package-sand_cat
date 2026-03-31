def cat_tip(skill: str, level: str) -> str:
    """
    Return a sand cat programming tip tailored to a skill and experience level.

    Args:
        skill: The programming skill to get a tip for. Valid options are
               "git", "debugging", "testing", "refactoring", "documentation".
        level: The developer's experience level. Valid options are
               "beginner", "intermediate", "expert".

    Returns:
        A cat-themed programming tip string.

    Raises:
        TypeError : If skill or level is not a string.
        ValueError: If skill or level is empty or not a valid option.
    """
    if not isinstance(skill, str):
        raise TypeError("skill must be a string")
    if not isinstance(level, str):
        raise TypeError("level must be a string")

    clean_skill = skill.strip().lower()
    clean_level = level.strip().lower()

    if not clean_skill:
        raise ValueError("skill must be a non-empty string")
    if not clean_level:
        raise ValueError("level must be a non-empty string")

    valid_skills = {"git", "debugging", "testing", "refactoring", "documentation"}
    valid_levels = {"beginner", "intermediate", "expert"}

    if clean_skill not in valid_skills:
        raise ValueError(f"skill must be one of: {', '.join(sorted(valid_skills))}")
    if clean_level not in valid_levels:
        raise ValueError(f"level must be one of: {', '.join(sorted(valid_levels))}")

    tips = {
        "git": {
            "beginner":     "Purrr... tiny tip: commit early and often. Even the sand cat saves its nap spots.",
            "intermediate": "Meow! Try rebasing instead of merging to keep history tidy — the sand cat prefers clean paw prints.",
            "expert":       "MROW. Use git bisect to hunt down bugs like a stealthy cat in the dark.",
        },
        "debugging": {
            "beginner":     "Purrr... start simple: print statements are your friend. Even cats use their senses first.",
            "intermediate": "Meow! Learn your debugger's breakpoints — the sand cat always knows where to pause and observe.",
            "expert":       "MROW. Reproduce before you fix. A cat never swipes at something it has not tracked first.",
        },
        "testing": {
            "beginner":     "Purrr... write one test for the happy path first. The sand cat learns to walk before it zooms.",
            "intermediate": "Meow! Test edge cases and invalid inputs — the sand cat knows danger lurks at the edges.",
            "expert":       "MROW. Use property-based testing to let randomness find what you could not. Cats trust instinct.",
        },
        "refactoring": {
            "beginner":     "Purrr... rename variables to mean what they hold. The sand cat would never call its tail 'thing1'.",
            "intermediate": "Meow! Extract repeated logic into small functions — the sand cat does not duplicate its grooming routine.",
            "expert":       "MROW. Refactor with tests in place first. The sand cat does not rearrange furniture in the dark.",
        },
        "documentation": {
            "beginner":     "Purrr... write a short docstring for every function you create. Even the sand cat labels its snack spots.",
            "intermediate": "Meow! Keep docs close to the code — outdated docs are worse than none. The cat knows where it left things.",
            "expert":       "MROW. Good documentation explains *why*, not *what*. Even the sand cat knows the code speaks for itself.",
        },
    }

    return tips[clean_skill][clean_level]
