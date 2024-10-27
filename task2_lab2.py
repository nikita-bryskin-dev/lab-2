salary = 5000           # Ежемесячная зарплата
spend = 6000            # Траты за первый месяц
months = 10             # Количество месяцев, которые нужно покрыть
increase = 0.05         # Рост цен (5% ежемесячно)

# Инициализация переменной для общей нехватки средств
total_shortage = 0

# Цикл для расчета нехватки средств за 10 месяцев
for month in range(months):
    # Увеличиваем расходы на 5% начиная со второго месяца
    if month > 0:
        spend *= (1 + increase)
    
    # Рассчитываем нехватку средств в текущем месяце
    shortage = spend - salary
    if shortage > 0:
        total_shortage += shortage  # Добавляем нехватку к общей

# Округляем до целого числа
required_capital = round(total_shortage)

# Вывод результата
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", required_capital)