import datetime
from sqlalchemy import Column, Integer, String, DateTime
from db_manager import Base

class AuditLog(Base):
    __tablename__ = 'audit_logs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    action = Column(String(255), nullable=False)
    ip_address = Column(String(64))
    detail = Column(String(1024))
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

def log_action(session, user_id, action, ip_address=None, detail=None):
    """ثبت رویداد یا تراکنش امنیتی مهم"""
    log = AuditLog(
        user_id=user_id,
        action=action,
        ip_address=ip_address,
        detail=detail
    )
    session.add(log)
    session.commit()
