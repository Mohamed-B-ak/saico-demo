# ============================================
#  DATABASE MODULE (DB + DEMO DATA ONLY)
# ============================================

from sqlalchemy import create_engine, Column, Integer, String, Float, Date, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from datetime import date, timedelta

# --------------------------------------------
# Database Connection
# --------------------------------------------
DATABASE_URL = "sqlite:///./invoices.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()


# --------------------------------------------
# Database Model
# --------------------------------------------
class CustomerInvoice(Base):
    __tablename__ = "customer_invoices"

    id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    invoice_amount = Column(Float)
    payment_date = Column(Date)
    customer_phone = Column(String)
    customer_email = Column(String)
    is_paid = Column(Boolean, default=False)


# --------------------------------------------
# Create tables
# --------------------------------------------
Base.metadata.create_all(engine)


# --------------------------------------------
# Insert demo data ONCE (no cron, no scheduler)
# --------------------------------------------
def insert_demo_data():
    db = SessionLocal()
    # 1️⃣ Delete all existing invoices
    db.query(CustomerInvoice).delete()
    db.commit()
    # 2️⃣ Insert fresh demo rows
    if db.query(CustomerInvoice).count() == 0:
        demo_rows = [
            {
                "customer_name": "Mohamed Akacha",
                "invoice_amount": 120,
                "payment_date": date.today() - timedelta(days=3),
                "customer_phone": "+966115102700",
                "customer_email": "Mohamed@example.com"
            },
            {
                "customer_name": "Mohamed Akacha",
                "invoice_amount": 300,
                "payment_date": date.today() + timedelta(days=2),
                "customer_phone": "+966115102700",
                "customer_email": "akacha@example.com"
            },
            {
                "customer_name": "Mohamed Akacha",
                "invoice_amount": 200,
                "payment_date": date.today() - timedelta(days=1),
                "customer_phone": "+966115102700",
                "customer_email": "med.ak@example.com"
            },
        ]

        for row in demo_rows:
            db.add(CustomerInvoice(**row))

        db.commit()
    db.close()


# --------------------------------------------
# DB Dependency for FastAPI
# --------------------------------------------
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()

insert_demo_data()