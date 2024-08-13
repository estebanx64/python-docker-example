## Simple python docker dev example for the official docker docs

https://docs.docker.com/language/python/containerize/

## Run the application

docker compose up --build

## Run the application in the background

docker compose up --build -d

## Stop the application

press ctrl+c to stop the application.
docker compose down

## FastAPI info

To see the OpenAPI docs you can go to http://localhost:8000/docs.

## Sample JSON payload

{
"employee_name": "MR Ross Gellar",
"employee_id": "001",
"pay_period": "2022/08/31",
"job_title": "Training Manager",
"company_name": "RocketSlip Holdings Limited",
"known_as": "Ross",
"job_grade": "Paterson F",
"company_address": "987 Rocket Ship, 654 Rocket Lane, Launchpad",
"employee_address": "987 Rocket Ship, 654 Rocket Lane, Launchpad",
"paye_ref_no": "7770703199",
"uif_reg_no": "0111111/8",
"rate_per_hour": "216.35",
"hours_per_period": "173.33",
"account_no": "987654321",
"income_tax_no": "0004532230",
"branch_no": "250655",
"payment_type": "ACB",
"earnings": [
{"description": "Cash", "amount": "7,672.00"},
{"description": "Production Bonus", "amount": "1,000.00"},
{"description": "Cellphone Reimbursement", "amount": "3,000.00"}
],
"deductions": [
{"description": "Pay as you Earn", "amount": "639.50"},
{"description": "Unemployment Insurance Fund", "amount": "177.12"},
{"description": "LOAN", "amount": "4,500.00"},
{"description": "SAVING", "amount": "2,500.00"},
{"description": "VITALITY", "amount": "296.00"}
],
"total_earnings": "11,672.00",
"total_deductions": "8,112.62",
"net_pay": "3,559.38",
"company_contributions": [
{"description": "Skills Development Levy", "amount": "339.00"},
{"description": "Unemployment Insurance Fund", "amount": "177.12"},
{"description": "Medical Aid", "amount": "14,328.00"},
{"description": "Provident Fund", "amount": "5,625.00"}
],
"year_to_date": [
{"description": "Tax Paid", "amount": "3,836.95"},
{"description": "Taxable Earnings", "amount": "70,032.00"},
{"description": "Taxable Company Contributions", "amount": "0.00"},
{"description": "Fringe Benefits", "amount": "178,968.00"},
{"description": "Tax Deductible Deductions", "amount": "33,750.00"},
{"description": "Provisions", "amount": "237,981.00"},
{"description": "Private Contributions", "amount": "3,000.00"}
]
}
