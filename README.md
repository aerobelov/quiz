# Install


## Installation


```bash
git pull origin main
pipenv shell
```

## GET /api/sets
Request active sets

```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "sets": [
        {
            "title": "Product satisfaction quiz",
            "start_date": "2021-03-31",
            "end_date": "2021-04-30"
        }
    ]
}
```

## GET /api/question/<question_id:int>
Request question with id

```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "question": [
        {
            "id": 1,
            "type": {
                "type": "Single"
            },
            "set": {
                "title": "Product satisfaction quiz",
                "start_date": "2021-03-31",
                "end_date": "2021-04-30"
            },
            "text": "Are you satisfied with our new product?"
        }
    ],
    "options": [
        {
            "id": 1,
            "text": "I am satisfied"
        },
        {
            "id": 2,
            "text": "Absolutely not"
        }
    ]
}
```

## GET /api/user_answer/<user_id:int>
Request user answers
```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "answers": [
        {
            "user": {
                "user_number": 1
            },
            "question": {
                "id": 1,
                "type": {
                    "type": "Single"
                },
                "set": {
                    "title": "Product satisfaction quiz",
                    "start_date": "2021-03-31",
                    "end_date": "2021-04-30"
                },
                "text": "Are you satisfied with our new product?"
            },
            "option": {
                "id": 1,
                "text": "I am satisfied"
            }
        },
        {
            "user": {
                "user_number": 1
            },
            "question": {
                "id": 2,
                "type": {
                    "type": "Single"
                },
                "set": {
                    "title": "Product satisfaction quiz",
                    "start_date": "2021-03-31",
                    "end_date": "2021-04-30"
                },
                "text": "Do you want something to add?"
            },
            "option": {
                "id": 3,
                "text": "No, it's full"
            }
        },
        {
            "user": {
                "user_number": 1
            },
            "question": {
                "id": 2,
                "type": {
                    "type": "Single"
                },
                "set": {
                    "title": "Product satisfaction quiz",
                    "start_date": "2021-03-31",
                    "end_date": "2021-04-30"
                },
                "text": "Do you want something to add?"
            },
            "option": {
                "id": 4,
                "text": "Yes, please add other features"
            }
        }
    ]
}
```

## POST /api/save
Save question

```
data = {
            'user': user_number <int>,
            'question' : question_id<int>,
            'option': option_id<int>,
            'freetext': freetext_answer<string>,
        }
```
