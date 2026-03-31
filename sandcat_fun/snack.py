def cat_snack(snack: str, quantity: int) -> str:
    """
    Return a sand cat reaction to your coding snack and how much of it you had.

    Args:
        snack   : The snack being consumed. Valid options are
                  "coffee", "tea", "chips", "cookies", "water".
        quantity: How many servings (1 to 5).

    Returns:
        A cat-themed snack reaction string.

    Raises:
        TypeError : If snack is not a string or quantity is not an integer.
        ValueError: If snack is empty, not a valid option, or quantity is
                    outside 1-5.
    """
    if not isinstance(snack, str):
        raise TypeError("snack must be a string")
    if not isinstance(quantity, int) or isinstance(quantity, bool):
        raise TypeError("quantity must be an integer")

    clean_snack = snack.strip().lower()

    if not clean_snack:
        raise ValueError("snack must be a non-empty string")

    valid_snacks = {"coffee", "tea", "chips", "cookies", "water"}
    if clean_snack not in valid_snacks:
        raise ValueError(f"snack must be one of: {', '.join(sorted(valid_snacks))}")

    if quantity < 1 or quantity > 5:
        raise ValueError("quantity must be between 1 and 5")

    messages = {
        "coffee": {
            1: "Meow. One coffee? The sand cat respects your measured approach.",
            2: "Purrr. Two coffees — productivity is warming up nicely.",
            3: "Meow! Three coffees?! The sand cat's eyes are wide with respect.",
            4: "Purrr... four coffees? The sand cat is concerned but supportive.",
            5: "MROW!! FIVE COFFEES?! The sand cat strongly suggests water soon!",
        },
        "tea": {
            1: "Meow. A calming cup of tea — the sand cat approves.",
            2: "Purrr. Two teas — wise and soothing. Very cat-like.",
            3: "Meow. Three teas? The sand cat nods peacefully.",
            4: "Purrr... four teas? You are practically a tea-powered machine.",
            5: "MROW! Five teas! The sand cat is impressed by your dedication.",
        },
        "chips": {
            1: "Meow. One serving of chips — respectable snacking.",
            2: "Purrr. Two servings? The crunch is real. The sand cat hears you.",
            3: "Meow! Three servings of chips?! The sand cat eyes your bag hopefully.",
            4: "Hiss... four servings? The sand cat judges slightly but understands.",
            5: "HISS!! FIVE bags of chips?! The sand cat is sliding you a salad.",
        },
        "cookies": {
            1: "Meow. One cookie — a perfectly sweet reward for your work.",
            2: "Purrr. Two cookies! You must have done something good today.",
            3: "Meow! Three cookies?! The sand cat is sneaking one off your plate.",
            4: "Purrr... four cookies? No judgment from this cat. You deserve it.",
            5: "MROW!! Five cookies?! The sand cat admires your commitment to dessert.",
        },
        "water": {
            1: "Meow. One glass of water — the sand cat is pleased.",
            2: "Purrr. Two glasses! Great hydration habits. The cat approves.",
            3: "Purrr! Three glasses of water? You are thriving!",
            4: "Meow! Four glasses! The sand cat is proud. Keep going!",
            5: "PURRR!! FIVE glasses of water?! The sand cat is your biggest fan!",
        },
    }

    return messages[clean_snack][quantity]
