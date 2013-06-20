from nose.tools import *
from ex48.parser import *

def test_sentence():
    phrase = Sentence(('noun', 'princess'),('verb', 'go'), ('direction', 'north'))
    assert_equal(phrase, phrase) 

def test_subject():
    princess = Sentence(('noun','princess'),('verb','go'),('directiona','north'))
    assert_equal(princess.subject, 'princess')

def test_verb():
    go = Sentence(('noun','princess'),('verb','go'),('direction','north'))
    assert_equal(go.verb, 'go')

def test_object():
    north = Sentence(('noun','princess'),('verb','go'),('direction','north'))
    assert_equal(north.object, 'north')

def test_peek():
    noun_tuple = ('noun', 'princess')
    verb_tuple = ('verb', 'go')
    object_tuple = ('object', 'north')
    no_sentence = ('something', 'here')

    assert_equal(peek([noun_tuple]),'noun')
    assert_equal(peek([verb_tuple]),'verb')
    assert_equal(peek([object_tuple]),'object')
    assert_equal(peek(''), None)

def test_match():
    phrase = [('noun', 'princess')]
    assert_equal(match(phrase, 'noun'), ('noun', 'princess'))
    assert_equal(match(phrase, 'getting_none'), None)

def test_skip():
    phrase = [('stop', 'the')]
    assert_equal(skip(phrase, 'stop'), None)

def test_parse_verb():
    phrase = [('verb', 'go')]
    assert_equal(parse_verb(phrase), ('verb', 'go'))
    exception_phrase = [('noun', 'princess')]
    assert_raises(ParserError, parse_verb, exception_phrase)

def test_parse_object():
    phrase =  [('noun', 'princess')]
    assert_equal(parse_object(phrase), ('noun', 'princess'))
    direction_phrase = [('direction', 'north')]
    assert_equal(parse_object(direction_phrase), ('direction', 'north'))
    verb_phrase = [('verb', 'go')]
    assert_raises(ParserError, parse_object, verb_phrase)

def test_parse_subject():
    word_list = [('verb', 'go'), ('direction', 'north')]
    subj = ('noun', 'princess')
    assert_equal(parse_subject(word_list, subj),Sentence(('noun', 'princess'),('verb', 'go'), ('direction', 'north')))

def test_parse_sentence():
    word_list = [('verb', 'go'), ('direction', 'north')]
    assert_equal(parse_sentence(word_list), Sentence(('noun', 'player'),('verb', 'go'), ('direction', 'north')))
    noun_word_list = [('noun', 'player'), ('verb', 'go'), ('direction', 'north')]
    assert_equal(parse_sentence(noun_word_list), Sentence(('noun', 'player'),('verb', 'go'), ('direction', 'north')))
    exception_word_list = [('adjetive', 'fancy')]
    assert_raises(ParserError, parse_sentence, exception_word_list)






