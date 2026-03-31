from sandcat_fun import (
    cat_greeting,
    cat_comfort,
    cat_energy,
    draw_cat,
    get_fortune,
    cat_reaction,
    cat_snack,
    cat_tip,
)

def main():
    print("=== Sand Cat Package Demo ===\n")

    print("1. Greeting")
    print(cat_greeting("Tuo", "happy"))
    print()

    print("2. Comfort")
    print(cat_comfort(3))
    print()

    print("3. Draw")
    print(draw_cat("coding"))
    print()

    print("4. Cat Energy")
    print(cat_energy("sunny", 8))
    print()

    print("5. Get Fortune")
    print(get_fortune(5))
    print()

    print("6. Cat Reaction")
    print(cat_reaction("bug_fixed", 3))
    print()
    print(cat_reaction("monday", 2))
    print()

    print("7. Cat Snack")
    print(cat_snack("coffee", 3))
    print()
    print(cat_snack("water", 5))
    print()

    print("8. Cat Tip")
    print(cat_tip("git", "beginner"))
    print()
    print(cat_tip("debugging", "expert"))
    print()


if __name__ == "__main__":
    main()