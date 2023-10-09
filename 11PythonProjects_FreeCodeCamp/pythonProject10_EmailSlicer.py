# Get user email address
email = input("¿Cuál es tu correo electrónico?: ").strip()

# Slice out the user name
user_name = email[:email.index("@")]

# Slice the domain name
domain_name = email[email.index("@")+1:]

# Format message
if domain_name=="gmail.com":
    output = "Hola '{}', veo que estás registrado en '{}'".format(user_name,domain_name)
elif domain_name=="yahoo.com":
    output = "Hola '{}', no es muy común tener cuenta en '{}'".format(user_name,domain_name)
elif domain_name=="hotmail.com":
    output = "Hola '{}', ¿Debes tener este correo hace mucho no?, pues es '{}'".format(user_name,domain_name)
elif domain_name=="uabc.edu.mx":
    output = "Hola cimarrón '{}' usando orgullosamente '{}'".format(user_name,domain_name)
else:
    output = "Hola '{}' ¿usando un dominio diferente?, nunca habia visto '{}'".format(user_name,domain_name)

# Display output message
print(output)