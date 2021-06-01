# This script takes a contact's HighLevel CRM data
# and converts the key-value pairs into a list
# which can then output the single custom value
# we need, the contact's Lead Origin List

# Example key-value pairs below from the webhook
input_data = {'customValue': 'Peyronies Disease,YouTubeAds,2021'}

# Splits the customValue's strings into a list
chunks = input_data['customValue'].split(',')

print(chunks)  # Tests output for developer of split strings
print(chunks[1])  # Tests output for developer for our desired list value

output = {'Lead Origin List': chunks[1]}
