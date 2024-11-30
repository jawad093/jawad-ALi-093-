def remove_punct(txt):
    puncts = '''.,?!:;'"()#[]}{-—.../\*&@_~^|'''
    cleaned_txt = ''
    for i in txt:
        if i in puncts:
            continue
        else:
            remove_txt += i
    return remove_txt

userr_input = input('Enter your sentence: ')
print(remove_punct(userr_input))
