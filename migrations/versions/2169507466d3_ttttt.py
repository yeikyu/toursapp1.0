"""ttttt

Revision ID: 2169507466d3
Revises: 33724f7ef611
Create Date: 2024-07-10 20:51:17.590744

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2169507466d3'
down_revision = '33724f7ef611'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ciudad',
    sa.Column('id_ciudad', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=255), nullable=False),
    sa.Column('estado', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_ciudad')
    )
    op.drop_table('ciudades')
    with op.batch_alter_table('clientes', schema=None) as batch_op:
        batch_op.drop_constraint('clientes_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'ciudad', ['ciudad'], ['id_ciudad'])

    with op.batch_alter_table('destinos', schema=None) as batch_op:
        batch_op.drop_constraint('destinos_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'ciudad', ['ciudad'], ['id_ciudad'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('destinos', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('destinos_ibfk_1', 'ciudades', ['ciudad'], ['id_ciudad'])

    with op.batch_alter_table('clientes', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('clientes_ibfk_1', 'ciudades', ['ciudad'], ['id_ciudad'])

    op.create_table('ciudades',
    sa.Column('id_ciudad', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('nombre', mysql.VARCHAR(collation='utf8mb3_spanish_ci', length=255), nullable=False),
    sa.Column('estado', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id_ciudad'),
    mariadb_collate='utf8mb3_spanish_ci',
    mariadb_default_charset='utf8mb3',
    mariadb_engine='InnoDB'
    )
    op.drop_table('ciudad')
    # ### end Alembic commands ###