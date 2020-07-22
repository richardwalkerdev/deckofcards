"""This module includes the logic to build a random deck of cards"""
# pylint: disable=C0200
import random
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CardSerializer


@api_view(['GET'])
def deck(request):
    """This function generates a random deck of cards as JSON"""
    class Card:
        """This creates a card class"""
        def __init__(self, suit, face, value):
            self.suit = suit
            self.face = face
            self.value = value

        def get_suit(self):
            """Getter for suit"""
            return self.suit

        def get_face(self):
            """Getter for face"""
            return self.face

        def get_value(self):
            """Getter for value"""
            return self.value

        def __str__(self):
            return self.__class__.__name__

    suits = ['spades',
             'hearts',
             'diamonds',
             'clubs']

    faces = ['ace',
             'two',
             'three',
             'four',
             'five',
             'six',
             'seven',
             'eight',
             'nine',
             'ten',
             'jack',
             'queen',
             'king']

    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    new_deck = []

    for suit in range(len(suits)):
        for face in range(len(faces)):
            card = Card(suits[suit], faces[face], values[face])
            new_deck.append(card)

    random.shuffle(new_deck)

    serializer = CardSerializer(new_deck, many=True)

    return Response(serializer.data)
