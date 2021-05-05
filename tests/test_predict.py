from mercari_model import predict
import numpy

def test_predict(input_name):
    subject = predict.make_prediction([input_name])
    assert subject is not None
    assert isinstance(subject[0], numpy.int64)
    assert subject[0] == 3 ## input_name == logitech mouse, which then is predicted as 6 (electronics)