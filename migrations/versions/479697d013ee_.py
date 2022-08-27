"""empty message

Revision ID: 479697d013ee
Revises: 5abb383c4fd9
Create Date: 2022-08-22 10:49:24.103519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '479697d013ee'
down_revision = '5abb383c4fd9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(length=150), nullable=True))
    op.create_unique_constraint(None, 'user', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'username')
    # ### end Alembic commands ###
