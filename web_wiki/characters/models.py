from django.db import models

class Character(models.Model):
    """Base model for both Player and Non-Player Characters"""
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=50)
    alignment = models.CharField(max_length=50)
    backstory = models.TextField(blank=True)
    campaign = models.ForeignKey('campaigns.Campaign', on_delete=models.CASCADE, related_name="characters")

    def __str__(self):
        return self.name

class PlayerCharacter(Character):
    """Model for Player Characters (PCs), with an associated character sheet PDF"""
    character_class = models.CharField(max_length=50)
    player_name = models.CharField(max_length=100)
    #portrait = models.ImageField(default='placeholder_image.png', blank=True)
    character_sheet = models.FileField(upload_to='character_sheets/', blank=True, null=True)  # PDF upload

class NonPlayerCharacter(Character):
    """Model for Non-Player Characters (NPCs), no extra fields needed"""
    role = models.CharField(
        max_length=50, 
        choices=[('ALLY', 'Ally'), ('ENEMY', 'Enemy'), ('NEUTRAL', 'Neutral'), ('OTHER', 'Other')],
        default='NEUTRAL'
    )

