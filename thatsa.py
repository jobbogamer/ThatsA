
import twitter
import argparse
import os


FILENAME_NOUNS      = 'nouns.txt'
FILENAME_ADJECTIVES = 'adjectives.txt'


def get_word_pool(filename):
    """
    Load the list of words from the given file and filter out any which are
    marked as previously used.
    If all words are marked as previously used, unmark all of them and return
    the entire list.
    """
    with open(filename) as f:
        words = f.readlines()

    # Filter out those which are marked, i.e. they start with !.
    filtered_words = [word.strip().lower() for word in words if not word.startswith('!')]

    # If there are no unmarked words left, unmark them all and return the
    # entire list.
    if len(filtered_words) == 0:
        unmark_words(filename)
        return get_word_pool(filename)

    return filtered_words


def mark_word_used(word, filename):
    """
    Update the given file to reflect that `word` has been used, by prefixing
    it with a !.
    """
    with open(filename) as f:
        words = f.readlines()

    with open(filename, 'w') as f:
        new_words = ['!' + w if w.strip().lower() == word else w for w in words]
        f.writelines(new_words)


def unmark_words(filename):
    """
    Update the given file to remove all ! prefixes.
    """
    with open(filename) as f:
        words = f.readlines()

    with open(filename, 'w') as f:
        new_words = [word[1:] if word.startswith('!') else word for word in words]
        f.writelines(new_words)


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
    noun_pool = get_word_pool(FILENAME_NOUNS)
    print len(noun_pool)


def post_tweet(text):
    """
    Post the given text as a tweet. Requires the following environment variables
    to be set, containing the API keys for a twitter application:
    - THATSA_CONSUMER_KEY
    - THATSA_CONSUMER_SECRET
    - THATSA_ACCESS_TOKEN_KEY
    - THATSA_ACCESS_TOKEN_SECRET
    """
    keys = {
        'consumer_key':        os.getenv('THATSA_CONSUMER_KEY', None),
        'consumer_secret':     os.getenv('THATSA_CONSUMER_SECRET', None),
        'access_token_key':    os.getenv('THATSA_ACCESS_TOKEN_KEY', None),
        'access_token_secret': os.getenv('THATSA_ACCESS_TOKEN_SECRET', None)
    }

    # If any of the environment variables couldn't be found, give up here.
    for item in keys:
        if keys[item] is None:
            print 'Missing environment variable: {}'.format(item)
            return

    api = twitter.Api(**keys)
    api.PostUpdate("test post, please ignore")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--print', action='store_true', dest='to_console',
                        help='print the phrase to the console instead of tweeting')
    args = parser.parse_args()

    # Get the phrase...
    phrase = build_phrase()

    # ...and either print it...
    if args.to_console:
        print phrase

    # ... or tweet it.
    else:
        post_tweet(phrase)


