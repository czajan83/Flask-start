from sqlalchemy import create_engine, text

import hidden_data

ENGINE = create_engine(f"mysql+pymysql://{hidden_data.SQL_CRED}/EarthData")


def sql_select(table, condition=None):
    with ENGINE.connect() as conn:
        columns = conn.execute(text(f"SHOW COLUMNS FROM {table};"))
        items = conn.execute(text(f"SELECT * FROM {table}" +
                                  (f" WHERE {condition}" if condition is not None else "") + ";"))
    return columns, items
