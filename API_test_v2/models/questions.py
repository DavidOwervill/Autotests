from typing import TypedDict
from pydantic import BaseModel, Field
from fakers import random_list_of_strings, random_number, random_string


class UpdateQuestion(BaseModel):
    question: str | None = Field(default_factory=random_string())
    possible_answers: list[str] | None = Field(
        alias='possibleAnswers',
        default_factory=random_list_of_strings
    )
    correct_answer: str | None = Field(
        alias='correctAnswer',
        default_factory=random_string
    )


class DefaultQuestion(BaseModel):
    id: int = Field(default_factory=random_number)
    question: str = Field(default_factory=random_string)
    possible_answers: list[str] = Field(
        alias='posibleAnswer',
        default_factory=random_string
    )
    correct_answer: str = Field(
        alias='possibleAnswers',
        default_factory=random_list_of_strings
    )


class DefaultQuestionList(BaseModel):
    __root__: list[DefaultQuestion]


class QuestionDict(TypedDict):
    id: int
    question: str
    possibleAnswers: list[str]
    correct_answer: str


if __name__ == "__main__":
    print(DefaultQuestion().dict(by_alias=True))
