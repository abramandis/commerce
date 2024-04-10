from django.contrib.auth.models import AbstractUser
from django.db import models


CATEGORY_CHOICES = (
        ('option1', 'TOYS'),
        ('option2', 'FASHION'),
        ('option3', 'FURNITURE'),
        ('option4', 'ELECTRONICS'),
        ('option5', 'OTHER'),
    )

class User(AbstractUser):
    watchlist = models.ManyToManyField('Listing', blank=True, related_name='watchers')
    pass


class Listing(models.Model):
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=100)
    image_url = models.URLField(blank=True )
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2, default = 5.00)
    highest_bid = models.ForeignKey('Bid', on_delete=models.SET_NULL, null=True, blank=True, related_name='winning_bid')
    description = models.TextField()
    category = models.CharField(max_length=100, blank = True, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_open = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Listing by {self.created_by.username}: {self.description}"
    
    pass

class Bid(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bids')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bid by {self.created_by.username} on {self.listing}"
    
    pass

class Comment(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {created_by.user.username} on {self.listing}"

    pass
