"""empty message

Revision ID: 5d9d2c65820e
Revises: 
Create Date: 2024-04-22 19:13:23.559438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d9d2c65820e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('id', sa.String(length=126), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('user',
    sa.Column('fullname', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('username', sa.String(length=120), nullable=True),
    sa.Column('bio', sa.String(length=500), nullable=True),
    sa.Column('phone', sa.String(length=11), nullable=False),
    sa.Column('password_hash', sa.String(length=1024), nullable=True),
    sa.Column('image_url', sa.String(length=500), nullable=True),
    sa.Column('email_verified', sa.Boolean(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('id', sa.String(length=126), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('phone')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('quiz',
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('category_id', sa.String(length=126), nullable=False),
    sa.Column('id', sa.String(length=126), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('attempt',
    sa.Column('quiz_id', sa.String(length=126), nullable=False),
    sa.Column('user_id', sa.String(length=126), nullable=False),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('id', sa.String(length=126), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['quiz_id'], ['quiz.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('question',
    sa.Column('text', sa.String(length=255), nullable=False),
    sa.Column('quiz_id', sa.String(length=126), nullable=False),
    sa.Column('id', sa.String(length=126), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['quiz_id'], ['quiz.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('option',
    sa.Column('text', sa.String(length=255), nullable=False),
    sa.Column('is_correct', sa.Boolean(), nullable=False),
    sa.Column('question_id', sa.String(length=126), nullable=False),
    sa.Column('id', sa.String(length=126), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('response',
    sa.Column('attempt_id', sa.String(length=126), nullable=False),
    sa.Column('question_id', sa.String(length=126), nullable=False),
    sa.Column('option_id', sa.String(length=126), nullable=False),
    sa.Column('id', sa.String(length=126), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['attempt_id'], ['attempt.id'], ),
    sa.ForeignKeyConstraint(['option_id'], ['option.id'], ),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('response')
    op.drop_table('option')
    op.drop_table('question')
    op.drop_table('attempt')
    op.drop_table('quiz')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    op.drop_table('category')
    # ### end Alembic commands ###
