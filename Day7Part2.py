import re
import os
import sys
from enum import Enum

class HandType(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0

class CardType(Enum):
    ACE = 13
    KING = 12
    QUEEN = 11
    JACK = 0
    TEN = 9
    NINE = 8
    EIGHT = 7
    SEVEN = 6
    SIX = 5
    FIVE = 4
    FOUR = 3
    THREE = 2
    TWO = 1
    

class Hand():
    def __init__(self, cards, bid) -> None:
        self.cards = self.determineCardTypes(cards)
        self.bid = int(bid)
        self.handType = self.figureOutHandType()

    def determineCardTypes(self, strCards) -> [CardType]:
        cards = []
        for strCard in strCards:
            if strCard == "A":
                cards.append(CardType.ACE)
                continue
            if strCard == "K":
                cards.append(CardType.KING)
                continue
            if strCard == "Q":
                cards.append(CardType.QUEEN)
                continue
            if strCard == "J":
                cards.append(CardType.JACK)
                continue
            if strCard == "T":
                cards.append(CardType.TEN)
                continue
            if strCard == "9":
                cards.append(CardType.NINE)
                continue
            if strCard == "8":
                cards.append(CardType.EIGHT)
                continue
            if strCard == "7":
                cards.append(CardType.SEVEN)
                continue
            if strCard == "6":
                cards.append(CardType.SIX)
                continue
            if strCard == "5":
                cards.append(CardType.FIVE)
                continue
            if strCard == "4":
                cards.append(CardType.FOUR)
                continue
            if strCard == "3":
                cards.append(CardType.THREE)
                continue
            if strCard == "2":
                cards.append(CardType.TWO)
                continue
        return cards


    def figureOutHandType(self) -> HandType:
        sameNumbers = []
        jacks = []
        for card in self.cards:
            foundSameNumber = False
            if card == CardType.JACK:
                jacks.append(card)
                continue
            for j, arr in enumerate(sameNumbers):
                if card == arr[0]:
                    sameNumbers[j].append(card)
                    foundSameNumber = True
            if foundSameNumber == False:
                sameNumbers.append([card])
        
        numPairs = 0
        for numbers in sameNumbers:
            if len(numbers) == 5:
                return HandType.FIVE_OF_A_KIND
            if len(numbers) == 4:
                if len(jacks) == 1:
                    return HandType.FIVE_OF_A_KIND
                return HandType.FOUR_OF_A_KIND
            if len(numbers) > 1:
                numPairs += 1

        if numPairs == 2:
            if (len(sameNumbers[0]) == 3 and len(sameNumbers[1]) == 2) or (len(sameNumbers[1]) == 3 and len(sameNumbers[0]) == 2):
                return HandType.FULL_HOUSE
            if len(jacks) == 1:
                return HandType.FULL_HOUSE
            return HandType.TWO_PAIR
        
        if numPairs == 1:
            for numbers in sameNumbers:
                if len(numbers) == 3:
                    if len(jacks) == 2:
                        return HandType.FIVE_OF_A_KIND
                    if len(jacks) == 1:
                        return HandType.FOUR_OF_A_KIND
                    return HandType.THREE_OF_A_KIND
            if len(jacks) == 3:
                return HandType.FIVE_OF_A_KIND
            if len(jacks) == 2:
                return HandType.FOUR_OF_A_KIND
            if len(jacks) == 1:
                return HandType.THREE_OF_A_KIND
            return HandType.ONE_PAIR

        if len(jacks) == 5:
            return HandType.FIVE_OF_A_KIND
        if len(jacks) == 4:
            return HandType.FIVE_OF_A_KIND
        if len(jacks) == 3:
            return HandType.FOUR_OF_A_KIND
        if len(jacks) == 2:
            return HandType.THREE_OF_A_KIND
        if len(jacks) == 1:
            return HandType.ONE_PAIR
        return HandType.HIGH_CARD


def part1():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    pattern = r"^(.+) (\d+)$"
    handsInput = re.findall(pattern, contents, re.M)

    hands = []
    for cards, bid in handsInput:
        handInQuestion = Hand(cards, bid)
        addedHand = False

        for j, hand in enumerate(hands):
            if handInQuestion.handType.value < hand.handType.value:
                hands.insert(j, handInQuestion)
                addedHand = True
                break
            if handInQuestion.handType.value == hand.handType.value:
                for k, card in enumerate(hand.cards):
                    if handInQuestion.cards[k].value < card.value:
                        hands.insert(j, handInQuestion)
                        addedHand = True
                        break
                    if handInQuestion.cards[k].value > card.value:
                        break
                if addedHand:
                    break
        if addedHand == False:
            hands.append(handInQuestion)
        
    # Use for debugging
    # for hand in hands:
    #     print(hand.handType.name, end=" -> ")
    #     for card in hand.cards:
    #         print(card.name, end=" ")
    #     print()
    
    totalWinnings = 0
    for i, hand in enumerate(hands):
        totalWinnings += (hand.bid * (i+1))
            
    return totalWinnings

print(part1())