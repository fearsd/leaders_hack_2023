// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-nocheck

import {Survey} from "../../types/interfaces.ts";
import React, {useState} from 'react';
import {Button, Checkbox, Col, Radio, Row} from 'antd';
import {useNavigate} from "react-router-dom";

const SurveyPage: React.FC<Survey> = () => {
    const navigate = useNavigate();
    //const survey = API.getPoll();
    // survey = API.getPoll();
    // const questions = survey.questions;
    // const id = survey.id;
    const questions = q.questions;
    const [currentQuestion, setCurrentQuestion] = useState(0);
    const [answers, setAnswers] = useState<{ question_id: number; option_ids: number[] }[]>([]);
    const id = q.id;
    const handleCheckboxChange = (questionId: number, optionId: number) => {
        setAnswers((prevAnswers) => {
            const existingAnswerIndex = prevAnswers.findIndex((answer) => answer.question_id === questionId);
            if (existingAnswerIndex !== -1) {
                const existingOptionIds = prevAnswers[existingAnswerIndex].option_ids;
                const updatedOptionIds = existingOptionIds.includes(optionId)
                    ? existingOptionIds.filter((id) => id !== optionId)
                    : [...existingOptionIds, optionId];
                return [
                    ...prevAnswers.slice(0, existingAnswerIndex),
                    {question_id: questionId, option_ids: updatedOptionIds},
                    ...prevAnswers.slice(existingAnswerIndex + 1),
                ];
            } else {
                return [...prevAnswers, {question_id: questionId, option_ids: [optionId]}];
            }
        });
    };

    const handleRadioChange = (questionId: number, optionId: number) => {
        setAnswers((prevAnswers) => [
            ...prevAnswers.filter((answer) => answer.question_id !== questionId),
            {question_id: questionId, option_ids: [optionId]},
        ]);
    };

    const handleNext = () => {
        setCurrentQuestion((prevQuestion) => prevQuestion + 1);
    };

    const handleSubmit = () => {
        const payload = {
            poll_id: id,
            answers: answers.map((answer) => ({
                question_id: answer.question_id,
                options: answer.option_ids,
            })),
        };
        console.log(payload);
        navigate("/home");
        // Отправка payload на сервер или выполнение другой логики
    };

    const question = questions[currentQuestion];

    return (
        <>
            <h3>{question.text}</h3>
            {question.question_type === 'Check' && (
                <Checkbox.Group>
                    <Row>
                        {question.options.map((option) => (
                            <Col span={12} key={option.id}>
                                <Checkbox
                                    checked={answers.some((answer) => answer.question_id === question.id && answer.option_ids.includes(option.id))}
                                    onChange={() => handleCheckboxChange(question.id, option.id)}
                                >
                                    {option.text}
                                </Checkbox>
                            </Col>
                        ))}
                    </Row>
                </Checkbox.Group>
            )}
            {question.question_type === 'Radio' && (
                <Radio.Group>
                    {question.options.map((option) => (
                        <Radio
                            key={option.id}
                            checked={answers.some((answer) => answer.question_id === question.id && answer.option_ids.includes(option.id))}
                            onChange={() => handleRadioChange(question.id, option.id)}
                        >
                            {option.text}
                        </Radio>
                    ))}
                </Radio.Group>
            )}
            <div style={{marginTop: '1rem'}}>
                {currentQuestion > 0 && (
                    <Button style={{marginRight: '1rem'}}
                            onClick={() => setCurrentQuestion((prevQuestion) => prevQuestion - 1)}>
                        Назад
                    </Button>
                )}
                {currentQuestion < questions.length - 1 ? (
                    <Button type="primary" onClick={handleNext}>
                        Далее
                    </Button>
                ) : (
                    <Button type="primary" onClick={handleSubmit}>
                        Отправить
                    </Button>
                )}
            </div>
        </>
    );
};


