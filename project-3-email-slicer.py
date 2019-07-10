# Brian Snitzer
# July 10, 2019
# Exploring string methods

# Get user email
email = input("What is your email address?:").strip()

# Slice out user user_name
user = email[:email.index("@")]

# slice out domain
domain = email[email.index("@") + 1:]

# format message

message = "Your user name is {} and your domain name is {}".format(user,domain)
# display output

print(message)
