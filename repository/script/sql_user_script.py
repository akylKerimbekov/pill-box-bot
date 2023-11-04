CREATE_USER_TABLE = """
    create table if not exists tg_user(
        id integer primary key,
        tg_id integer,
        username text,
        first_name text,
        last_name text,
        phone_number text,
        is_active integer,
        unique (tg_id)
    );
"""

INSERT_INTO_USER_QUERY = """
    insert into tg_user(id, tg_id, username, first_name, last_name, phone_number, is_active)
    values (:id, :tg_id, :username, :first_name, :last_name, :phone_number, :is_active)
    returning *;
"""

SELECT_USER_BY_TG_ID_QUERY = """
    select * from tg_user where tg_id = :tg_id;
"""