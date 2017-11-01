"""empty message

Revision ID: 90e26111b47f
Revises: 0887f2e025aa
Create Date: 2017-10-16 23:40:49.967000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90e26111b47f'
down_revision = '0887f2e025aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('label', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('question', 'label')
    # ### end Alembic commands ###