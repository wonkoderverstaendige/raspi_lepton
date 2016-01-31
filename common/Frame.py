import base64
import json
import numpy as np
import io


class FrameEncoder(json.JSONEncoder):
    def default(self, obj):
	if isinstance(obj, Frame):
            output = io.BytesIO()
            np.savez_compressed(output, arr=obj.arr)
            return {'idx' : obj.idx,
                    'arr_b64npz' : base64.b64encode(output.getvalue())}
        return json.JSONEncoder.default(self, obj)


class Frame(object):
    def __init__(self, idx, arr):
        self.idx = int(idx)
        self.arr = arr

    def encode(self):
        return json.dumps(self, cls=FrameEncoder)

    @classmethod
    def from_json(cls, json_msg):
        dct = json.loads(json_msg, object_hook=frame_decoder)
        return cls.from_dict(dct)

    @classmethod
    def from_dict(cls, dct):
        return cls(dct['idx'], dct['arr'])


def frame_decoder(dct):
    if isinstance(dct, dict) and 'arr_b64npz' in dct:
        output = io.BytesIO(base64.b64decode(dct['arr_b64npz']))
        output.seek(0)
        dct['arr'] = np.load(output)['arr']
        return dct
    return None


if __name__ == "__main__":
    expected = np.random.random_integers(10, size=(60, 80))
    
    frame = Frame(0, expected)
    dumped = frame.encode()
    loaded = Frame.from_json(dumped)

    
    print "Loaded frame idx:", loaded.idx
    result = loaded.arr
    assert result.dtype == expected.dtype, "Wrong Type"
    assert result.shape == expected.shape, "Wrong Shape"
    assert np.array_equal(expected, result), "Wrong Values"
    
    print "OK"
