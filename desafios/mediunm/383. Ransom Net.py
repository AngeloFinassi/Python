def inbiri():
    ransomNote = "ab"
    magazine = "aab"
    if ransomNote in magazine:
        return True
    if ransomNote not in magazine:
        return False

print(inbiri())