from django.db import models

# Create your models here.

class URL(models.Model):
    original_url = models.URLField(unique=True, help_text="The original long URL.")
    short_code = models.CharField(
        max_length=10,
        unique=True,
        blank=True,
        help_text="The unique code for the shortened URL."
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Generate a unique short code if it doesn't exist
        if not self.short_code:
            self.short_code = self.generate_unique_short_code()
        super().save(*args, **kwargs)

    def generate_unique_short_code(self):
        """Generates a unique short code."""
        max_attempts = 5
        for _ in range(max_attempts):
            code = generate_short_code()
            if not URL.objects.filter(short_code=code).exists():
                return code
        raise ValidationError("Failed to generate a unique short code after several attempts.")

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"
