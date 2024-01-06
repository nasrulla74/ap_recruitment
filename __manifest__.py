
{
    'name': 'Appeul Recruit Inherit',
    'version': '17.0.1.5.2',
    'summary': 'Appeul Recruit Inherit',
    'description': """Appeul Recruit Inherit""",
    'author': 'Appeul Services',
    'company': 'Appeul',
    'maintainer': 'Appeul Services',
    'category': 'Sales',
    'website': 'https://www.appeul.com',
    'sequence':"-1110",
    'depends': ['base','hr_recruitment'],
    'data': [
        'security/ir.model.access.csv',
        # 'data/sequence.xml',
        'views/recruit_inherit_view.xml',
        'views/xpat_worktype_view.xml',
        'views/header_footer_view.xml',
        'report/appointment_letter.xml',
        'report/im30.xml',
        'report/insurance_request.xml',
        'report/report.xml',
    ],

    'installable': True,
    'application': True,


    'license': 'LGPL-3',

}
