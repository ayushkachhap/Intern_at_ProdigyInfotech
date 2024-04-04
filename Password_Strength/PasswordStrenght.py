def assess_password_strength(password):
 
  score = 0
  feedback = ""

  
  if len(password) < 8:
    feedback += "Password is too short. Aim for at least 8 characters.\n"
  else:
    score += 1

  
  has_uppercase = any(char.isupper() for char in password)
  has_lowercase = any(char.islower() for char in password)
  has_number = any(char.isdigit() for char in password)
  has_special = any(not char.isalnum() for char in password)

  if has_uppercase:
    score += 1
  else:
    feedback += "Include uppercase letters (A-Z).\n"
  if has_lowercase:
    score += 1
  else:
    feedback += "Include lowercase letters (a-z).\n"
  if has_number:
    score += 1
  else:
    feedback += "Include numbers (0-9).\n"
  if has_special:
    score += 1
  else:
    feedback += "Include special characters (e.g., !@#$%^&*). \n"

 
  if score == 0:
    feedback += "Password is very weak. Please consider using a stronger password."
  elif score <= 2:
    feedback += "Password is weak. Consider adding more complexity with different character types."
  elif score == 3:
    feedback += "Password is moderately strong."
  elif score == 4:
    feedback += "Password is strong."
  else:
    feedback += "Password is very strong."

  return score, feedback

password = input("Enter your password: ")
score, feedback = assess_password_strength(password)

print(f"Password strength score: {score}")
print(feedback)
