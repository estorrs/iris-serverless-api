import json

from sklearn.externals import joblib

IRIS_CLASSIFIER = joblib.load('model/model.pkl')
LABELS = json.load(open('model/labels.json'))

def status(event, context):
    body = {
        "message": "Good to go!",
    }

    response = {
        "statusCode": 200,
        "headers": {"content-type": "application/json"},
        "body": json.dumps(body)
    }

    return response

def predict(event, context):
    request = json.loads(event['body'])
    X = request['X']

    prediction = IRIS_CLASSIFIER.predict([X])

    body = {
        'label': LABELS[prediction[0]],
        'input': X
    }

    response = {
        "statusCode": 200,
        "headers": {"content-type": "application/json"},
        "body": json.dumps(body)
    }

    return response
