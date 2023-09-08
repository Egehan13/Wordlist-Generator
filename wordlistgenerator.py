import itertools

# Oluşturulacak wordlist dosyasının adı
wordlist_file = "wordlist.txt"

# İşlem yapılacak isim
name = "name"

# Wordlist dosyasını oluşturma
with open(wordlist_file, "w") as file:
    # İsmi alt kümelerine ayırma
    for length in range(1, len(name) + 1):
        for subset in itertools.permutations(name, length):
            subset_name = ''.join(subset)
            file.write(subset_name + "\n")

    # İsmi alt kümelerine ek harfleri ekleyerek ayırma
    for length in range(1, len(name)):
        for subset in itertools.combinations(name, length):
            remaining_chars = ''.join(char for char in name if char not in subset)
            for permutation in itertools.permutations(remaining_chars):
                subset_name = ''.join(subset) + ''.join(permutation)
                file.write(subset_name + "\n")

print(f"Wordlist oluşturma tamamlandı: {wordlist_file}")
