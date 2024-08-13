from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from fastapi.responses import StreamingResponse
from io import BytesIO

# Function to create a PDF payslip from JSON data
def pdf_payslip_creator(data):

    # Create a buffer to hold the PDF data
    buffer = BytesIO()

    # Register the font
    pdfmetrics.registerFont(TTFont('Menlo-Regular', 'Menlo-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('Menlo-Bold', 'Menlo-Bold.ttf'))

    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    y_left = 20
    y_middle = 210
    y_right = 400
    y_middle_middle = 320
    running_height = height - 40

    # Setting title and header
    c.setFont("Menlo-Bold", 16)
    c.drawString(280, running_height, "Payslip")
    running_height -= 20

    # Draw a line for visual separation
    running_height -= 10
    c.line(20, running_height, 590, running_height)
    running_height -= 20

    c.setFont("Menlo-Regular", 8)
    c.drawString(y_left, running_height, f"Employee ID:")
    c.drawString(y_left + 75, running_height, f"{data['employee_id']}")
    c.drawString(y_middle, running_height,  f"Job Title:")
    c.drawString(y_middle + 75, running_height,  f"{data['job_title']}")
    c.drawString(y_right, running_height,  f"Pay Period:")
    c.drawString(y_right + 75, running_height,  f"{data['pay_period']}")
    running_height -= 20

    c.drawString(y_left, running_height, f"Employee Name:")
    c.drawString(y_left + 75, running_height, f"{data['employee_name']}")
    c.drawString(y_middle, running_height, f"Job Grade:")
    c.drawString(y_middle + 75, running_height, f"{data['job_grade']}")
    c.drawString(y_right, running_height, f"Company Name:")
    c.drawString(y_right + 75, running_height, f"{data['company_name']}")
    running_height -= 20

    c.drawString(y_left, running_height, f"Known As:")
    c.drawString(y_left + 75, running_height, f"{data['known_as']}")
    c.drawString(y_middle, running_height, f"Rate / Hour:")
    c.drawString(y_middle + 75, running_height, f"{data['rate_per_hour']}")
    c.drawString(y_right, running_height, f"PAYE Ref. No.:")
    c.drawString(y_right + 75, running_height, f"{data['paye_ref_no']}")
    running_height -= 20

    c.drawString(y_left, running_height, f"Income Tax No.:")
    c.drawString(y_left + 75, running_height, f"{data['income_tax_no']}")
    c.drawString(y_middle, running_height, f"Hours / Period:")
    c.drawString(y_middle + 75, running_height, f"{data['hours_per_period']}")
    c.drawString(y_right, running_height, f"UIF Reg. No.:")
    c.drawString(y_right + 75, running_height, f"{data['uif_reg_no']}")
    running_height -= 20

    # Draw a line for visual separation
    running_height -= 10
    c.line(y_left, running_height, 590, running_height)
    running_height -= 20

    # Drawing the table headers for Earnings and Deductions
    c.setFont("Menlo-Bold", 10)
    c.drawString(y_left, running_height, "Earnings")
    c.drawString(y_middle_middle, running_height, "Deductions")
    running_height -= 20

    # Drawing Earnings and Deductions
    y = running_height
    for earning in data['earnings']:
        c.setFont("Menlo-Regular", 8)
        c.drawString(y_left, y, f"{earning['description']}:")
        c.drawString(y_left + 180, y, f"R {float(earning['amount'].replace(",", "")):,.2f}".rjust(15))
        y -= 20

    y = running_height
    for deduction in data['deductions']:
        c.setFont("Menlo-Regular", 8)
        c.drawString(y_middle_middle, y, f"{deduction['description']}:")
        c.drawString(y_middle_middle + 180, y, f"R {float(deduction['amount'].replace(",", "")):,.2f}".rjust(15))
        y -= 20

    running_height = y

    # Draw a line for visual separation
    running_height -= 10
    c.line(y_left, running_height, 590, running_height)
    running_height -= 20

    # Adding the totals
    c.setFont("Menlo-Bold", 10)
    c.drawString(y_left, running_height, f"Total Earnings:")
    c.drawString(y_left + 160, running_height, f"R {float(data['total_earnings'].replace(",", "")):,.2f}".rjust(15))
    c.drawString(y_middle_middle, running_height, f"Total Deductions:")
    c.drawString(y_middle_middle + 160, running_height, f"R {float(data['total_deductions'].replace(",", "")):,.2f}".rjust(15))
    running_height -= 20

    c.drawString(y_middle_middle, running_height, f"Net Pay:")
    c.drawString(y_middle_middle + 160, running_height, f"R {float(data['net_pay'].replace(",", "")):,.2f}".rjust(15))
    running_height -= 20

    # Draw a line for visual separation
    running_height -= 10
    c.line(20, running_height, 590, running_height)
    running_height -= 20

    # Adding Company Contributions
    c.setFont("Menlo-Bold", 10)
    c.drawString(y_left, running_height, "Company Contributions")
    running_height -= 20
    y = running_height
    y2 = y
    for contribution in data['company_contributions']:
        c.setFont("Menlo-Regular", 8)
        c.drawString(y_left, y, f"{contribution['description']}:")
        c.drawString(y_left + 180, y, f"R {float(contribution['amount'].replace(",", "")):,.2f}".rjust(15))
        y -= 20

    # Adding Year To Date Totals
    c.setFont("Menlo-Bold", 10)
    y = y2
    c.drawString(y_middle_middle, y + 20, "Year To Date Totals")
    for ytd in data['year_to_date']:
        c.setFont("Menlo-Regular", 8)
        c.drawString(y_middle_middle, y, f"{ytd['description']}:")
        c.drawString(y_middle_middle + 180, y, f"R {float(ytd['amount'].replace(",", "")):,.2f}".rjust(15))
        y -= 20

    c.save()

    # Set the buffer's position to the beginning
    buffer.seek(0)
    
    # Return the PDF via StreamingResponse
    return StreamingResponse(buffer, media_type="application/pdf", headers={
        "Content-Disposition": "inline; filename=temp.pdf"
    })
