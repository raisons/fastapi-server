from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "user" (
    "hashed_password" VARCHAR(128),
    "last_login" TIMESTAMP,
    "is_superuser" INT NOT NULL  DEFAULT 0,
    "username" VARCHAR(20) NOT NULL UNIQUE,
    "nickname" VARCHAR(50),
    "mobile" VARCHAR(11)  UNIQUE,
    "email" VARCHAR(100)  UNIQUE,
    "is_active" INT NOT NULL  DEFAULT 1,
    "date_joined" TIMESTAMP NOT NULL,
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
