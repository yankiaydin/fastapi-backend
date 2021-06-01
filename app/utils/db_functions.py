from .db import fetch, execute

async def add_staff(staff):
    query = """insert into personels(name, password, position, id) values(:name, :password, :position, :id)"""
    values = {"name":staff.name, "password":staff.password, "position": staff.position, "id": staff.id}
    await execute(query, False, values)

async def login_staff(persona):
    query = """select * from personels where name = :name and password = :password"""
    values = {"name": persona.name, "password": persona.password}
    result = await fetch(query, True, values)
    if result is None:
        return None
    return True

async def fetch_staff(position: str):
    query = """select * from personels where position = :position"""
    values = {"position":position}
    result = await fetch(query, False, values)
    return result

async def patch_position(id : int, position: str):
    query = """update personels set position = :position where id = :id """
    values = {"id":id, "position":position}
    await execute(query, False, values)

async def update_staff(id, persona):
    query = """update personels set name = :name, position= :position where id = :id """
    values = {"name": persona.name, "position":persona.position, "id": id}
    await execute(query, False, values)

async def delete_staff(id):
    query = """delete from personels where id = :id"""
    values = {"id":id}
    await execute(query, False,values)

async def photo_db(id: str, url: str, size : str):
    query = """insert into images(img_id, img_url, img_size) values(:img_id, :img_url, :img_size)"""
    values = {"img_id": id, "img_url":url,"img_size": size}
    await execute(query, False, values)


