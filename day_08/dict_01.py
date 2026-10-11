# Capgemini
# TL - Koushik,
# DH- Sudipta,
# AID - Arpan,
# Deadline - 25th October,
# total_members-7,
# client - electrolux,
# is_completed: False

# Modelling with List
# rutuja_job = (
#     "Capgemini",
#     "Koushik",
#     "Sudipta",
#     "Arpan",
#     "25/10/2026",
#     7,
#     "Electrolux",
#     False,
# )


from datetime import datetime

# Modelling with Dictionary
rutuja_job = {
    "total_members": 7,
    "is_completed": False,
    "company": "Capgemini",
    "tl": "Koushik",
    "dh": "Sudipta",
    "aid": "arpan",
    "deadline": datetime.now(),
    "locations": ["Hinjewadi", "Talawade", "Kolkata"],
    "payroll": (5, 2, 4),
}

# Access values using key
print(rutuja_job["deadline"])
print(rutuja_job["aid"])
print(rutuja_job["deadline"])

rut_payroll = rutuja_job["payroll"]

