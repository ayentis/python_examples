
def to_camel(in_str: str) -> str:
    map = str.maketrans("","","-_")
    print(map)
    print(in_str.title())
    y = in_str[0]+in_str.title().translate(map)[1:]
    print(y)



to_camel('python_community_ru')# -> 'pythonCommunityRu'
to_camel('Python-community-Ru')# -> 'PythonCommunityRu'