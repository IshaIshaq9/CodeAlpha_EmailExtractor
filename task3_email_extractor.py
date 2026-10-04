# ===== TASK 3: TASK AUTOMATION — EMAIL EXTRACTOR =====
# .txt file se saare email addresses nikaal kar dusri file me save karta hai

import re   # regular expressions: pattern matching ke liye
import os   # os module: file exist check karne ke liye

input_file = "input.txt"      # jis file se emails nikalne hain
output_file = "emails.txt"    # jis file me emails save honge

# Agar input.txt nahi hai to demo ke liye ek sample file bana do
if not os.path.exists(input_file):
    with open(input_file, "w") as f:
        f.write("Contact us at info@codealpha.tech or services.codealpha@gmail.com.\n"
                "Personal: ali123@example.com, sara_k@test.org\n"
                "Ye line me koi email nahi hai.")
    print("Sample 'input.txt' bana di gayi.")

# File ko read mode me kholo
with open(input_file, "r") as f:
    text = f.read()           # poori file ka text ek string me

# Email ka regex pattern:
# [A-Za-z0-9._%+-]+  -> username part
# @                  -> @ symbol
# [A-Za-z0-9.-]+     -> domain name
# \.[A-Za-z]{2,}     -> .com, .org jaisa extension
pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

emails = re.findall(pattern, text)       # text me saare matches dhundo
unique_emails = sorted(set(emails))      # duplicates hatao (set) aur sort karo

# Emails ko output file me save karo
with open(output_file, "w") as f:
    for email in unique_emails:          # har email ke liye
        f.write(email + "\n")            # nayi line me likho

print(f"{len(unique_emails)} email(s) mile aur '{output_file}' me save ho gaye:")
for email in unique_emails:
    print(" -", email)
