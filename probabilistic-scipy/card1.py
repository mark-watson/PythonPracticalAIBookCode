import scipy

def prob_pick_success(num_cards_in_deck,
                      num_cards_in_desired_selection_set,
                      num_cards_to_be_drawn):
    # Use the Probability Mass Function for hypergeometric discrete random variables:
    prob_card_not_drawn = scipy.stats.hypergeom.pmf(0,
                                                         num_cards_in_deck,
                                                         num_cards_in_desired_selection_set,
                                                         num_cards_to_be_drawn)
    return 1 - prob_card_not_drawn # which is the probability of a card being drawn

print("Probability of selecting a Heart, from a full 52 card deck:")
print(prob_pick_success(52,13,1))
print("Probability of selecting a Heart, from a 51 card deck where a Heart has already been picked:")
print(prob_pick_success(51,12,1))
