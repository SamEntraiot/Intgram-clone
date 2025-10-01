"""
Script to create test data for Instagram clone
Run with: python manage.py shell < create_test_data.py
"""

from django.contrib.auth.models import User
from accounts.models import Profile
from posts.models import Post, Comment
from django.core.files.base import ContentFile
import io
from PIL import Image

def create_test_image(color='blue', size=(600, 600)):
    """Create a simple colored image"""
    img = Image.new('RGB', size, color=color)
    img_io = io.BytesIO()
    img.save(img_io, format='JPEG')
    img_io.seek(0)
    return ContentFile(img_io.read(), name='test.jpg')

# Create test users
users_data = [
    {'username': 'john_doe', 'email': 'john@example.com', 'first_name': 'John', 'last_name': 'Doe'},
    {'username': 'jane_smith', 'email': 'jane@example.com', 'first_name': 'Jane', 'last_name': 'Smith'},
    {'username': 'bob_wilson', 'email': 'bob@example.com', 'first_name': 'Bob', 'last_name': 'Wilson'},
    {'username': 'alice_brown', 'email': 'alice@example.com', 'first_name': 'Alice', 'last_name': 'Brown'},
    {'username': 'charlie_davis', 'email': 'charlie@example.com', 'first_name': 'Charlie', 'last_name': 'Davis'},
]

print("Creating test users...")
created_users = []

for user_data in users_data:
    try:
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            defaults={
                'email': user_data['email'],
                'first_name': user_data['first_name'],
                'last_name': user_data['last_name'],
            }
        )
        if created:
            user.set_password('password123')
            user.save()
            print(f"✓ Created user: {user.username}")
        else:
            print(f"- User exists: {user.username}")
        created_users.append(user)
    except Exception as e:
        print(f"✗ Error creating {user_data['username']}: {e}")

# Update profiles
print("\nUpdating profiles...")
bios = [
    "Photographer 📷 | Travel enthusiast ✈️",
    "Food lover 🍕 | Coffee addict ☕",
    "Fitness coach 💪 | Health & wellness",
    "Artist 🎨 | Creating beautiful things",
    "Tech enthusiast 💻 | Code & coffee"
]

for i, user in enumerate(created_users):
    try:
        profile = user.profile
        profile.bio = bios[i]
        profile.website = f"https://{user.username}.example.com"
        profile.save()
        print(f"✓ Updated profile for {user.username}")
    except Exception as e:
        print(f"✗ Error updating profile for {user.username}: {e}")

# Create follow relationships
print("\nCreating follow relationships...")
try:
    # John follows everyone
    john = User.objects.get(username='john_doe')
    for user in created_users[1:]:
        john.profile.following.add(user.profile)
    print(f"✓ {john.username} now follows {len(created_users)-1} users")
    
    # Everyone follows John back
    for user in created_users[1:]:
        user.profile.following.add(john.profile)
    print(f"✓ {len(created_users)-1} users now follow {john.username}")
    
    # Jane and Alice follow each other
    jane = User.objects.get(username='jane_smith')
    alice = User.objects.get(username='alice_brown')
    jane.profile.following.add(alice.profile)
    alice.profile.following.add(jane.profile)
    print("✓ Created mutual follows between Jane and Alice")
except Exception as e:
    print(f"✗ Error creating follows: {e}")

# Create test posts
print("\nCreating test posts...")
colors = ['blue', 'red', 'green', 'purple', 'orange', 'pink', 'yellow', 'cyan']
captions = [
    "Beautiful day! ☀️ #nature #photography",
    "Loving this view! 🌄 #travel #adventure",
    "Coffee time ☕ #coffee #morning",
    "Sunset vibes 🌅 #sunset #beautiful",
    "Weekend mood! 🎉 #weekend #fun",
    "New artwork! 🎨 #art #creative",
    "Coding session 💻 #coding #developer",
    "Foodie life 🍕 #food #delicious",
]

posts_created = 0
for i, user in enumerate(created_users):
    try:
        # Create 2-3 posts per user
        num_posts = 2 if i % 2 == 0 else 3
        for j in range(num_posts):
            color_idx = (i * 3 + j) % len(colors)
            caption_idx = (i * 3 + j) % len(captions)
            
            post = Post.objects.create(
                author=user,
                image=create_test_image(color=colors[color_idx]),
                caption=captions[caption_idx]
            )
            posts_created += 1
        print(f"✓ Created {num_posts} posts for {user.username}")
    except Exception as e:
        print(f"✗ Error creating posts for {user.username}: {e}")

print(f"✓ Total posts created: {posts_created}")

# Add some likes
print("\nAdding likes to posts...")
try:
    all_posts = Post.objects.all()
    for post in all_posts[:10]:  # Like first 10 posts
        # Random users like the post
        for user in created_users[:3]:
            if user != post.author:
                post.likes.add(user)
    print(f"✓ Added likes to posts")
except Exception as e:
    print(f"✗ Error adding likes: {e}")

# Add some comments
print("\nAdding comments...")
comments = [
    "Great photo! 😍",
    "Love this! ❤️",
    "Amazing! 👏",
    "So beautiful! 🌟",
    "Awesome! 🔥",
]
try:
    all_posts = Post.objects.all()
    for i, post in enumerate(all_posts[:8]):  # Add comments to first 8 posts
        # 1-2 comments per post
        for j in range(2):
            commenter = created_users[(i + j + 1) % len(created_users)]
            if commenter != post.author:
                Comment.objects.create(
                    post=post,
                    author=commenter,
                    text=comments[(i + j) % len(comments)]
                )
    print(f"✓ Added comments to posts")
except Exception as e:
    print(f"✗ Error adding comments: {e}")

print("\n" + "="*50)
print("Test data creation complete!")
print("="*50)
print(f"\n✓ Created {len(created_users)} users")
print(f"✓ Created {posts_created} posts")
print(f"✓ Created follow relationships")
print(f"✓ Added likes and comments")
print("\nTest Accounts:")
print("-" * 50)
for user_data in users_data:
    print(f"Username: {user_data['username']}")
    print(f"Password: password123")
    print(f"Email: {user_data['email']}")
    print("-" * 50)
