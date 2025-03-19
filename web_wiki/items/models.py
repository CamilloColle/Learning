from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50)
    rarity = models.CharField(
        max_length=50, 
        choices=[('COMMON', 'Common'), ('UNCOMMON', 'Uncommon'), 
                 ('RARE', 'Rare'), ('EPIC', 'Epic'),
                 ('LEGENDARY', 'Legendary'), ('ARTIFACT', 'Artifact'),
                 ('VARIES', 'Varies')],
        blank=True
    )
    is_magic = models.BooleanField()
    requires_attunement  = models.BooleanField()
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

