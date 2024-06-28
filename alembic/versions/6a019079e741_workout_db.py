"""workout_db

Revision ID: 6a019079e741
Revises: 
Create Date: 2024-06-28 20:03:29.475813

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a019079e741'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('atletas',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nome', sa.String(length=50), nullable=False),
        sa.Column('cpf', sa.String(length=11), nullable=False),
        sa.Column('idade', sa.Integer(), nullable=False),
        sa.Column('peso', sa.Float(), nullable=False),
        sa.Column('altura', sa.Float(), nullable=False),
        sa.Column('sexo', sa.String(length=1), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('cpf')
    )
    op.create_index(op.f('ix_atletas_id'), 'atletas', ['id'], unique=False)
    
    op.create_table('categorias',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nome', sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('nome')
    )
    op.create_index(op.f('ix_categorias_id'), 'categorias', ['id'], unique=False)
    
    op.create_table('centro_de_treinamentos',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nome', sa.String(length=50), nullable=False),
        sa.Column('endereco', sa.String(length=60), nullable=False),
        sa.Column('proprietario', sa.String(length=30), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('nome')
    )
    op.create_index(op.f('ix_centro_de_treinamentos_id'), 'centro_de_treinamentos', ['id'], unique=False)
    


def downgrade() -> None:
    
    op.drop_index(op.f('ix_centro_de_treinamentos_id'), table_name='centro_de_treinamentos')
    op.drop_table('centro_de_treinamentos')
    op.drop_index(op.f('ix_categorias_id'), table_name='categorias')
    op.drop_table('categorias')
    op.drop_index(op.f('ix_atletas_id'), table_name='atletas')
    op.drop_table('atletas')
