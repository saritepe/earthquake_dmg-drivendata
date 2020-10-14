from src.data.categorize_data import get_drop_cols


def drop_cols(df):
    # parametre olarak eklenmeli mi bunlar ?
    # index de yapılabilir guid kolonu?
    cols = get_drop_cols()
    return df.drop(cols, axis=1)
