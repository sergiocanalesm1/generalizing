from django.db import models

class Origin(models.TextChoices):
    PERSONAL_EXPERIENCE = 'Personal Experience'
    BOOK = 'Book'
    LECTURE = 'Lecture'
    FILM = 'Film'
    THEATER_PLAY = 'Theater Play'
    VIDEO = 'Video'
    VIDEO_GAME = 'Video Game'
    SONG = 'Song'
    ARTICLE = 'Article'
    RELATION = 'Relation'
    LESSON = 'Lesson'
    INTERPRETATION = 'Interpretation'
    OTHER= 'Other'
