# Created by Suraj Mandal
from .pipelines import pipeline
import wikipedia
import nltk

nlp = pipeline("question-generation")


def prepare():
    nltk.download("punkt")


def find_topic(topic: str = "Amber Heard"):
    return wikipedia.search(topic)


def generate_qa(wiki_title: str = "Depp v. Heard"):
    summary = wikipedia.summary(wiki_title, sentences=10, auto_suggest=False)
    summary = summary.replace("\n", "")

    json_result = nlp(summary)
    json_result = filter_length_answers(json_result)

    return json_result


def generate_custom_qa(input: str = ""):
    if input == "":
        return

    json_result = nlp(input)
    json_result = filter_length_answers(json_result)

    return json_result


# Filter out answers that are too long
def filter_length_answers(json_result):
    result = []
    for qa_pair in json_result:
        lenght_of_answer = len(qa_pair["answer"])
        if lenght_of_answer > 30:
            continue
        qa_pair["answer"] = qa_pair["answer"].capitalize()
        result.append(qa_pair)
    return result
