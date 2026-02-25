import re
def check_strength(password):
    score = 0
    feedback = []
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use minimum 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")
        
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")
        
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$...).")
    return score, feedback

def show_result(score):
    print("\n Password Strength:")

    if score <= 2:
        print(" Weak")
    elif score == 3:
        print(" Medium")
    elif score == 4:
        print(" Strong")
    else:
        print(" Very Strong")

print("===")
print("PASSWORD STRENGTH CHECKER")
print("====")

while True:
    user_password = input("\nEnter Password (type exit to quit): ")

    if user_password.lower() == "exit":
        print("Program Ended")
        break

    score, feedback = check_strength(user_password)
    show_result(score)

    if feedback:
        print("\n Suggestions:")
        for item in feedback:
            print("-", item)
    else:
        print(" Excellent Password!")
