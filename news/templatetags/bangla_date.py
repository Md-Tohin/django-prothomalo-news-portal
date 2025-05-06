from django import template
import datetime

register = template.Library()

english_to_bangla = str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")

months = {
    "January": "জানুয়ারি",
    "February": "ফেব্রুয়ারি",
    "March": "মার্চ",
    "April": "এপ্রিল",
    "May": "মে",
    "June": "জুন",
    "July": "জুলাই",
    "August": "আগস্ট",
    "September": "সেপ্টেম্বর",
    "October": "অক্টোবর",
    "November": "নভেম্বর",
    "December": "ডিসেম্বর",
}

@register.filter
def bangla_date(value):
    # Handle DateTimeField or DateField
    if isinstance(value, datetime.datetime):
        value = value.date()
    if not isinstance(value, datetime.date):
        return value

    formatted = value.strftime("%d %B %Y").lstrip("0")
    parts = formatted.split(" ")
    day = parts[0].translate(english_to_bangla)
    month = months.get(parts[1], parts[1])
    year = parts[2].translate(english_to_bangla)
    return f"{day} {month} {year}"


@register.filter
def bangla_datetime(value):
    if not isinstance(value, (datetime.date, datetime.datetime)):
        return value

    # Use .strftime for full datetime
    formatted = value.strftime("%d %B %Y, %H:%M")

    # Extract and translate components
    day, month, year_time = formatted.split(" ", 2)
    year, time = year_time.split(",", 1)
    day = day.translate(english_to_bangla)
    month = months.get(month, month)
    year = year.strip().translate(english_to_bangla)
    time = time.strip().translate(english_to_bangla)

    return f"{day} {month} {year}, {time}"