import re


def extract_date(text_lines):
    """
    Find date from OCR text
    """

    date_pattern = r"\d{2}/\d{2}/\d{4}"

    for line in text_lines:
        match = re.search(date_pattern, line)
        if match:
            return match.group()

    return None


def extract_total(text_lines):
    """
    Find total amount
    """

    for i, line in enumerate(text_lines):

        if "total" in line.lower():

            for j in range(i, min(i+3, len(text_lines))):

                amount = re.findall(r"\d+\.\d{2}", text_lines[j])

                if amount:
                    return amount[-1]

    return None


def extract_vendor(text_lines):
    """
    Vendor usually appears at the top of receipt
    """

    for line in text_lines[:5]:

        if len(line) > 5 and not any(char.isdigit() for char in line):
            return line

    return None


def extract_fields(text_lines):

    vendor = extract_vendor(text_lines)
    date = extract_date(text_lines)
    total = extract_total(text_lines)

    return {
        "vendor": vendor,
        "date": date,
        "total": total
    }