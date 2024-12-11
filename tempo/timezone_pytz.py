import pytz, datetime
from datetime import datetime
from pytz import all_timezones, timezone, common_timezones, country_timezones, country_names



def horario_outra_zona(loc_agora, nome_zona, agora = datetime.now()):
	outra_zona = loc_agora.astimezone(timezone(nome_zona))
	return '{0} - {1} '.format(nome_zona, outra_zona.strftime(fmt))

fmt = '%H:%M - %d/%m/%Y'
agora = datetime.now()

zona_local = timezone('America/Sao_Paulo')
loc_agora = zona_local.localize(agora)

print('{0} - {1} '.format(zona_local, loc_agora.strftime(fmt)))

# for cada_pais in common_timezones:
# 	print(horario_outra_zona(loc_agora, cada_pais))
cidade = input("Digite uma cidade: ")
print(horario_outra_zona(loc_agora, cidade))
# print(all_timezones)
# print(len(all_timezones))
# print(common_timezones)
# print(len(common_timezones))
# print(list(country_timezones))
# print(len(country_timezones))
# print(country_names)

"""
DATA
    __all__ = ['timezone', 'utc', 'country_timezones', 'country_names', 'A...
    all_timezones = ['Africa/Abidjan', 'Africa/Accra', 'Africa/Addis...amo...
    all_timezones_set = LazySet({'Europe/Oslo', 'Etc/GMT+0', 'Africa/Asm.....
    common_timezones = ['Africa/Abidjan', 'Africa/Accra', 'Africa/Addis......
    common_timezones_set = LazySet({'Europe/Oslo', 'Africa/Asmara', 'Ameri...
    country_names = <pytz._CountryNameDict object>
    country_timezones = <pytz._CountryTimezoneDict object>
    utc = <UTC>
"""