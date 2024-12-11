import base64

def codifica(x):
    for i in 'ab':
        i = base64.b64encode(x)
        x = i
    return x
print(codifica(b'a31p20lf'))


def decodifica(x):
	for i in 'abcdefghi':
		i = base64.b64decode(x)
		x = i
	return x
print(decodifica(b'Vm0wd2VHUXhTWGhpUm1SWFYwZG9WMWx0ZUV0WFJteFZVMjA1VjJKSGVGWlZiVEZIVmpGYWMySkVUbGhoTVhCUVdWZDRTMk14WkhWaFJscHBWa1phVFZac1ZtRldNVnBXVFZWV2FHVnFRVGs9='))
