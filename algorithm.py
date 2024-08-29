import random
import json
import runpy

# Generate 80 random users (Specified in file)
runpy.run_path('randomUserGenerator.py')

# Read the generated data from the file
with open('sample_users.json', 'r') as file:
    users = json.load(file)

# Initialize a set to track user pairs that have been together
past_groupings = set()

def have_been_together(user1, user2):
    '''Check if two users have been in the same group before.'''
    pair = frozenset([user1['Name'], user2['Name']])
    return pair in past_groupings

def add_grouping(group):
    '''Add all pairs from the current group to past groupings.'''
    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            past_groupings.add(frozenset([group[i]['Name'], group[j]['Name']]))

def calculate_diversity(user1, user2):
    '''Calculate diversity score between two users based on differences in all keys'''
    diversity_score = 0

    # Check if users have been grouped together before
    if have_been_together(user1, user2):
        diversity_score = -1000
        return diversity_score

    # Calculate diversity based on differences in all keys
    for key in user1:
        if user1[key] != user2[key]:
            diversity_score += 1

    return diversity_score

def group_diversity(group):
    score = 0
    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            score += calculate_diversity(group[i], group[j])
    return score

def form_diverse_groups(users, group_size):
    if group_size < 1:
        raise ValueError("Group size must be at least 1.")
    
    remaining_users = users[:]
    diverse_groups = []
    ungrouped_members = []

    while len(remaining_users) >= group_size:
        best_group = None
        best_score = -1
        
        # Try to form a diverse group
        for _ in range(100):  # Try 100 random samples
            if len(remaining_users) < group_size:
                break
            sample = random.sample(remaining_users, group_size)
            score = group_diversity(sample)
            if score > best_score:
                best_score = score
                best_group = sample
        
        if best_group:
            diverse_groups.append(best_group)
            add_grouping(best_group)
            remaining_users = [u for u in remaining_users if u not in best_group]
        else:
            break
    
    ungrouped_members = remaining_users

    return diverse_groups, ungrouped_members

# Use Case
group_size = 3  # Can be 3 or 4 or larger
diverse_groups, ungrouped_members = form_diverse_groups(users, group_size)

# Print groups
for i, group in enumerate(diverse_groups):
    print(f"Group {i + 1}: {[user['Name'] for user in group]}")

# Print remaining ungrouped members
print("Ungrouped Members:", [user['Name'] for user in ungrouped_members])
