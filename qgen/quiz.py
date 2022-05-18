# -*- coding: utf-8 -*-
import json
from pipelines import pipeline
import wikipedia
import nltk
nltk.download('punkt')

nlp = pipeline("question-generation")

TOPIC = "Amber Heard"
wikipedia.search(TOPIC)

SELECTED_TOPIC = "Depp v. Heard"
summary = wikipedia.summary(SELECTED_TOPIC)
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

print(json.dumps(json_result, indent=1))

# for idx, qa_pair in enumerate(json_result):
#     print("Question " + str(idx + 1) + ":")
#     print(qa_pair["question"] + "\n")
#     print("Press Enter to see the answer\n")
#     input()
#     print("Answer: " + qa_pair["answer"] + "\n")
#     print("---------------------------")
