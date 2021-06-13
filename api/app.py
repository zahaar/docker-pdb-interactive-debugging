from flask import Flask, jsonify, make_response

app = Flask(__name__)


@app.route('/api/v1.0/the_answer', methods=['GET'])
def test_response():
    """Return a sample JSON response."""

    true_response = {
        "answer": "42"
    }

    fake_response = {
        "answer": "what_is_the_question?"
    }
    # JSONify response
    response = make_response(jsonify(fake_response))

    # start interactive debugging
    import pdb
    pdb.set_trace()


    return response
