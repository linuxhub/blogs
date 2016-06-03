"""initial migration

Revision ID: 5c5ddb755e41
Revises: 15c64d4eb722
Create Date: 2016-06-03 01:17:25.548000

"""

# revision identifiers, used by Alembic.
revision = '5c5ddb755e41'
down_revision = '15c64d4eb722'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('title', sa.Text(length=128), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'title')
    ### end Alembic commands ###
