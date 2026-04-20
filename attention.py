ATTENTIONS: dict[str, dict[str, str]] = {
    "bird": {
        "Psittacosis": "Zoonotic, Use protective equipment",
        "Avian Pox": ""
    },
    "cat": {
        "Feline URI": "Contagious",
        "Ringworm": "Zoonotic"
    },
    "chicken": {
        "Coccidiosis": "",
        "Newcastle Disease": ""
    },
    "cow": {
        "Mastitis": "Milk from a treated cow must not be consumed until the antibiotic withdrawal period has ended",
        "Foot and Mouth Disease": "Highly contagious",
        "Bloat": "Emergency condition, Please consult a veterinarian"
    },
    "dog": {
        "Mange": "Treat all in-contact animals",
        "Parvovirus": "Isolation is essential",
        "Rabies": "Zoonotic disease"
    },
    "horse": {
        "Colic": "Emergency condition, Please consult a veterinarian",
        "Laminitis": "",
        "Equine Influenza": "Highly contagious + Rest is importatnt"
    },
    "pigeon": {
        "Salmonella": "Zoonotic",
        "Trichomoniasis": ""
    }
}

_DEFAULT_ATTENTION = ""


def get_attention(animal: str, disease: str) -> str:
    """Return the attention text for the given animal and disease.

    Falls back to the default attention if the combination is not found.
    """
    return ATTENTIONS.get(animal, {}).get(disease, _DEFAULT_ATTENTION)