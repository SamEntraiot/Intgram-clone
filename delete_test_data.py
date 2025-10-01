"""
Script to delete test data from Instagram clone
Run with: python manage.py shell < delete_test_data.py
"""

from django.contrib.auth.models import User
from posts.models import Post, Comment
from accounts.models import Profile, Notification, Conversation, Message

print("=" * 50)
print("Deleting test data...")
print("=" * 50)

# Test usernames to delete
test_usernames = [
    'john_doe',
    'jane_smith', 
    'bob_wilson',
    'alice_brown',
    'charlie_davis'
]

print(f"\nDeleting test users: {', '.join(test_usernames)}")

# Delete users (this will cascade delete their posts, comments, etc.)
deleted_count = 0
for username in test_usernames:
    try:
        user = User.objects.get(username=username)
        user.delete()
        deleted_count += 1
        print(f"✓ Deleted user: {username}")
    except User.DoesNotExist:
        print(f"✗ User not found: {username}")

print(f"\n✓ Deleted {deleted_count} test users")
print(f"✓ All related posts, comments, and relationships removed")

# Optional: Clean up orphaned data
orphaned_posts = Post.objects.filter(author__isnull=True).count()
orphaned_comments = Comment.objects.filter(author__isnull=True).count()

if orphaned_posts > 0:
    Post.objects.filter(author__isnull=True).delete()
    print(f"✓ Cleaned up {orphaned_posts} orphaned posts")

if orphaned_comments > 0:
    Comment.objects.filter(author__isnull=True).delete()
    print(f"✓ Cleaned up {orphaned_comments} orphaned comments")

print("\n" + "=" * 50)
print("Test data deletion complete!")
print("=" * 50)
