from django.db import models


class SudokuGame(models.Model):
    puzzle_state = models.CharField(max_length=81)  # Store puzzle state as a string
    date_created = models.DateTimeField(auto_now_add=True)  # Automatically set when created

    # Add other fields as needed

    def __str__(self):
        return f"Sudoku Game {self.id}"
