import argparse

from .assessment import Assessment
from .data import AGE_RANGES, FREQUENCIES, SEVERITIES, TRAUMA_BRAIN_REGIONS


def prompt_choice(prompt: str, choices: list[str]) -> str:
    while True:
        print(f"{prompt} ({', '.join(choices)})")
        choice = input().strip().lower()
        normalized = {c.lower(): c for c in choices}
        if choice in normalized:
            return normalized[choice]
        print("Invalid choice. Try again.")


def run_interactive() -> None:
    gender = prompt_choice("Select biological sex", ["male", "female"])
    assessment = Assessment(gender)

    print("Select trauma types separated by comma from the following:")
    print(", ".join(TRAUMA_BRAIN_REGIONS.keys()))
    trauma_input = input().strip().lower()
    traumas = [t.strip() for t in trauma_input.split(",") if t.strip()]

    for trauma in traumas:
        if trauma not in TRAUMA_BRAIN_REGIONS:
            print(f"Skipping unknown trauma type: {trauma}")
            continue
        age = prompt_choice(f"Age range for {trauma}", AGE_RANGES)
        freq = prompt_choice(f"Frequency for {trauma} at age {age}", FREQUENCIES)
        sev = prompt_choice(f"Severity for {trauma} at age {age}", SEVERITIES)
        assessment.add_occurrence(trauma, age, freq, sev)

    print()
    print(assessment.generate_report())


def main() -> None:
    parser = argparse.ArgumentParser(description="AI Blackened Management System")
    parser.add_argument(
        "--interactive", action="store_true", help="Run in interactive mode"
    )
    args = parser.parse_args()

    if args.interactive:
        run_interactive()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
