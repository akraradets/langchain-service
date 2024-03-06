"""
We will try to write a test script for testing our `agent/chain`
"""
import pytest
import langchain_service.chain as chain
from langchain_core.messages.ai import AIMessage

@pytest.fixture(scope="module")
def answer():
    ans = chain.invoke(input={"text":"Hello mam"})
    return ans

class TestChain:
    def test_chain_answer_type_AIMessage(self, answer):
        assert isinstance(answer, AIMessage), f"Expect type of response as {type(AIMessage)}, got {type(answer)}"

    def test_chain_answer_content_is_string(self, answer):
        content = answer.content
        assert isinstance(content, str), f"Expect type of response as {type(str)}, got {type(content)}"