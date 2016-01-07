"""empty message

Revision ID: 887862cdc2a
Revises: None
Create Date: 2015-10-29 11:29:06.138242

"""

# revision identifiers, used by Alembic.
revision = '887862cdc2a'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    member_table = op.create_table('member',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=False),
    sa.Column('last_name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )

    # Seed with "guest" accounts
    op.bulk_insert(member_table,
    [
        {'id':1, 'first_name':'Guest', 'last_name': 'Creator'},
        {'id':2, 'first_name':'Guest', 'last_name': 'Pledgor'},
    ])

    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('short_description', sa.Text(), nullable=False),
    sa.Column('long_description', sa.Text(), nullable=False),
    sa.Column('goal_amount', sa.Integer(), nullable=False),
    sa.Column('image_filename', sa.String(length=128), nullable=False),
    sa.Column('time_created', sa.DateTime(), nullable=False),
    sa.Column('time_start', sa.DateTime(), nullable=False),
    sa.Column('time_end', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['member_id'], ['member.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pledge',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('time_created', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['member_id'], ['member.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pledge')
    op.drop_table('project')
    op.drop_table('member')
    ### end Alembic commands ###
