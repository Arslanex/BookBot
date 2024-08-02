def main():
    # Dosyanın yolunu belirleyin
    path_to_file = "books/frankenstein.txt"

    # Dosyayı açın ve içeriği okuyun
    with open(path_to_file, 'r') as f:
        file_contents = f.read()

    # Kelimeleri sayan fonksiyonu çağırın
    word_count = count_words(file_contents)

    # Sonucu ekrana yazdırın
    print(f"Total number of words: {word_count}")

def count_words(text):
    # Metni kelimelere bölün
    words = text.split()
    
    # Kelime sayısını döndürün
    return len(words)

# Programı çalıştırın
if __name__ == "__main__":
    main()
