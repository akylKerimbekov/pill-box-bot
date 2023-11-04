CREATE_PILL_TABLE = """
    create table if not exists pill(
        id integer primary key,
        tg_id integer,
        description text,
        time text,
        frequency text,
        is_active integer
    );
"""


INSERT_INTO_PILL_QUERY = """
    insert into pill(id, tg_id, description, time, frequency, is_active)
    values (:id, :tg_id, :description, :time, :frequency, :is_active)
    returning *;
"""

SELECT_ALL_PILLS_BY_TG_ID_QUERY = """
    select * from pill where tg_id = :tg_id and is_active = 1;
"""