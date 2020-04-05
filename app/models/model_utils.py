def model_from_dict(model, **kwargs):
    for key, value in kwargs.items():
        if hasattr(model, key):
            # print("setting {0}= {1}".format(key, value))
            setattr(model, key, value)
        else:
            print("NOT setting {0} not found (value={1})".format(key, value))
