def ask_question(question, options):
    print("\n" + question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    # ✅ Guardrail: handle invalid input
    while True:
        try:
            choice = int(input("Choose option: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Invalid choice. Try again.")
        except:
            print("Please enter a number.")


def main():
    print("Welcome to Daily Reflection Agent\n")

    # 🔹 Axis 1 (Locus)
    day = ask_question(
        "How would you describe your day?",
        ["Good", "Bad", "Mixed", "Productive"]
    )

    if day in ["Good", "Productive"]:
        reason = ask_question(
            "When things went well today, what made it happen?",
            ["I worked hard", "My team helped", "I got lucky", "I adapted quickly"]
        )
        axis1 = "Internal (You took responsibility)"
    else:
        reason = ask_question(
            "When things went wrong today, what was your reaction?",
            ["I tried to fix it", "I blamed others", "I felt stuck", "I waited for help"]
        )
        axis1 = "External (You focused on outside factors)"

    # 🔹 Axis 2 (Contribution vs Entitlement)
    behavior = ask_question(
        "Which best describes your behavior today?",
        ["I helped someone", "I did extra work", "I expected recognition", "I felt others should do more"]
    )

    if behavior in ["I helped someone", "I did extra work"]:
        axis2 = "Contribution (You gave value)"
    else:
        axis2 = "Entitlement (You expected more)"

    # 🔹 Axis 3 (Self vs Others)
    focus = ask_question(
        "When thinking about your challenges today, who comes to mind?",
        ["Only me", "My team", "A colleague", "Customer"]
    )

    if focus == "Only me":
        axis3 = "Self-focused"
    else:
        axis3 = "Others-focused"

    # 🔹 Final Summary
    print("\n--- Reflection Summary ---")
    print(f"Locus: {axis1}")
    print(f"Orientation: {axis2}")
    print(f"Radius: {axis3}")
    print("\nInsight: You reflected on responsibility, contribution, and awareness.")
    print("Come back tomorrow for another reflection!")


if __name__ == "__main__":
    main()