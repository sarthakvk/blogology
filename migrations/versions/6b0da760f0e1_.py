"""empty message

Revision ID: 6b0da760f0e1
Revises: 
Create Date: 2020-04-05 00:53:03.372102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b0da760f0e1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dat', sa.Text(), nullable=True),
    sa.Column('title', sa.Text(), nullable=False),
    sa.Column('short', sa.Text(), nullable=False),
    sa.Column('breif', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Blog')
    # ### end Alembic commands ###