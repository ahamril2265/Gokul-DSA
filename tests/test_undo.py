import pytest
from src.undo_editor import TextEditor


def test_append_and_undo():
    e = TextEditor()
    e.append("hello")
    assert e.get_text() == "hello"
    assert e.undo() is True
    assert e.get_text() == ""


def test_delete_and_undo():
    e = TextEditor()
    e.append("hello")
    deleted = e.delete(2)
    assert deleted == "lo"
    assert e.get_text() == "hel"
    assert e.undo() is True
    assert e.get_text() == "hello"


def test_multiple_undos():
    e = TextEditor()
    e.append("a")
    e.append("b")
    e.append("c")
    assert e.get_text() == "abc"
    e.delete(1)  # removes 'c'
    assert e.get_text() == "ab"
    # undo delete -> restores 'c'
    assert e.undo() is True
    assert e.get_text() == "abc"
    # undo last append (which was 'c') -> removes it
    assert e.undo() is True
    assert e.get_text() == "ab"
    # another undo -> removes 'b'
    assert e.undo() is True
    assert e.get_text() == "a"


def test_undo_empty_stack():
    e = TextEditor()
    assert e.get_text() == ""
    assert e.undo() is False
