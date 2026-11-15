from chathub.models import ChatMessage
from chathub.stats import count_by_author, top_words


def make(*pairs):
    return [ChatMessage(author, text) for author, text in pairs]


def test_top_words_ignores_case_and_punctuation():
    msgs = make(("a", "Hello hello world!"), ("b", "hello, WORLD."), ("c", "bye"))
    assert top_words(msgs, 2) == [("hello", 3), ("world", 2)]


def test_top_words_default_n_is_5():
    msgs = make(("a", "a b c d e f g"))
    assert len(top_words(msgs)) == 5


def test_top_words_empty():
    assert top_words([]) == []


def test_count_by_author():
    msgs = make(("vedal", "x"), ("neuro", "y"), ("vedal", "z"))
    assert count_by_author(msgs) == {"vedal": 2, "neuro": 1}
