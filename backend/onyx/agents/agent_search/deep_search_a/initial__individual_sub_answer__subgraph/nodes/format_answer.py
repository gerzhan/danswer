from onyx.agents.agent_search.deep_search_a.initial__individual_sub_answer__subgraph.states import (
    AnswerQuestionOutput,
)
from onyx.agents.agent_search.deep_search_a.initial__individual_sub_answer__subgraph.states import (
    AnswerQuestionState,
)
from onyx.agents.agent_search.shared_graph_utils.models import (
    QuestionAnswerResults,
)


def format_answer(state: AnswerQuestionState) -> AnswerQuestionOutput:
    return AnswerQuestionOutput(
        answer_results=[
            QuestionAnswerResults(
                question=state.question,
                question_id=state.question_id,
                verified_high_quality=state.answer_quality,
                answer=state.answer,
                expanded_retrieval_results=state.expanded_retrieval_results,
                documents=state.documents,
                context_documents=state.context_documents,
                cited_docs=state.cited_docs,
                sub_question_retrieval_stats=state.sub_question_retrieval_stats,
            )
        ],
    )
