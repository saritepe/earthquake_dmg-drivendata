import category_encoders


def select_encoder(cols, encoder_name='BinaryEncoder'):
    return getattr(category_encoders, encoder_name)(cols=cols)
