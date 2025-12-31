{
    'name': 'Gestion Cabinet Pédiatrique',
    'version': '1.0.0',
    'category': 'Healthcare',
    'summary': 'Module complet de gestion pour cabinet de pédiatrie',
    'description': """
        Module de gestion complète pour cabinet pédiatrique incluant :
        - Gestion des patients avec informations parents
        - Planning des rendez-vous intelligent
        - Consultations avec examens cliniques
        - Prescriptions avec calcul automatique des dosages
        - Facturation et gestion des paiements
        - Suivi vaccinal automatique
        - Courbes de croissance
        - Tableau de bord avec statistiques
        - Configuration entièrement paramétrable
        - Alertes et notifications automatiques
        - Rapports détaillés
    """,
    'author': 'Votre Cabinet',
    'website': 'https://www.votre-cabinet.fr',
    'depends': [
        'base',
        'mail',
        'calendar',
        'account',
        'contacts',
        'web',
        'report_xlsx'
    ],
    'data': [
        # Sécurité
        'security/ir.model.access.csv',
	'security/pediatric_security.xml',
        
        # Données de base
        'data/ir_sequence_data.xml',
        'data/pediatric_medication_data.xml',
        'data/pediatric_vaccine_data.xml',
        'data/pediatric_config_data.xml',
        'data/pediatric_cron_data.xml',
        
        # Vues
	'views/pediatric_growth_views.xml',
        'views/pediatric_patient_views.xml',
        'views/pediatric_appointment_views.xml',
        'views/pediatric_consultation_views.xml',
        'views/pediatric_prescription_views.xml',
        'views/pediatric_vaccination_views.xml',
        'views/pediatric_medication_views.xml',
        'views/pediatric_config_views.xml',
        'views/pediatric_dashboard_views.xml',
        'views/pediatric_menus.xml',
        
        # Rapports
        'reports/pediatric_prescription_report.xml',
        'reports/pediatric_patient_report.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'pediatric_management/static/src/css/pediatric_dashboard.css',
            'pediatric_management/static/src/js/pediatric_dashboard.js',
        ],
    },
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
    'images': ['static/description/icon.png'],
    'price': 0,
    'currency': 'EUR',
}