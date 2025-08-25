from django import template

register = template.Library()

@register.filter
def currency(value):
    """
    Formatea un número como dinero con separadores de miles y dos decimales.
    Ejemplo: 1234567.89 -> $1.234.567,89
    """
    try:
        value = float(value)
    except (TypeError, ValueError):
        return value  # si no es número, se devuelve tal cual

    # formato estilo latino (puntos como separadores de miles, coma decimal)
    formatted = f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"${formatted}"