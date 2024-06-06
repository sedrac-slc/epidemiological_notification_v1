from backend.entities.concrect.municipality import Municipality
from backend.entities.concrect.province import Province
from .province import ProvinceData
from enum import Enum


class MunicipalityData(Enum):
    ALL = [
        # Municípios da província de Luanda
        Municipality(name="Talatona", province=ProvinceData.LUANDA.value),
        Municipality(name="Belas", province=ProvinceData.LUANDA.value),
        Municipality(name="Cacuaco", province=ProvinceData.LUANDA.value),
        Municipality(name="Cazenga", province=ProvinceData.LUANDA.value),
        Municipality(name="Viana", province=ProvinceData.LUANDA.value),
        Municipality(name="Ícolo e Bengo", province=ProvinceData.LUANDA.value),
        Municipality(name="Kilamba Kiaxi", province=ProvinceData.LUANDA.value),
        Municipality(name="Luanda", province=ProvinceData.LUANDA.value),
        # Municípios da província de Bengo
        Municipality(name="Ambriz", province=ProvinceData.BENGO.value),
        Municipality(name="Dande", province=ProvinceData.BENGO.value),
        Municipality(name="Bula Atumbo", province=ProvinceData.BENGO.value),
        Municipality(name="Panguila", province=ProvinceData.BENGO.value),
        # Municípios da província de Benguela
        Municipality(name="Baía Farta", province=ProvinceData.BENGUELA.value),
        Municipality(name="Benguela", province=ProvinceData.BENGUELA.value),
        Municipality(name="Bocoio", province=ProvinceData.BENGUELA.value),
        Municipality(name="Catumbela", province=ProvinceData.BENGUELA.value),
        Municipality(name="Chongoroi", province=ProvinceData.BENGUELA.value),
        Municipality(name="Cubal", province=ProvinceData.BENGUELA.value),
        Municipality(name="Ganda", province=ProvinceData.BENGUELA.value),
        Municipality(name="Lobito", province=ProvinceData.BENGUELA.value),
        # Municípios da província de Bié
        Municipality(name="Andulo", province=ProvinceData.BIE.value),
        Municipality(name="Camacupa", province=ProvinceData.BIE.value),
        Municipality(name="Catabola", province=ProvinceData.BIE.value),
        Municipality(name="Chinguar", province=ProvinceData.BIE.value),
        Municipality(name="Chitembo", province=ProvinceData.BIE.value),
        Municipality(name="Cunje", province=ProvinceData.BIE.value),
        Municipality(name="Cuemba", province=ProvinceData.BIE.value),
        Municipality(name="Kuito", province=ProvinceData.BIE.value),
        # Municípios da província de Cabinda
        Municipality(name="Belize", province=ProvinceData.CABINDA.value),
        Municipality(name="Buco-Zau", province=ProvinceData.CABINDA.value),
        Municipality(name="Cabinda", province=ProvinceData.CABINDA.value),
        Municipality(name="Cacongo", province=ProvinceData.CABINDA.value),
        # Municípios da província de Cuando-Cubango
        Municipality(name="Calai", province=ProvinceData.CUANDO_CUBANGO.value),
        Municipality(name="Cuito Cuanavale", province=ProvinceData.CUANDO_CUBANGO.value),
        Municipality(name="Cuango", province=ProvinceData.CUANDO_CUBANGO.value),
        Municipality(name="Dirico", province=ProvinceData.CUANDO_CUBANGO.value),
        Municipality(name="Longa", province=ProvinceData.CUANDO_CUBANGO.value),
        Municipality(name="Mavinga", province=ProvinceData.CUANDO_CUBANGO.value),
        Municipality(name="Menongue", province=ProvinceData.CUANDO_CUBANGO.value),
        Municipality(name="Nankova", province=ProvinceData.CUANDO_CUBANGO.value),
        # Municípios da província de Cuanza Norte
        Municipality(name="Amboim", province=ProvinceData.CUANZA_NORTE.value),
        Municipality(name="Banga", province=ProvinceData.CUANZA_NORTE.value),
        Municipality(name="Bolongongo", province=ProvinceData.CUANZA_NORTE.value),
        Municipality(name="Cambambe", province=ProvinceData.CUANZA_NORTE.value),
        Municipality(name="Cassoa", province=ProvinceData.CUANZA_NORTE.value),
        Municipality(name="Golungo Alto", province=ProvinceData.CUANZA_NORTE.value),
        Municipality(name="Gongonda", province=ProvinceData.CUANZA_NORTE.value),
        Municipality(name="Ngongoro", province=ProvinceData.CUANZA_NORTE.value),
        # Municípios da província de Cuanza Sul
        Municipality(name="Amboim", province=ProvinceData.CUANZA_SUL.value),
        Municipality(name="Cassoma", province=ProvinceData.CUANZA_SUL.value),
        Municipality(name="Cela", province=ProvinceData.CUANZA_SUL.value),
        Municipality(name="Conda", province=ProvinceData.CUANZA_SUL.value),
        Municipality(name="Ekunga", province=ProvinceData.CUANZA_SUL.value),
        Municipality(name="Kibala", province=ProvinceData.CUANZA_SUL.value),
        Municipality(name="Libolo", province=ProvinceData.CUANZA_SUL.value),
        Municipality(name="Mussende", province=ProvinceData.CUANZA_SUL.value),
        # Municípios da província de Cunene
        Municipality(name="Cahama", province=ProvinceData.CUNENE.value),
        Municipality(name="Cuanhama", province=ProvinceData.CUNENE.value),
        Municipality(name="Kalai", province=ProvinceData.CUNENE.value),
        Municipality(name="Kuvango", province=ProvinceData.CUNENE.value),
        Municipality(name="Namaquembilo", province=ProvinceData.CUNENE.value),
        Municipality(name="Omupanda", province=ProvinceData.CUNENE.value),
        Municipality(name="Xangongo", province=ProvinceData.CUNENE.value),
        # Municípios da província de Huambo
        Municipality(name="Bailundo", province=ProvinceData.HUAMBO.value),
        Municipality(name="Caála", province=ProvinceData.HUAMBO.value),
        Municipality(name="Catchiungo", province=ProvinceData.HUAMBO.value),
        Municipality(name="Ecunda", province=ProvinceData.HUAMBO.value),
        Municipality(name="Huambo", province=ProvinceData.HUAMBO.value),
        Municipality(name="Londuimbali", province=ProvinceData.HUAMBO.value),
        Municipality(name="Longonjo", province=ProvinceData.HUAMBO.value),
        Municipality(name="Munhango", province=ProvinceData.HUAMBO.value),
        # Municípios da província de Huíla
        Municipality(name="Caconda", province=ProvinceData.HUILA.value),
        Municipality(name="Caluquembe", province=ProvinceData.HUILA.value),
        Municipality(name="Chiange", province=ProvinceData.HUILA.value),
        Municipality(name="Chipindo", province=ProvinceData.HUILA.value),
        Municipality(name="Chongoroi", province=ProvinceData.HUILA.value),
        Municipality(name="Cuvango", province=ProvinceData.HUILA.value),
        Municipality(name="Humpata", province=ProvinceData.HUILA.value),
        Municipality(name="Jamba", province=ProvinceData.HUILA.value),
        Municipality(name="Lubango", province=ProvinceData.HUILA.value),
        Municipality(name="Matala", province=ProvinceData.HUILA.value),
        Municipality(name="Quilengues", province=ProvinceData.HUILA.value),
        Municipality(name="Quipungo", province=ProvinceData.HUILA.value),
        # Municípios da província de Lunda Norte
        Municipality(name="Capenda Camulemba", province=ProvinceData.LUNDA_NORTE.value),
        Municipality(name="Cuango", province=ProvinceData.LUNDA_NORTE.value),
        Municipality(name="Cuanhama", province=ProvinceData.LUNDA_NORTE.value),
        Municipality(name="Lucapa", province=ProvinceData.LUNDA_NORTE.value),
        Municipality(name="Lóvua", province=ProvinceData.LUNDA_NORTE.value),
        Municipality(name="Nsolu", province=ProvinceData.LUNDA_NORTE.value),
        Municipality(name="Xá-Muteba", province=ProvinceData.LUNDA_NORTE.value),
        # Municípios da província de Lunda Sul
        Municipality(name="Dala", province=ProvinceData.LUNDA_SUL.value),
        Municipality(name="Cassaquinguina", province=ProvinceData.LUNDA_SUL.value),
        Municipality(name="Lucapa", province=ProvinceData.LUNDA_SUL.value),
        Municipality(name="Mucojo", province=ProvinceData.LUNDA_SUL.value),
        Municipality(name="Sambulo", province=ProvinceData.LUNDA_SUL.value),
        Municipality(name="Songo", province=ProvinceData.LUNDA_SUL.value),
        Municipality(name="Xá-Cassiquinguina", province=ProvinceData.LUNDA_SUL.value),
        # Municípios da província de Malanje
        Municipality(name="Caçuso", province=ProvinceData.MALANJE.value),
        Municipality(name="Calandula", province=ProvinceData.MALANJE.value),
        Municipality(name="Caponte", province=ProvinceData.MALANJE.value),
        Municipality(name="Cazenga", province=ProvinceData.MALANJE.value),
        Municipality(name="Cambundas", province=ProvinceData.MALANJE.value),
        Municipality(name="Cunene", province=ProvinceData.MALANJE.value),
        Municipality(name="Kalandula", province=ProvinceData.MALANJE.value),
        Municipality(name="Luanda", province=ProvinceData.MALANJE.value),
        Municipality(name="Ndalatando", province=ProvinceData.MALANJE.value),
        Municipality(name="Quelima", province=ProvinceData.MALANJE.value),
        # Municípios da província de Moxico
        Municipality(name="Alto Zambeze", province=ProvinceData.MOXICO.value),
        Municipality(name="Cambundos", province=ProvinceData.MOXICO.value),
        Municipality(name="Camba", province=ProvinceData.MOXICO.value),
        Municipality(name="Cassima", province=ProvinceData.MOXICO.value),
        Municipality(name="Cuandi", province=ProvinceData.MOXICO.value),
        Municipality(name="Leopoldo", province=ProvinceData.MOXICO.value),
        Municipality(name="Luena", province=ProvinceData.MOXICO.value),
        Municipality(name="Mucusso", province=ProvinceData.MOXICO.value),
        # Municípios da província de Namibe
        Municipality(name="Bibala", province=ProvinceData.NAMIBE.value),
        Municipality(name="Camucuio", province=ProvinceData.NAMIBE.value),
        Municipality(name="Iona", province=ProvinceData.NAMIBE.value),
        Municipality(name="Lucira", province=ProvinceData.NAMIBE.value),
        Municipality(name="Moçâmedes", province=ProvinceData.NAMIBE.value),
        Municipality(name="Tombwa", province=ProvinceData.NAMIBE.value),
        # Municípios da província de Uíge
        Municipality(name="Ambrizete", province=ProvinceData.UIGE.value),
        Municipality(name="Bembe", province=ProvinceData.UIGE.value),
        Municipality(name="Buengas", province=ProvinceData.UIGE.value),
        Municipality(name="Bungo", province=ProvinceData.UIGE.value),
        Municipality(name="Dambos", province=ProvinceData.UIGE.value),
        Municipality(name="Maquela do Zombo", province=ProvinceData.UIGE.value),
        Municipality(name="Mucaba", province=ProvinceData.UIGE.value),
        Municipality(name="Pombo", province=ProvinceData.UIGE.value),
        Municipality(name="Quimbumdo", province=ProvinceData.UIGE.value),
        Municipality(name="Quimbumdo", province=ProvinceData.UIGE.value),
        Municipality(name="Quinjimbo", province=ProvinceData.UIGE.value),
        Municipality(name="Quitaxi", province=ProvinceData.UIGE.value),
        # Municípios da província de Zaire
        Municipality(name="Cuimba", province=ProvinceData.ZAIRE.value),
        Municipality(name="M'banza-Kongo", province=ProvinceData.ZAIRE.value),
        Municipality(name="Noqui", province=ProvinceData.ZAIRE.value),
        Municipality(name="Nsolu", province=ProvinceData.ZAIRE.value),
        Municipality(name="Songo", province=ProvinceData.ZAIRE.value),
        Municipality(name="Tomboco", province=ProvinceData.ZAIRE.value),
    ]

    def get(data: Province):
        list = []
        for municipality in MunicipalityData.ALL.value:
            if municipality.province.name == data.name:
                municipality.province = data
                list.append(municipality)
        return list