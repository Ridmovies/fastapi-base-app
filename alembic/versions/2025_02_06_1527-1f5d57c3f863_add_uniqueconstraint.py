"""add UniqueConstraint

Revision ID: 1f5d57c3f863
Revises: 97e2662b000f
Create Date: 2025-02-06 15:27:35.417872

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1f5d57c3f863"
down_revision: Union[str, None] = "97e2662b000f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("foo", sa.String(), nullable=False))
    op.add_column("users", sa.Column("bar", sa.String(), nullable=False))
    op.create_unique_constraint(None, "users", ["foo", "bar"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "users", type_="unique")
    op.drop_column("users", "bar")
    op.drop_column("users", "foo")
    # ### end Alembic commands ###
