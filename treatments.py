TREATMENTS: dict[str, dict[str, str]] = {
    "bird": {
        "Psittacosis": "Antibiotics(Tetracycline) + Isolation of infected birds",
        "Avian Pox": "Topical antiseptic + isolation",
    },
    "cat": {
        "Feline URI":  "Amoxicillin + supportive care",
        "Ringworm":  "Antifungal cream (Miconazole) + Ketoconazole spray + disinfect bedding",
    },
    "chicken": {
        "Coccidiosis": "Amprolium + clean water + disinfect floor" ,
        "Newcastle Disease":  "Vitamins + Newcastle vaccine",
    },
    "cow": {
        "Mastitis": "Penicillin injection (or intramammary infusion) + Frequent milking + warm compress + fluids + udder hygiene and disinfection",
        "Foot and Mouth Disease": "Vaccine + antibiotics for secondary infection +Supportive drugs (vitamins + fluids)",
        "Bloat": "Antifoaming agents(Poloxalene) + mineral oil + massage ",
    },
    "dog": {
        "Mange": "Ivermectin + clean bedding + isolation",
        "Parvovirus": "IV fluids + Amoxicillin + Metronidazole",
        "Rabies":  "Rabies vaccine (preventive) + isolation",
    },
    "horse": {
        "Colic": "Analgesics + walking + hydration",
        "Equine Influenza": "Vaccine + antiviral+ Paracetamol + fluids",
        "Laminitis": "Anti-inflammatory + hoof care",
    },
    "pigeon": {
        "Salmonella": "Antibiotics (Enrofloxacin) + Disinfection of water and cage + vitamins + hydration",
        "Trichomoniasis":  "Metronidazole + clean water",
    },
}

_DEFAULT_TREATMENT = "Please Consult a veternian."


def get_treatment(animal: str, disease: str) -> str:
    """Return the treatment text for the given animal and disease.

    Falls back to the default treatment if the combination is not found.
    """
    return TREATMENTS.get(animal, {}).get(disease, _DEFAULT_TREATMENT)
