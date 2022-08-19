ano = int(input('digite o ano que você deseja saber: '))
bissexto = ano/4
if(float.is_integer(bissexto)):
    print (f'o ano {ano} é bissexto')
else:
    print (f'o ano {ano} não é bissexto')
