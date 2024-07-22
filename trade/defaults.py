class Defaults:
    """Default values used in the trade-legacy"""

    # Period of time used to update data on the dashboard
    # update_time = 60*1000 # in milliseconds
    update_time = 5*1000  # in milliseconds

    # Maximum number of requests the user can make on the dashboard
    max_requests = 10

    # Initial money the user has
    initial_money = 100000

    # Path to the data folder
    data_path = "../data"

    # News settings
    api_key = "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"


    # Stocks and Indexes used in the interface
    # They are also used to download data with the download_market_data setup tool
    # The key is the ticker and the value is the name of the company, the activity and a boolean to know if the company has charts
    # So the data provided in the data folder must have the same name as the symbol
    companies_list = {
        "MC.PA": {
            "label": "LVMH MOËT HENNESSY LOUIS VUITTON SE (MC)",
            "activity": "Textile Habillement Accessoires",
            "got_charts": False,
        },
        "OR.PA": {
            "label": "L'ORÉAL (OR)",
            "activity": "Chimie Pharmacie Cosmétiques",
            "got_charts": False,
        },
        "RMS.PA": {
            "label": "HERMÈS INTERNATIONAL (RMS)",
            "activity": "Textile Habillement Accessoires",
            "got_charts": False,
        },
        "TTE.PA": {
            "label": "TOTALENERGIES SE (TTE)",
            "activity": "Energie et Produits de base",
            "got_charts": False,
        },
        "SAN.PA": {
            "label": "SANOFI (SAN)",
            "activity": "Chimie Pharmacie Cosmétiques",
            "got_charts": False,
        },
        "AIR.PA": {
            "label": "AIRBUS SE (AIR)",
            "activity": "Aéronautique Espace Armement",
            "got_charts": False,
        },
        "SU.PA": {
            "label": "SCHNEIDER ELECTRIC SE (SU)",
            "activity": "Electricité Electronique",
            "got_charts": False,
        },
        "AI.PA": {
            "label": "AIR LIQUIDE (AI)",
            "activity": "Energie et Produits de base",
            "got_charts": False,
        },
        "EL.PA": {
            "label": "ESSILORLUXOTTICA (EL)",
            "activity": "Biens d'équipement domestique",
            "got_charts": False,
        },
        "BNP.PA": {
            "label": "BNP PARIBAS (BNP)",
            "activity": "Banque",
            "got_charts": False,
        },
        "KER.PA": {
            "label": "KERING (KER)",
            "activity": "Textile Habillement Accessoires",
            "got_charts": False,
        },
        "DG.PA": {
            "label": "VINCI (DG)",
            "activity": "BTP Génie Civil",
            "got_charts": False,
        },
        "CS.PA": {
            "label": "AXA (CS)",
            "activity": "Banque",
            "got_charts": False,
        },
        "SAF.PA": {
            "label": "SAFRAN (SAF)",
            "activity": "Electricité Electronique",
            "got_charts": False,
        },
        "RI.PA": {
            "label": "PERNOD RICARD (RI)",
            "activity": "Agroalimentaire",
            "got_charts": False,
        },
        "DSY.PA": {
            "label": "DASSAULT SYSTÈMES SE (DSY)",
            "activity": "Services informatiques",
            "got_charts": False,
        },
        "STLAM.MI": {
            "label": "STELLANTIS N.V. (STLAM)",
            "activity": "Automobile",
            "got_charts": False,
        },
        "BN.PA": {
            "label": "DANONE (BN)",
            "activity": "Agroalimentaire",
            "got_charts": False,
        },
        "STMPA.PA": {
            "label": "STMICROELECTRONICS N.V. (STMPA)",
            "activity": "Electricité Electronique",
            "got_charts": False,
        },
        "ACA.PA": {
            "label": "CRÉDIT AGRICOLE S.A. (ACA)",
            "activity": "Banque",
            "got_charts": False,
        },
        "^GSPC": {
            "label": "S&P 500",
            "activity": "Indice",
            "got_charts": False,
        },
        "^DJI": {
            "label": "Dow Jones Industrial Average",
            "activity": "Indice",
            "got_charts": False,
        },
        "^FCHI": {
            "label": "CAC 40",
            "activity": "Indice",
            "got_charts": False,
        },
        "^SPGSGC": {
            "label": "S&P GSCI Gold Index",
            "activity": "Indice",
            "got_charts": False,
        }
    }

    activities = {
        "Energie et Produits de base": [ "TTE.PA", "AI.PA" ],
        "Services informatiques": [ "DSY.PA" ],
        "Communication Médias Multimédias": [],
        "Electricité Electronique": [ "SU.PA", "SAF.PA", "STMPA.PA" ],
        "Chimie Pharmacie Cosmétiques": [ "SAN.PA", "OR.PA" ],
        "Autres biens d'équipement": [],
        "Autres services": [],
        "Aéronautique Espace Armement": [ "AIR.PA", "AIR.PA" ],
        "Environnement et Services aux collectivités": [],
        "Automobile": [ "STLAM.MI" ],
        "SIIC": [],
        "Textile Habillement Accessoires": [ "MC.PA", "RMS.PA", "KER.PA" ],
        "Ingénierie": [],
        "Biotechnologie": [],
        "Equipement automobile": [],
        "Télécommunication": [],
        "Agroalimentaire": [ "RI.PA", "BN.PA" ],
        "Banque": ["BNP.PA", "CS.PA", "ACA.PA"],
        "Loisirs, équipements de loisirs": [],
        "Hôtellerie Restauration Tourisme": [],
        "Transport Stockage": [],
        "Distribution générale grand public": [],
        "BTP Génie Civil": [ "DG.PA" ],
        "Biens d'équipement domestique": [ "EL.PA" ],
        "Transformation des métaux": [],
        "Société de portefeuille": [],
        "Conglomérat": [],
        "Matériaux de construction": [],
        "Assurances": [],
        "Services financiers": [],
        "Distribution spécialisée": [],
        "Holding": [],
        "Immobilier": [],
        "Distribution industrielle": [],
        "Construction mécanique": [],
        "Emballage": [],
        "Biens de consommation non durables": [],
        "Internet": [],
        "Nanotechnologie": [],
        "Indice": [ "^GSPC", "^DJI", "^FCHI", "^SPGSGC" ],
    }

# Provide the default values in global scope
defaults = Defaults()