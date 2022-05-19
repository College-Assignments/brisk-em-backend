# Created by Suraj Mandal
from .pipelines import pipeline
import wikipedia
import nltk


def prepare():
    nltk.download('punkt')


def find_topic(topic: str = "Amber Heard"):
    return wikipedia.search(topic)


def generate_mcq(
    wiki_title: str = "Depp v. Heard"
):
    nlp = pipeline("question-generation")

    summary = wikipedia.summary(wiki_title)
    summary = summary.replace("\n", "")

    json_result = nlp(summary)

    def filter_length_answers(json_result):
        result = []
        for qa_pair in json_result:
            lenght_of_answer = len(qa_pair["answer"])
            if(lenght_of_answer > 30):
                continue
            result.append(qa_pair)
        return result

    json_result = filter_length_answers(json_result)

    # for idx, qa_pair in enumerate(json_result):
    #     print("Question " + str(idx + 1) + ":")
    #     print(qa_pair["question"] + "\n")
    #     print("Press Enter to see the answer\n")
    #     input()
    #     print("Answer: " + qa_pair["answer"] + "\n")
    #     print("---------------------------")

    return json_result
