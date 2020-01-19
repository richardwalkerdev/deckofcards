from rest_framework.response import Response
from rest_framework.decorators import api_view
import random
from .serializers import CardSerializer
from rest_framework.renderers import JSONRenderer


@api_view(['GET'])
def deck(request):

    class Card():
        def __init__(self, suit, face, value):
            self.suit = suit
            self.face = face
            self.value = value

    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    faces = ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']
    values = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    deck = []

    for suit in range(len(suits)):
        for n in range(len(faces)):
            card = Card(suits[suit], faces[n], values[n])
            deck.append(card)

    random.shuffle(deck)

    serializer = CardSerializer(deck, many=True)

    return Response(serializer.data)