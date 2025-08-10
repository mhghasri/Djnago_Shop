# Django Shop

یک پروژه فروشگاه آنلاین ساخته‌شده با **Django** که شامل مدیریت محصولات، سبد خرید، سفارشات و احراز هویت کاربران است.

## نصب و اجرا
```bash
git clone https://github.com/mhghasri/Djnago_Shop.git
cd Djnago_Shop

python -m venv .venv
source .venv/bin/activate  # یا در ویندوز: .venv\Scripts\activate

pip install -r requirements.txt

cp .env.example .env  # فایل env را بسازید و مقادیر را تنظیم کنید

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## پیکربندی `.env`
```env
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=127.0.0.1,localhost

DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
```

## ویژگی‌ها
- مدیریت محصولات و دسته‌بندی‌ها
- سبد خرید و ثبت سفارش
- احراز هویت کاربران
- پنل مدیریت Django

## مجوز
MIT License
