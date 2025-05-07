def main():
    scores = []

    print("=======================")
    print("=  Grade  Calculator  =")
    print("=======================")

    while True:
        try:
            print("======  CHOICES  ======")
            print("\n1. Add Score")
            print("2. Calculate Average")
            print("3. Exit")

            try:
                choice = int(input("Enter your choice (1-3): "))

                if choice == 1:
                    subject = input("Enter the subject: ").strip()
                    try:
                        score = float(input("Enter the score: "))
                        if 0 <= score <= 100:
                            scores.append(score)
                            print("Score added.")
                        else:
                            print("Score must be between 0 and 100.")
                    except ValueError:
                        print("Invalid score. Please enter a number.")
                elif choice == 2:
                    if scores:
                        average = sum(scores) / len(scores)
                        print(f"Average Grade: {average:.2f}")
                    else:
                        print("No scores added yet.")
                elif choice == 3:
                    print("Exiting program. Goodbye!")
                    break
                else:
                    print("Invalid choice. Enter 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        except ValueError:
            print("Invalid input. Please enter a number.")