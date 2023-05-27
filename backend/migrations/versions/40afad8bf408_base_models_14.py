"""base models #14

Revision ID: 40afad8bf408
Revises: 8560231e65e3
Create Date: 2023-05-27 10:16:54.464476

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '40afad8bf408'
down_revision = '8560231e65e3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('address', 'group_old_ids',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('address', 'group_old_ids',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
