TREATMENTS: dict[str, dict[str, str]] = {
    "bird": {
        "Avian Pox": "Please drink more water",
        "Psittacosis": "Please drink more water",
    },
    "cat": {
        "Feline URI": "Please drink more water",
        "Ringworm": "Please drink more water",
    },
    "chicken": {
        "Coccidiosis": "Please drink more water",
        "Newcastle Disease": "Please drink more water",
    },
    "cow": {
        "Avian Pox": "Please drink more water",
        "Psittacosis": "Please drink more water",
    },
    "dog": {
        "Mange": "Please drink more water",
        "Parvovirus": "Please drink more water",
        "Rabies": "Please drink more water",
    },
    "horse": {
        "Colic": "Please drink more water",
        "Equine Influenza": "Please drink more water",
        "Laminitis": "Please drink more water",
    },
    "pigeon": {
        "Salmonella": "Please drink more water",
        "Trichomoniasis": "Please drink more water",
    },
}

_DEFAULT_TREATMENT = "Please drink more water"


def get_treatment(animal: str, disease: str) -> str:
    """Return the treatment text for the given animal and disease.

    Falls back to the default treatment if the combination is not found.
    """
    return TREATMENTS.get(animal, {}).get(disease, _DEFAULT_TREATMENT)
