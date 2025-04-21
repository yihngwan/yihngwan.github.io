import calendar

def generate_markdown_calendar_monday_first(year: int, month: int) -> str:
    cal = calendar.Calendar(firstweekday=0)  # 周一为首
    month_name = calendar.month_name[month]
    
    header = f"## {month:02d}月({month_name})\n\n"
    table_header = "| 一 | 二 | 三 | 四 | 五 | 六 | 日 |\n"
    table_divider = "|---|---|---|---|---|---|---|\n"
    
    weeks = cal.monthdayscalendar(year, month)
    table_rows = ""
    
    for week in weeks:
        row = "|"
        for day in week:
            if day == 0:
                row += "    |"
            else:
                day_link = f"[{day}]({year}/{year}-{month:02d}-{day:02d}.md)"
                row += f"{day_link}|"
        table_rows += row + "\n"
    
    return header + table_header + table_divider + table_rows

# 🧪 在这里修改年份和月份：
print(generate_markdown_calendar_monday_first(2023, 12))
print(generate_markdown_calendar_monday_first(2023, 11))
print(generate_markdown_calendar_monday_first(2023, 10))
print(generate_markdown_calendar_monday_first(2023, 9))
print(generate_markdown_calendar_monday_first(2023, 8))
print(generate_markdown_calendar_monday_first(2023, 7))
print(generate_markdown_calendar_monday_first(2023, 6))
print(generate_markdown_calendar_monday_first(2023, 5))
print(generate_markdown_calendar_monday_first(2023, 4))
print(generate_markdown_calendar_monday_first(2023, 3))
print(generate_markdown_calendar_monday_first(2023, 2))
print(generate_markdown_calendar_monday_first(2023, 1))

