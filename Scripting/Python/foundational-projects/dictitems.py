# Working with dictionaries
account_info = {
    "username": "tlannister",
    "password": "hearmeroar1!",
    "email": "tywin@casterlyrock.com",
    "department": "GRC",
}
print(account_info)

# Add job title/role to the dictionary using update
account_info.update({"job title": "Senior Analyst"})
# Display content
print(account_info)
print(account_info["job title"])

# Use len() to return and display the number of key values
print(len(account_info))

# Use .keys() to return the entire list of items
print(account_info.keys())

# Use .items() to return the entire list of items
print(account_info.items())

# For loop to display key and values
for key,value in account_info.items():
    print(key,value)
