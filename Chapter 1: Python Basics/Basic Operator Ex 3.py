#Zoblik uses a system where employees need a specific security level and a valid badge to enter restricted areas.

# Zoblik employee access credentials
employee_security_level = 7
required_security_level = 4
has_valid_badge = False
is_admin = True # Whether the employee has admin privileges

# Condition 1: Does the employee meet the required security level?
meets_security_requirement = employee_security_level >= required_security_level
print(f"Meets security level requirement? {meets_security_requirement}")

# Condition 2: Does the employee have a valid badge AND meet the security level?
can_enter_restricted_area = meets_security_requirement and has_valid_badge
print(f"Can enter restricted area? {can_enter_restricted_area}")

# Condition 3: Can enter if they meet security OR are an admin (even without a badge for specific cases)
can_access_override = meets_security_requirement or is_admin
print(f"Can access with override privileges? {can_access_override}")

# Condition 4: What if an employee does NOT have a valid badge?
does_not_have_valid_badge = not has_valid_badge
print(f"Does not have a valid badge? {does_not_have_valid_badge}")