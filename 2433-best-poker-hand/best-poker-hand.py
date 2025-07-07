class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        ranks=Counter(ranks)
        suits=Counter(suits)

        if max(suits.values())>=5:
            return "Flush"
        elif max(ranks.values())>=3:
            return "Three of a Kind"
        elif max(ranks.values())==2:
            return "Pair"
        else:
            return "High Card"
        