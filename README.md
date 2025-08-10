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
DB_NAME = 'DB_NAME'
DB_USER = 'DB_USER'
DB_PASSWORD = 'DB_STRONGPASSWORD'
DB_HOST = 'DB_IP'
DB_PORT = 'DB_PORT'
```

## ویژگی‌ها
- مدیریت محصولات و دسته‌بندی‌ها
- سبد خرید و ثبت سفارش
- احراز هویت کاربران
- پنل مدیریت Django

## مجوز
MIT License
