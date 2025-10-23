# rules = [
#     {"if": {"fever", "cough", "fatigue"}, "then": "Flu"},
#     {"if": {"fever", "cough", "shortness of breath"}, "then": "COVID-19"},
#     {"if": {"headache", "nausea", "sensitivity to light"}, "then": "Migraine"},
#     {"if": {"sore throat", "runny nose", "sneezing"}, "then": "Common Cold"},
#     {"if": {"chest pain", "shortness of breath", "dizziness"}, "then": "Heart Attack"},
# ]

# def diagnose(symptoms):
#     matched_diseases = []
#     symptoms_set = set(symptoms)
#     for rule in rules:
#         if rule["if"].issubset(symptoms_set):
#             matched_diseases.append(rule["then"])
#     return matched_diseases

# def main():
#     print("\nWelcome to the Medical Expert System")
#     print("Enter your symptoms separated by commas (e.g., fever, cough):")
#     user_input = input("Symptoms: ").lower()
#     symptoms = [s.strip() for s in user_input.split(",")]
#     diagnoses = diagnose(symptoms)
#     if diagnoses:
#         print("\n⚠ Possible diagnosis(es):")
#         for disease in diagnoses:
#             print(f"- {disease}")
#     else:
#         print("\nNo matching diagnosis found. Please consult a doctor.")

# if __name__ == "__main__":
#     main()


rules = {
    tuple(sorted({"fever", "cough", "fatigue"})): "Flu",
    tuple(sorted({"fever", "cough", "shortness of breath"})): "COVID-19",
    tuple(sorted({"headache", "nausea", "sensitivity to light"})): "Migraine",
    tuple(sorted({"sore throat", "runny nose", "sneezing"})): "Common Cold",
    tuple(sorted({"chest pain", "shortness of breath", "dizziness"})): "Heart Attack",
}

def diagnose(symptoms: tuple[str]) -> list[str]:
    symptoms = tuple(sorted(symptoms))
    matched_diseases = []
    for rule in rules:
        if set(rule).issubset(set(symptoms)):
            matched_diseases.append(rules[rule])
    
    return matched_diseases

print("\nWelcome to the Medical Expert System")
print("Enter your symptoms separated by commas (e.g., fever, cough):")
user_input = input("Symptoms: ").lower()
symptoms = [s.strip() for s in user_input.split(",")]
diagnoses = diagnose(tuple(symptoms))
if diagnoses:
    print("\n⚠ Possible diagnosis(es):")
    for disease in diagnoses:
        print(f"- {disease}")
else:
    print("\nNo matching diagnosis found. Please consult a doctor.")

