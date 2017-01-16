"""Your job is to write a speech for your CEO. You have a list of meaningful
phrases that he is fond of such as "knowledge optimization initiatives" and
your task is to weave them in to a speech.

You also have the opening words "Our clear strategic direction is to invoke..."
and some useful joining phrases such as "whilst not forgetting".

The speech that you will write takes the opening words and randomly jumbles the
phrases alternated with joining phrases to make a more complete, if meaningless,
speech. After execution the speech might need some light editing.

Note to my current employer: This is no reflection whatsoever on the
organisation that I work for. This all comes from one of my former CEOs,
Stephen Elop, during his tenure at Nokia. The code is mine but the words are
all his, slightly transliterated ("<big corp.>" replaces "Nokia",
"<little corp.>" replaces "Symbian" and "<other corp.>" replaces "Microsoft"). 

Created on 19 Feb 2016

@author: paulross
"""
import random
import textwrap

OPENING_WORDS = ['Our', 'clear', 'strategic', 'direction', 'is', 'to', 'invoke',]

PHRASE_TABLE = (
    ("accountable",         "transition",           "leadership"),
    ("driving",             "strategy",             "implementation"),
    ("drilling down into",  "active",               "core business objectives"),
    ("next billion",        "execution",            "with our friends in <other corp.>"),
    ("creating",            "next-generation",      "franchise platform"),
    ("<big corp.>'s",       "volume and",           "value leadership"),
    ("significant",         "end-user",             "experience"),
    ("transition",          "from <small corp.>",   "to <other corp.>'s platform"),
    ("integrating",         "shared",               "services"),
    ("empowered to",        "improve and expand",   "our portfolio of experience"),
    ("deliver",             "new",                  "innovation"),
    ("ramping up",          "diverse",              "collaboration"),
    ("next generation",     "mobile",               "ecosystem"),
    ("focus on",            "growth and",           "consumer delight"),
    ("management",          "planning",             "interlocks"),
    ("necessary",           "operative",            "capabilities"),
    ("knowledge",           "optimization",         "initiatives"), 
    ("modular",             "integration",          "environment"),
    ("software",            "creation",             "processes"),
    ("agile",               "working",              "practices"),
)

INSERTS = ('for', 'with', 'and', 'as well as', 'by',
           'whilst not forgetting',
           '. Of course',
           '. To be absolutely clear',
           '. We need',
           'and unrelenting',
           'with unstoppable',
)

def get_phrase():
    """Return a phrase by choosing words at random from each column of the PHRASE_TABLE."""
    # Your code goes here
    return "{0} {1} {2}".format(get_phrase_portion(0), get_phrase_portion(1), get_phrase_portion(2))

def get_phrase_portion(index):
    return PHRASE_TABLE[random.randint(0, len(PHRASE_TABLE)-1)][index]

def get_insert():
    """Return a randomly chosen set of words to insert between phrases."""
    # Your code goes here
    return INSERTS[random.randint(0, len(INSERTS)-1)]

def write_speech(n):
    """Write a speech with the opening words followed by n random phrases
    interspersed with random inserts."""
    print ' '.join(item for item in OPENING_WORDS)
    text='\r\n'.join(["{0}{1}".format(get_phrase(), get_insert() if i != n-1 else '') for i in range(0, n)]) +"."

    print textwrap.fill(text)

if __name__ == '__main__':
    write_speech(40)
