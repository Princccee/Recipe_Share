from django.db import models
from django.contrib.auth import User

# Create your models here.

# This is a Django model that will be used to create a 
# database table to store recipe data.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    instruction = models.TextField()
    cooking_time = models.IntegerField(help_text="Time in min")

    difficulty = models.CharField(max_length=50, choices=[
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard')
    ])

    food_type = models.CharField(max_length=50, choices=[
        ('Vegetarian', 'Vegetarian'),
        ('Non-Vegetarian', 'Non-Vegetarian'),
        ('Vegan', 'Vegan')
    ], default='Vegetarian')  # Default value set to 'Vegetarian'

    image= models.ImageField(upload_to='recipes/')

    # Add a foreign key for recipe author from the 'User'
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    #  This method defines how a Recipe object is represented as a string.
    #  In this case, whenever a Recipe instance is printed or displayed (e.g., in the Django admin),
    #  it will show the title of the recipe.
    def __str__(self):
        return self.title
