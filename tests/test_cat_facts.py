from unittest.mock import Mock
from lib.cat_facts import CatFacts
'''
When we call CatFact
we should get a fact about cats back
'''

def test_cat_facts_returns_fact():
    requester_mock = Mock()
    cat_facts = CatFacts(requester_mock)
    requester_mock.get().json.return_value = {'fact':"The ancestor of all domestic cats is the African Wild Cat which still exists today."}
    assert cat_facts.provide() == "Cat fact: The ancestor of all domestic cats is the African Wild Cat which still exists today."