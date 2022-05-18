import random

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from generalizing_core.serializers.challenge_serializer import ChallengeReadSerializer, ChallengeWriteSerializer

from generalizing_core.models.challenge import Challenge
from generalizing_core.models.lesson import Lesson
from generalizing_core.api.common.protocols import detail,list

@api_view(['GET', 'POST'])
def challenge_list(request):
    if request.method == 'GET':
        return list( request, Challenge, ChallengeReadSerializer, ChallengeWriteSerializer )

    elif request.method == 'POST':

        created_challenges = Challenge.objects.all()
        lesson_tuples = get_challenges_lesson_tuples( created_challenges )
        existing_lessons = Lesson.objects.all()
        lesson1, lesson2 = choose_lessons( existing_lessons, lesson_tuples )
        new_challenge = Challenge( lesson_1 = lesson1, lesson_2 = lesson2 )
        new_challenge.save()
        serializer = ChallengeReadSerializer(new_challenge)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def challenge_detail(request, uuid):
    return detail( request, uuid, Challenge, ChallengeWriteSerializer )


def get_challenges_lesson_tuples( challenges ):
    tuples = []
    for challenge in challenges:
        tuples.append( (challenge.lesson_1, challenge.lesson_2) )
    return tuples

def choose_lessons( lessons, tuples ):
    chosen = False
    l = len(lessons)
    while not chosen :
        rand1 = random.choice( range(0, l) )
        rand2 = random.choice( range(0, l) )
        if rand1 == rand2 :
            continue
        if (rand1, rand2) in tuples:
            continue
        chosen = True
    return lessons[rand1], lessons[rand2]