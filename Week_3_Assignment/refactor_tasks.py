def calculate_shipping(order, customer):
    if customer is None:
        return 400
    
    if customer.is_premium:
        if order.total >= 5000:
            return 0
        return 100
        
    if order.total >= 5000:
        return 200
        
    return 400


def is_eligible_for_bonus(emp):
    is_experienced = emp.months_employed >= 12
    good_rating = emp.performance_rating >= 4
    no_issues = not emp.has_disciplinary_action
    good_attendance = emp.attendance_rate >= 0.90
    
    return emp.is_active and is_experienced and good_rating and no_issues and good_attendance


def process_bonus(employee):
    if is_eligible_for_bonus(employee):
        return "Bonus Approved"
    else:
        return "Bonus Denied"


def check_access(user, resource):
    if user is None or not user.active:
        return False
    if resource is None:
        return False
        
    if user.role == "admin" or resource.owner_id == user.id or resource.public:
        return True
        
    return False