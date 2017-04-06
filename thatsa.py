
def get_noun_pool():
    """
    Load the list of words from nouns.txt and filter out any which are marked
    as previously used.
    If all words are marked as previously used, unmark all of them and return
    the entire list.
    """
    pass


def get_adjective_pool():
    """
    Load the list of words from adjectives.txt and filter out any which are
    marked as previously used.
    If all words are marked as previously used, unmark all of them and return
    the entire list.
    """
    pass


def mark_noun_used(word):
    """
    Update nouns.txt to reflect that `word` has been used.
    """
    pass


def mark_adjective_used(word):
    """
    Update adjective.txt to reflect that `word` has been used.
    """
    pass


def a_or_an(word):
    """
    Decide whether a word should be preceeded by "a" or "an". Uses the first
    letter to choose, but this can be overriden by adding "#a" or "#an" to
    the end of the word.
    """
    pass


def build_phrase():
    """
    Build a "that's a _____ _____" phrase by selecting a noun and an adjective
    from the pool.
    """
    pass


def post_tweet(text):
    """
    Post the given text as a tweet. Requires the following environment variables
    to be set, containing the API keys for a twitter application:
    - THATSA_CONSUMER_KEY
    - THATSA_CONSUMER_SECRET
    - THATSA_ACCESS_TOKEN_KEY
    - THATSA_ACCESS_TOKEN_SECRET
    """
    pass


if __name__ == '__main__':
    pass
