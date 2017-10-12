"""empty message

Revision ID: e424d03ba260
Revises: ace8d095a26b
Create Date: 2017-10-12 11:25:11.775853

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e424d03ba260'
down_revision = 'ace8d095a26b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('gist', sa.Column('lang', sa.String(length=30), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('gist', 'lang')
    # ### end Alembic commands ###
