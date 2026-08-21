# -*- coding: utf-8 -*-
"""
برنامج حساب سنوات الانتظار لطلاب الدراسة الخارجية (الأبطال)
------------------------------------------------------------
1) تظهر واجهة ترحيبية لمدة 3 ثوانٍ.
2) تنتقل تلقائياً إلى الواجهة الرئيسية (خلفية سوداء).
3) الطالب يكتب سنة امتحانه الأخير.
4) يضغط زر "حساب السنوات" فتظهر له جدول السنوات.
"""

import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox

# ============ الإعدادات العامة (ألوان وخطوط) ============
BG_COLOR = "#000000"        # أسود
FG_COLOR = "#FFFFFF"        # أبيض
ACCENT_COLOR = "#00C896"    # لون مميز (أخضر فاتح) للأزرار والعناوين
ENTRY_BG = "#1a1a1a"
WAIT_COLOR = "#ff6b6b"       # لون سنوات الانتظار (أحمر فاتح)
SUBMIT_COLOR = "#ffd166"     # لون سنة التقديم (أصفر)
EXAM_COLOR = "#06d6a0"       # لون سنة الامتحان (أخضر)


def build_main_window():
    """بناء النافذة الرئيسية (بعد إغلاق الترحيب)."""
    main = tk.Tk()
    main.title("حساب سنوات الانتظار - طلاب الخارجي الأبطال")
    main.configure(bg=BG_COLOR)
    main.geometry("520x520")
    main.resizable(False, False)

    title_font = tkfont.Font(family="Arial", size=18, weight="bold")
    label_font = tkfont.Font(family="Arial", size=13)
    result_font = tkfont.Font(family="Arial", size=14, weight="bold")

    # العنوان
    title_lbl = tk.Label(
        main,
        text="حساب سنوات الانتظار",
        font=title_font,
        bg=BG_COLOR,
        fg=ACCENT_COLOR,
    )
    title_lbl.pack(pady=(25, 10))

    # حقل إدخال سنة الامتحان الأخير
    input_frame = tk.Frame(main, bg=BG_COLOR)
    input_frame.pack(pady=10)

    entry_lbl = tk.Label(
        input_frame,
        text="اكتب سنة امتحانك الأخير (مثال: 2023):",
        font=label_font,
        bg=BG_COLOR,
        fg=FG_COLOR,
    )
    entry_lbl.pack(pady=(0, 8))

    year_entry = tk.Entry(
        input_frame,
        font=label_font,
        justify="center",
        bg=ENTRY_BG,
        fg=FG_COLOR,
        insertbackground=FG_COLOR,
        relief="flat",
        width=15,
    )
    year_entry.pack(ipady=5)

    # إطار عرض النتائج
    result_frame = tk.Frame(main, bg=BG_COLOR)
    result_frame.pack(pady=20, fill="both", expand=True)

    def calculate_years():
        # تفريغ النتائج القديمة قبل الحساب من جديد
        for widget in result_frame.winfo_children():
            widget.destroy()

        raw = year_entry.get().strip()

        if not raw.isdigit():
            messagebox.showerror("خطأ", "الرجاء إدخال سنة صحيحة (أرقام فقط)، مثال: 2023")
            return

        x = int(raw)

        # ==== القوانين المطلوبة ====
        wait_year_1 = x + 1      # السنة الأولى للانتظار
        wait_year_2 = x + 2      # السنة الثانية للانتظار
        new_submit_year = x + 3  # سنة التقديم الجديد
        new_exam_year = x + 4    # سنة الامتحان الجديد

        rows = [
            (wait_year_1, "انتظار", WAIT_COLOR),
            (wait_year_2, "انتظار", WAIT_COLOR),
            (new_submit_year, "تقديم", SUBMIT_COLOR),
            (new_exam_year, "امتحان", EXAM_COLOR),
        ]

        for year, status, color in rows:
            row_lbl = tk.Label(
                result_frame,
                text=f"{year}   {status}",
                font=result_font,
                bg=BG_COLOR,
                fg=color,
            )
            row_lbl.pack(pady=6)

    calc_btn = tk.Button(
        main,
        text="حساب السنوات",
        font=label_font,
        bg=ACCENT_COLOR,
        fg="#000000",
        activebackground="#00a37a",
        relief="flat",
        padx=15,
        pady=6,
        cursor="hand2",
        command=calculate_years,
    )
    calc_btn.pack(pady=10)

    main.mainloop()


def show_splash_then_main():
    """عرض شاشة الترحيب لمدة 3 ثوانٍ، ثم فتح النافذة الرئيسية."""
    splash = tk.Tk()
    splash.overrideredirect(True)   # إخفاء إطار وشريط عنوان النافذة
    splash.configure(bg=BG_COLOR)

    # توسيط النافذة في الشاشة
    width, height = 500, 300
    screen_w = splash.winfo_screenwidth()
    screen_h = splash.winfo_screenheight()
    x = (screen_w - width) // 2
    y = (screen_h - height) // 2
    splash.geometry(f"{width}x{height}+{x}+{y}")

    welcome_font = tkfont.Font(family="Arial", size=20, weight="bold")

    # -----------------------------------------------------------
    # إذا كان عندك صورة فعلية وتريد عرضها بدلاً من النص:
    # 1) ضع ملف الصورة (مثلاً welcome.png) في نفس مجلد هذا الملف.
    # 2) احذف تعليق (uncomment) السطرين التاليين، واحذف كتلة الـ Label النصية بالأسفل.
    #
    # from PIL import Image, ImageTk   # يحتاج تثبيت: pip install pillow
    # img = ImageTk.PhotoImage(Image.open("welcome.png").resize((500, 300)))
    # img_label = tk.Label(splash, image=img, bg=BG_COLOR)
    # img_label.image = img  # مهم: منع حذف الصورة من الذاكرة
    # img_label.pack(fill="both", expand=True)
    # -----------------------------------------------------------

    welcome_label = tk.Label(
        splash,
        text="مرحباً بطلاب الخارجي الأبطال",
        font=welcome_font,
        bg=BG_COLOR,
        fg=ACCENT_COLOR,
        wraplength=450,
        justify="center",
    )
    welcome_label.pack(expand=True)

    def close_splash_and_open_main():
        splash.destroy()
        build_main_window()

    # بعد 3000 ملي ثانية (3 ثوانٍ) يتم إغلاق الترحيب وفتح النافذة الرئيسية
    splash.after(3000, close_splash_and_open_main)
    splash.mainloop()


if __name__ == "__main__":
    show_splash_then_main()
