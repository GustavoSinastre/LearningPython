# This code is a class where I'm learning how to work with strings


# Let's set the client e-mail 
client_email = "Luis.aleatorio@gmail.com"
client_name = "luis animal dos santos"
print(client_email)

# Transforming in upper letters
client_email = client_email.upper()
print(client_email)

# Repair that when we work with a variable, we need to call it and put the new treatment

# Transforming in lower letters
client_email = client_email.lower()
print(client_email)

# Finding a character in text
find_charact = client_email.find("@") # Returns -1 when not found
print(find_charact)

# Text size
size_email = len(client_email)
print(size_email)

# Find a character in text using coordinates
# In Python, the count starts in 0, 1, 2, 3, and we can use the reverse count, using -1, -2, -3
find_character_normal_order = client_email[3]
print(find_character_normal_order)

find_character_reverse_order = client_email[-3]
print(find_character_reverse_order)

# Finding a text until a determined index
find_text_until_character = client_email[:4]
print(find_text_until_character)

# Finding text from one index to another
find_text_from_until_character = client_email[5:14]
print(find_text_from_until_character)

# Changing a piece of the text
changed_client_email = client_email.replace("@gmail.com","@crap.com")
print(changed_client_email)

# Formating a name with the first letter capitalized
client_name_formated_first_capitalized = client_name.capitalize() # Only first letter capitalized
client_name_total_formated = client_name.title()
print(client_name_formated_first_capitalized)
print(client_name_total_formated)

# Now we will extract the e-mail server using the same items learned above
atsign_position = client_email.find("@")
print(atsign_position)
email_server = client_email[atsign_position+1:]
print(email_server)

# Using split function to break de name
split_name = client_name.split()
firs_client_name = split_name[0] if len(split_name) > 0 else ""
second_client_name = split_name[1] if len(split_name) > 1 else ""
complement_client_name = split_name[2] if len(split_name) > 2 else ""
last_client_name = split_name[-1] if len(split_name) > 3 else ""

print(firs_client_name.title())
print(second_client_name.title())
print(complement_client_name.title())
print(last_client_name.title())