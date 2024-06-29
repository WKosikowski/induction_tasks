#!/usr/bin/env python3
# Wojciech Kosikowski (c) 2024

from Quiz import Quiz, GeneralQuizGenerator

quizGenerator = GeneralQuizGenerator()
questions = quizGenerator.generateQuestions(10)

quiz = Quiz(questions)

quiz.start()