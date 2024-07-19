# pylint: disable=invalid-name
"""Add Restaurant Table

Revision ID: 11b40de5c0cb
Revises:
Create Date: 2022-12-07 21:31:23.559324

"""
import sqlalchemy as sa
import sqlmodel.sql.sqltypes

from alembic import op

# revision identifiers, used by Alembic.
revision = "11b40de5c0cb"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "restaurant",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("open_weekday", sa.Integer(), nullable=False),
        sa.Column("open_time", sa.Time(), nullable=False),
        sa.Column("close_weekday", sa.Integer(), nullable=False),
        sa.Column("close_time", sa.Time(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_restaurant_id"), "restaurant", ["id"], unique=True)
    op.create_index(
        op.f("ix_restaurant_unique_times"),
        "restaurant",
        ["name", "open_weekday", "open_time", "close_weekday", "close_time"],
        unique=True,
    )


def downgrade() -> None:
    op.drop_index(op.f("ix_restaurant_unique_times"), table_name="restaurant")
    op.drop_index(op.f("ix_restaurant_id"), table_name="restaurant")
    op.drop_table("restaurant")
