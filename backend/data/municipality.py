from backend.entities.concrect.municipality import Municipality
from backend.entities.concrect.province import Province
from .province import ProvinceData
from enum import Enum


class MunicipalityData(Enum):
    BENGUELA = Municipality(name="Benguela", province=ProvinceData.BENGUELA.value)
    KILAMBA_KIAXI = Municipality(name="Kilamba Kiaxi", province=ProvinceData.LUANDA.value)
    SAMBA = Municipality(name="Samba", province=ProvinceData.LUANDA.value)
    HUAMBO =  Municipality(name="Huambo", province=ProvinceData.HUAMBO.value)

    ALL = [
        # Municípios da província de Luanda
        Municipality(name="Talatona", province=ProvinceData.LUANDA.value),
        Municipality(name="Belas", province=ProvinceData.LUANDA.value),
        SAMBA,
        Municipality(name="Cacuaco", province=ProvinceData.LUANDA.value),
        Municipality(name="Cazenga", province=ProvinceData.LUANDA.value),
        Municipality(name="Viana", province=ProvinceData.LUANDA.value),
        Municipality(name="Ícolo e Bengo", province=ProvinceData.LUANDA.value),
        KILAMBA_KIAXI,
        Municipality(name="Luanda", province=ProvinceData.LUANDA.value),
        Municipality(name="Quiçama", province=ProvinceData.LUANDA.value),
        # Municípios da província de Bengo
        Municipality(name="Ambriz", province=ProvinceData.BENGO.value),
        Municipality(name="Dande", province=ProvinceData.BENGO.value),
        Municipality(name="Bula Atumbo", province=ProvinceData.BENGO.value),
        Municipality(name="Panguila", province=ProvinceData.BENGO.value),
        Municipality(name="Dembos", province=ProvinceData.BENGO.value),
        Municipality(name="Nambuangongo", province=ProvinceData.BENGO.value),
        # Municípios da província de Benguela
        Municipality(name="Balombo", province=ProvinceData.BENGUELA.value),
        Municipality(name="Baía Farta", province=ProvinceData.BENGUELA.value),
        BENGUELA,
        Municipality(name="Bocoio", province=ProvinceData.BENGUELA.value),
        Municipality(name="Caimbambo", province=ProvinceData.BENGUELA.value),
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
        Municipality(name="Nharea", province=ProvinceData.BIE.value),
        # Municípios da província de Cabinda
        Municipality(name="Belize", province=ProvinceData.CABINDA.value),
        Municipality(name="Buco-Zau", province=ProvinceData.CABINDA.value),
        Municipality(name="Cabinda", province=ProvinceData.CABINDA.value),
        Municipality(name="Cacongo", province=ProvinceData.CABINDA.value),
        # Municípios da província de Cuando-Cubango
        Municipality(name="Calai", province=ProvinceData.KUANDO_CUBANGO.value),
        Municipality(name="Cuito Cuanavale", province=ProvinceData.KUANDO_CUBANGO.value),
        Municipality(name="Cuango", province=ProvinceData.KUANDO_CUBANGO.value),
        Municipality(name="Dirico", province=ProvinceData.KUANDO_CUBANGO.value),
        Municipality(name="Longa", province=ProvinceData.KUANDO_CUBANGO.value),
        Municipality(name="Mavinga", province=ProvinceData.KUANDO_CUBANGO.value),
        Municipality(name="Menongue", province=ProvinceData.KUANDO_CUBANGO.value),
        Municipality(name="Nankova", province=ProvinceData.KUANDO_CUBANGO.value),
        Municipality(name="Rivungo", province=ProvinceData.KUANDO_CUBANGO.value),
        # Municípios da província de Cuanza Norte
        Municipality(name="Ambaca", province=ProvinceData.KUANZA_NORTE.value),
        Municipality(name="Amboim", province=ProvinceData.KUANZA_NORTE.value),
        Municipality(name="Banga", province=ProvinceData.KUANZA_NORTE.value),
        Municipality(name="Bolongongo", province=ProvinceData.KUANZA_NORTE.value),
        Municipality(name="Cambambe", province=ProvinceData.KUANZA_NORTE.value),
        Municipality(name="Cassoa", province=ProvinceData.KUANZA_NORTE.value),
        Municipality(name="Cazengo", province=ProvinceData.KUANZA_NORTE.value),
        Municipality(name="Golungo Alto", province=ProvinceData.KUANZA_NORTE.value),
        Municipality(name="Gongonda", province=ProvinceData.KUANZA_NORTE.value),
        Municipality(name="Ngongoro", province=ProvinceData.KUANZA_NORTE.value),
        Municipality(name="Lucala", province=ProvinceData.KUANZA_NORTE.value),
        Municipality(name="Quiculungo", province=ProvinceData.KUANZA_NORTE.value),
        Municipality(name="Samba Caju", province=ProvinceData.KUANZA_NORTE.value),
        # Municípios da província de Cuanza Sul
        Municipality(name="Amboim", province=ProvinceData.KUANZA_SUL.value),
        Municipality(name="Cassoma", province=ProvinceData.KUANZA_SUL.value),
        Municipality(name="Cela", province=ProvinceData.KUANZA_SUL.value),
        Municipality(name="Conda", province=ProvinceData.KUANZA_SUL.value),
        Municipality(name="Ekunga", province=ProvinceData.KUANZA_SUL.value),
        Municipality(name="Kibala", province=ProvinceData.KUANZA_SUL.value),
        Municipality(name="Libolo", province=ProvinceData.KUANZA_SUL.value),
        Municipality(name="Mussende", province=ProvinceData.KUANZA_SUL.value),
        # Municípios da província de Cunene
        Municipality(name="Cahama", province=ProvinceData.CUNENE.value),
        Municipality(name="Cuanhama", province=ProvinceData.CUNENE.value),
        Municipality(name="Curoca", province=ProvinceData.CUNENE.value),
        Municipality(name="Cuvelay", province=ProvinceData.CUNENE.value),        
        Municipality(name="Kalai", province=ProvinceData.CUNENE.value),
        Municipality(name="Kuvango", province=ProvinceData.CUNENE.value),
        Municipality(name="Namacunde", province=ProvinceData.CUNENE.value),
        Municipality(name="Namaquembilo", province=ProvinceData.CUNENE.value),
        Municipality(name="Ombadja", province=ProvinceData.CUNENE.value),
        Municipality(name="Omupanda", province=ProvinceData.CUNENE.value),
        Municipality(name="Xangongo", province=ProvinceData.CUNENE.value),
        # Municípios da província de Huambo
        Municipality(name="Bailundo", province=ProvinceData.HUAMBO.value),
        Municipality(name="Caála", province=ProvinceData.HUAMBO.value),
        Municipality(name="Catchiungo", province=ProvinceData.HUAMBO.value),
        Municipality(name="EKunha", province=ProvinceData.HUAMBO.value),
        HUAMBO,
        Municipality(name="Londuimbali", province=ProvinceData.HUAMBO.value),
        Municipality(name="Longonjo", province=ProvinceData.HUAMBO.value),
        Municipality(name="Munhango", province=ProvinceData.HUAMBO.value), 
        Municipality(name="Tchicala-Tcholoanga", province=ProvinceData.HUAMBO.value),
        Municipality(name="Tchindjenje", province=ProvinceData.HUAMBO.value),
        Municipality(name="Ucuma", province=ProvinceData.HUAMBO.value),
        # Municípios da província de Huíla
        Municipality(name="Caconda", province=ProvinceData.HUILA.value),
        Municipality(name="Cacula", province=ProvinceData.HUILA.value),
        Municipality(name="Caluquembe", province=ProvinceData.HUILA.value),
        Municipality(name="Chiange", province=ProvinceData.HUILA.value),
        Municipality(name="Chibia", province=ProvinceData.HUILA.value),
        Municipality(name="Chipindo", province=ProvinceData.HUILA.value),
        Municipality(name="Chongoroi", province=ProvinceData.HUILA.value),
        Municipality(name="Kuvango", province=ProvinceData.HUILA.value),
        Municipality(name="Humpata", province=ProvinceData.HUILA.value),
        Municipality(name="Jamba", province=ProvinceData.HUILA.value),
        Municipality(name="Lubango", province=ProvinceData.HUILA.value),
        Municipality(name="Matala", province=ProvinceData.HUILA.value),
        Municipality(name="Quilengues", province=ProvinceData.HUILA.value),
        Municipality(name="Quipungo", province=ProvinceData.HUILA.value),
        # Municípios da província de Lunda Norte
        Municipality(name="Cambulo", province=ProvinceData.LUNDA_NORTE.value),
        Municipality(name="Capenda Camulemba", province=ProvinceData.LUNDA_NORTE.value),
        Municipality(name="Cuango", province=ProvinceData.LUNDA_NORTE.value),
        Municipality(name="Cuanhama", province=ProvinceData.LUNDA_NORTE.value),
        Municipality(name="Chitato (Tchitato)", province=ProvinceData.LUNDA_NORTE.value),
        Municipality(name="Cuilo", province=ProvinceData.LUNDA_NORTE.value),
        Municipality(name="Lucapa", province=ProvinceData.LUNDA_NORTE.value),
        Municipality(name="Lubalo", province=ProvinceData.LUNDA_NORTE.value),
        Municipality(name="Lóvua", province=ProvinceData.LUNDA_NORTE.value),
        Municipality(name="Nsolu", province=ProvinceData.LUNDA_NORTE.value),
        Municipality(name="Xá-Muteba", province=ProvinceData.LUNDA_NORTE.value),
        # Municípios da província de Lunda Sul
        Municipality(name="Dala", province=ProvinceData.LUNDA_SUL.value),
        Municipality(name="Cacolo", province=ProvinceData.LUNDA_SUL.value),
        Municipality(name="Cassaquinguina", province=ProvinceData.LUNDA_SUL.value),
        Municipality(name="Mucojo", province=ProvinceData.LUNDA_SUL.value),
        Municipality(name="Muconda", province=ProvinceData.LUNDA_SUL.value),
        Municipality(name="Sambulo", province=ProvinceData.LUNDA_SUL.value),
        Municipality(name="Saurimo", province=ProvinceData.LUNDA_SUL.value),
        Municipality(name="Songo", province=ProvinceData.LUNDA_SUL.value),
        Municipality(name="Xá-Cassiquinguina", province=ProvinceData.LUNDA_SUL.value),
        # Municípios da província de Malanje
        Municipality(name="Caçuso", province=ProvinceData.MALANJE.value),
        Municipality(name="Calandula", province=ProvinceData.MALANJE.value),
        Municipality(name="Cambundi-Catembo", province=ProvinceData.MALANJE.value),
        Municipality(name="Cangandala", province=ProvinceData.MALANJE.value),
        Municipality(name="Caombo", province=ProvinceData.MALANJE.value),
        Municipality(name="Cuaba Nzogo", province=ProvinceData.MALANJE.value),
        Municipality(name="Cunda-Diaza", province=ProvinceData.MALANJE.value),
        Municipality(name="Luquembo", province=ProvinceData.MALANJE.value),
        Municipality(name="Malange", province=ProvinceData.MALANJE.value),
        Municipality(name="Marimba", province=ProvinceData.MALANJE.value),
        Municipality(name="Massango", province=ProvinceData.MALANJE.value),
        Municipality(name="Caculama-Mucari", province=ProvinceData.MALANJE.value),
        Municipality(name="Quela", province=ProvinceData.MALANJE.value),
        Municipality(name="Quirima", province=ProvinceData.MALANJE.value),
        # Municípios da província de Moxico
        Municipality(name="Alto Zambeze", province=ProvinceData.MOXICO.value),
        Municipality(name="Bundas", province=ProvinceData.MOXICO.value),
        Municipality(name="Camanongue", province=ProvinceData.MOXICO.value),
        Municipality(name="Cameia", province=ProvinceData.MOXICO.value),
        Municipality(name="Luau", province=ProvinceData.MOXICO.value),
        Municipality(name="Lucano", province=ProvinceData.MOXICO.value),
        Municipality(name="Luchazes", province=ProvinceData.MOXICO.value),
        Municipality(name="Léua", province=ProvinceData.MOXICO.value),
        Municipality(name="Moxico", province=ProvinceData.MOXICO.value),
        # Municípios da província de Namibe
        Municipality(name="Bibala", province=ProvinceData.NAMIBE.value),
        Municipality(name="Camulo", province=ProvinceData.NAMIBE.value),
        Municipality(name="Namibe", province=ProvinceData.NAMIBE.value),
        Municipality(name="Tômbua", province=ProvinceData.NAMIBE.value),
        Municipality(name="Virei", province=ProvinceData.NAMIBE.value),
        # Municípios da província de Uíge
        Municipality(name="Alto Cauale", province=ProvinceData.UIGE.value),
        Municipality(name="Ambuíla", province=ProvinceData.UIGE.value),
        Municipality(name="Bembe", province=ProvinceData.UIGE.value),
        Municipality(name="Buengas", province=ProvinceData.UIGE.value),
        Municipality(name="Bungo", province=ProvinceData.UIGE.value),
        Municipality(name="Damba", province=ProvinceData.UIGE.value),
        Municipality(name="Macocola", province=ProvinceData.UIGE.value),
        Municipality(name="Mucaba", province=ProvinceData.UIGE.value),
        Municipality(name="Negage", province=ProvinceData.UIGE.value),
        Municipality(name="Puri", province=ProvinceData.UIGE.value),
        Municipality(name="Quimbele", province=ProvinceData.UIGE.value),
        Municipality(name="Quitexe", province=ProvinceData.UIGE.value),
        Municipality(name="Sanza Pombo", province=ProvinceData.UIGE.value),
        Municipality(name="Songo", province=ProvinceData.UIGE.value),
        Municipality(name="Uíge", province=ProvinceData.UIGE.value),
        Municipality(name="Maquela do Zombo", province=ProvinceData.UIGE.value),
        # Municípios da província de Zaire
        Municipality(name="Cuimba", province=ProvinceData.ZAIRE.value),
        Municipality(name="M'banza-Kongo", province=ProvinceData.ZAIRE.value),
        Municipality(name="Noqui", province=ProvinceData.ZAIRE.value),
        Municipality(name="N'Zeto", province=ProvinceData.ZAIRE.value),
        Municipality(name="Soyo", province=ProvinceData.ZAIRE.value),
        Municipality(name="Tomboco", province=ProvinceData.ZAIRE.value),
    ]

    def get(data: Province):
        list = []
        for municipality in MunicipalityData.ALL.value:
            if municipality.province.name == data.name:
                municipality.province = data
                list.append(municipality)
        return list