import random
import json

# Define sample attributes
majors = ["CS", "Math", "Physics", "Chemistry", "Biology", "Engineering", "Economics", "History"]
years = ["Freshman", "Sophomore", "Junior", "Senior"]
groups = ['Howls', 'Magic Tree House','Lost In the Woods','First Seed','RagTag','La Familia']

# Generate a sample dataset of 80 users
def generate_sample_users(num_users):
    users = []
    for i in range(num_users):
        user = {
            "Name": f"User_{i+1}",
            "Major": random.choice(majors),
            "Year": random.choice(years),
            "Group": random.choice(groups)
        }
        users.append(user)
    return users

# Generate 80 sample users
sample_users = generate_sample_users(80)

# Save the generated users to a JSON file
file_path = 'sample_users.json'
with open(file_path, 'w') as file:
    json.dump(sample_users, file, indent=4)

print(f"Sample users have been saved to {file_path}.")
