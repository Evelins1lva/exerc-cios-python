def is_anagram(palavra1, palavra2):
    return sorted(palavra1) == sorted(palavra2)
if __name__ == "__main__":
    print(is_anagram("amor", "roma"))         
    print(is_anagram("python", "typhon"))     
    print(is_anagram("banana", "abana"))      
