from django.db.models import F


def monthly_payment(deposit, first_payment, term, stavka):
    total_amount = deposit - first_payment
    denominator = total_amount * ((F(stavka)/100) / 12)
    numerator = 1 - (1 + ((F(stavka)/100) / 12)) * (1 - term * 12)
    return denominator / numerator


"""
Ссылка с формулой и объяснением:
https://www.raiffeisen.ru/wiki/formuly-dlya-samostoyatelnogo-rascheta-ipoteki/?ysclid=l5gm7lez0497928402
"""
