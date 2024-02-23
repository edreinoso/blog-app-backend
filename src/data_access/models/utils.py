from sqlalchemy.orm import class_mapper


def model_to_dict(model) -> dict:
    d = {}
    for k in class_mapper(model.__class__).c.keys():
        d[k] = getattr(model, k)
    return d
