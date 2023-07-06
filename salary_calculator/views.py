from django.shortcuts import render

def home(request):
    return render(request, 'salary_calculator.html')

def calculate(request):
    if request.method == 'POST':
        base_salary = float(request.POST.get('base_salary'))
        days_not_worked = int(request.POST.get('days_not_worked'))
        social_fund_contribution = base_salary * 0.1
        income_tax = (base_salary - social_fund_contribution - 650.0) * 0.1
        net_salary = base_salary - social_fund_contribution - income_tax

        net_salary -= (net_salary / 22) * days_not_worked

        net_salary = round(net_salary, 2)

        expanded_equation = f"Net Salary = {base_salary} - {social_fund_contribution} - {income_tax} - (Net Salary / 30) * {days_not_worked} = {net_salary}"

        return render(request, 'salary_result.html',
                      {
                          'base_salary': base_salary,
                          'net_salary': net_salary,
                          'expanded_equation': expanded_equation,
                          'social_fund_contribution': social_fund_contribution,
                          'income_tax': income_tax
                      })
