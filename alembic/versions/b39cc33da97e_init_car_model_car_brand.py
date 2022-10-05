"""init car model & car brand

Revision ID: b39cc33da97e
Revises: 
Create Date: 2022-10-05 09:26:19.184674

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers, used by Alembic.
revision = 'b39cc33da97e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "car_brand",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("logo_url", sa.String(), nullable=True),
        sa.Column("num_of_models", sa.Integer(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("last_update", sa.DateTime(), default=datetime.now, nullable=True, onupdate=datetime.now),
        sa.Column("status", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_car_brand_id"), "car_brand", ["id"], unique=False)
    op.create_index(op.f("ix_car_brand_name"), "car_brand", ["name"], unique=False)
    op.create_index(op.f("ix_car_brand_status"), "car_brand", ["status"], unique=False)
    
    op.create_table(
        "car_model",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("image_url", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("brand_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["brand_id"], ["car_brand.id"],),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_car_model_name"), "car_model", ["name"], unique=True)
    op.create_index(op.f("ix_car_model_id"), "car_model", ["id"], unique=False)

def downgrade():
    op.drop_index(op.f("ix_car_model_name"), table_name="car_model")
    op.drop_index(op.f("ix_car_model_id"), table_name="car_model")
    op.drop_table("car_model")
    op.drop_index(op.f("ix_car_brand_id"), table_name="car_brand")
    op.drop_index(op.f("ix_car_brand_name"), table_name="car_brand")
    op.drop_index(op.f("ix_car_brand_status"), table_name="car_brand")
    op.drop_table("car_brand")
