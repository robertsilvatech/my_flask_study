"""empty message

Revision ID: 855d3a1f689c
Revises: 433a5fc362d2
Create Date: 2019-03-26 18:05:13.568241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '855d3a1f689c'
down_revision = '433a5fc362d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('organization', sa.Column('status', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('organization', 'status')
    # ### end Alembic commands ###
