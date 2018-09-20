palavra = {"pt-br": "cadeira",
           "ing":"chair",
           "es": "silla",
           "al": "stuhl",
           "fr": "chaise"}
def tradução(idioma):
    return palavra[idioma]
print(tradução('ing'))