"""registro

Revision ID: 5e1374d2b36f
Revises: 
Create Date: 2024-03-18 19:19:11.961559

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e1374d2b36f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('panicos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('registro', sa.String(length=100), nullable=True),
    sa.Column('hora_execucao', sa.TIMESTAMP(), nullable=True),
    sa.Column('hora_coleta', sa.TIMESTAMP(), nullable=True),
    sa.Column('exame', sa.String(length=100), nullable=True),
    sa.Column('resultado', sa.String(length=100), nullable=True),
    sa.Column('setor', sa.String(length=100), nullable=True),
    sa.Column('comunicacao', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_panicos_id'), 'panicos', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_panicos_id'), table_name='panicos')
    op.drop_table('panicos')
    # ### end Alembic commands ###
