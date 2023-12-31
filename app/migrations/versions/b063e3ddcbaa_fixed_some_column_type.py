"""Fixed some column type

Revision ID: b063e3ddcbaa
Revises: b7509a38f562
Create Date: 2023-11-01 21:25:27.712420

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b063e3ddcbaa"
down_revision: Union[str, None] = "b7509a38f562"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "bookings",
        "total_days",
        existing_type=sa.NUMERIC(precision=10, scale=2),
        type_=sa.Integer(),
        existing_nullable=True,
    )
    op.alter_column("rooms", "hotel_id", existing_type=sa.INTEGER(), nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("rooms", "hotel_id", existing_type=sa.INTEGER(), nullable=True)
    op.alter_column(
        "bookings",
        "total_days",
        existing_type=sa.Integer(),
        type_=sa.NUMERIC(precision=10, scale=2),
        existing_nullable=True,
    )
    # ### end Alembic commands ###
