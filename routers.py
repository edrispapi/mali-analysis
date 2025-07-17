from fastapi import APIRouter
from user_routes import router as user_router
from report_routes import router as report_router

router = APIRouter()

# روترهای حوزه‌های مختلف
router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(report_router, prefix="/reports", tags=["reports"])

# می‌شود در ادامه، بقیه سرویس‌ها مثل market، analysis، notification را نیز اضافه کرد.
