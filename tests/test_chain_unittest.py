"""
We will try to write a test script for testing our `agent/chain`
"""
import pytest
import unittest.mock as mock
import langchain_service.chain as chain
from langchain_core.messages.ai import AIMessage
from langchain_openai import ChatOpenAI

# @pytest.fixture(scope="module")
# def answer(mocker):
#     # ans = chain.invoke(input={"text":"Hello mam"})
#     ans = AIMessage("asdasd")
#     return ans

class TestChain:
    # We say, if this function is called, just don't call.
    # And return this message instead.
    @mock.patch.object(ChatOpenAI, "invoke", return_value=AIMessage("This is the message"))
    def test_chain_answer_type_AIMessage(self, mock_answer):
        # Calling the function like normal
        answer = chain.invoke(input={"text":"Hello mam"})

        assert isinstance(answer, AIMessage), f"Expect type of response as {type(AIMessage)}, got {type(answer)}"

    @mock.patch.object(ChatOpenAI, "invoke", return_value=AIMessage("This is the message"))
    def test_chain_answer_content_is_string(self, mock_answer):
        answer = chain.invoke(input={"text":"Hello mam"})
        content = answer.content
        assert isinstance(content, str), f"Expect type of response as {type(str)}, got {type(content)}"