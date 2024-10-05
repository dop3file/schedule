"""Alter group table: name not unique

Revision ID: a3f0bbb40c44
Revises: b3efd915baa2
Create Date: 2024-10-04 14:40:34.290440

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3f0bbb40c44'
down_revision: Union[str, None] = 'b3efd915baa2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('groups_name_key', 'groups', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('groups_name_key', 'groups', ['name'])
    # ### end Alembic commands ###