const q = {
    "datetime_created": "2023-05-28T16:53:13.801024+00:00",
    "id": 1,
    "questions": [
        {
            "question_type": "Check",
            "text": "Пол",
            "slug": "#1",
            "num": 1,
            "id": 1,
            "options": [
                {
                    "id": 31,
                    "question_id": 1,
                    "slug": "male",
                    "text": "Мужской"
                },
                {
                    "id": 32,
                    "question_id": 1,
                    "slug": "female",
                    "text": "Женский"
                }
            ]
        },
        {
            "question_type": "Check",
            "text": "Ваш возраст",
            "slug": "#2",
            "num": 2,
            "id": 2,
            "options": [
                {
                    "id": 33,
                    "question_id": 2,
                    "slug": "<60",
                    "text": "Младше 60 лет"
                },
                {
                    "id": 34,
                    "question_id": 2,
                    "slug": ">=60,<=70",
                    "text": "60-70 лет"
                },
                {
                    "id": 35,
                    "question_id": 2,
                    "slug": ">=71,<=80",
                    "text": "71-80 лет"
                },
                {
                    "id": 36,
                    "question_id": 2,
                    "slug": ">80",
                    "text": "Старше 80 лет"
                }
            ]
        },
        {
            "question_type": "Multi",
            "text": "Какие занятия Вам нравятся сейчас больше всего?",
            "slug": "#3",
            "num": 3,
            "id": 3,
            "options": [
                {
                    "id": 37,
                    "question_id": 3,
                    "slug": "competition",
                    "text": "Соревнования"
                },
                {
                    "id": 38,
                    "question_id": 3,
                    "slug": "lectures",
                    "text": "Лекции и обучение"
                },
                {
                    "id": 39,
                    "question_id": 3,
                    "slug": "travel",
                    "text": "Путешествия"
                },
                {
                    "id": 40,
                    "question_id": 3,
                    "slug": "walking",
                    "text": "Активные прогулки"
                },
                {
                    "id": 41,
                    "question_id": 3,
                    "slug": "gardening",
                    "text": "Садоводство и огородничество"
                }
            ]
        },
        {
            "question_type": "Check",
            "text": "В каком формате Вы предпочитаете заниматься?",
            "slug": "#4",
            "num": 4,
            "id": 4,
            "options": [
                {
                    "id": 42,
                    "question_id": 4,
                    "slug": "online",
                    "text": "Онлайн (через интернет)"
                },
                {
                    "id": 43,
                    "question_id": 4,
                    "slug": "offline",
                    "text": "Вживую (в группе или индивидуально)"
                }
            ]
        },
        {
            "question_type": "Multi",
            "text": "Какие навыки или интересы Вы бы хотели развивать или изучать?",
            "slug": "#5",
            "num": 5,
            "id": 5,
            "options": [
                {
                    "id": 44,
                    "question_id": 5,
                    "slug": "languages",
                    "text": "Изучение новых языков"
                },
                {
                    "id": 45,
                    "question_id": 5,
                    "slug": "drawing",
                    "text": "Рисование или живопись"
                },
                {
                    "id": 46,
                    "question_id": 5,
                    "slug": "music",
                    "text": "Музыка (игра на инструменте, пение)"
                },
                {
                    "id": 47,
                    "question_id": 5,
                    "slug": "cooking",
                    "text": "Кулинария"
                },
                {
                    "id": 48,
                    "question_id": 5,
                    "slug": "needlework",
                    "text": "Рукоделие (вязание, шитье и т.д.)"
                }
            ]
        },
        {
            "question_type": "Check",
            "text": "Занимаетесь ли Вы физическими упражнениями?",
            "slug": "#6",
            "num": 6,
            "id": 6,
            "options": [
                {
                    "id": 49,
                    "question_id": 6,
                    "slug": "yes",
                    "text": "Да"
                },
                {
                    "id": 50,
                    "question_id": 6,
                    "slug": "no",
                    "text": "Нет"
                }
            ]
        },
        {
            "question_type": "Check",
            "text": "Какую категорию интеллектуальных игр Вы считаете наиболее привлекательной и интересной для себя?",
            "slug": "#7",
            "num": 7,
            "id": 7,
            "options": [
                {
                    "id": 51,
                    "question_id": 7,
                    "slug": "offline_games",
                    "text": "Интеллектуальные игры (включая настольные игры и шахматы/шашки)"
                },
                {
                    "id": 52,
                    "question_id": 7,
                    "slug": "online_games",
                    "text": "Онлайн интеллектуальные игры"
                }
            ]
        },
        {
            "question_type": "Check",
            "text": "Какую категорию занятий Вы считаете наиболее привлекательной и интересной для себя в области образования и саморазвития?",
            "slug": "#8",
            "num": 8,
            "id": 8,
            "options": [
                {
                    "id": 53,
                    "question_id": 8,
                    "slug": "healthy",
                    "text": "Здорово жить (включая образовательный практикум, пеший лекторий, психологию и коммуникации, финансовую и правовую грамотность, личную безопасность, экологию жизни)"
                },
                {
                    "id": 54,
                    "question_id": 8,
                    "slug": "history",
                    "text": "История, искусство, краеведение"
                },
                {
                    "id": 55,
                    "question_id": 8,
                    "slug": "languages",
                    "text": "Иностранные языки"
                },
                {
                    "id": 56,
                    "question_id": 8,
                    "slug": "it",
                    "text": "Информационные технологии"
                }
            ]
        },
        {
            "question_type": "Check",
            "text": " Какую категорию занятий Вы считаете наиболее привлекательной и интересной для себя в области творчества и активного образа жизни?",
            "slug": "#9",
            "num": 9,
            "id": 9,
            "options": [
                {
                    "id": 57,
                    "question_id": 9,
                    "slug": "drawing",
                    "text": "Рисование"
                },
                {
                    "id": 58,
                    "question_id": 9,
                    "slug": "vocal",
                    "text": "Пение"
                },
                {
                    "id": 59,
                    "question_id": 9,
                    "slug": "dancing",
                    "text": "Танцы"
                },
                {
                    "id": 60,
                    "question_id": 9,
                    "slug": "sport",
                    "text": "Спорт и фитнес (включая борьбу, велоспорт, ГТО, гимнастику, коньки, лыжи, скандинавскую ходьбу, спортивные игры, фитнес и тренажеры)"
                }
            ]
        }
    ]
} as Survey;

export default SurveyPage;
