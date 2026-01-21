def groupAnagrams(strs: list[str]) -> list[list[str]]:
    mapping = {}

    for i in strs:
        sorted_i = "".join(sorted(i))
        if sorted_i not in mapping:
            mapping[sorted_i] = []

        mapping[sorted_i].append(i)
    
    return list(mapping.values())

if __name__ == "__main__":
    print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))

