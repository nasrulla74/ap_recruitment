
{
    'name': 'Appeul Recruit Inherit 1.7.1',
    'version': '17.0.1.7.1',
    'summary': 'Appeul Recruit Inherit',
    'description': """Appeul Recruit Inherit""",
    'author': 'Appeul Services',
    'company': 'Appeul',
    'maintainer': 'Appeul Services',
    'category': 'Sales',
    'website': 'https://www.appeul.com',
    'sequence':"-1110",
    'depends': ['base','hr_recruitment', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'data/mail_template_data.xml',
        'data/cron_job.xml',
        # 'data/sequence.xml',
        'wizard/statement_wizard.xml',
        'views/recruit_inherit_view.xml',
        'views/xpat_worktype_view.xml',
        # 'views/rq_dashboard.xml',
        'views/header_footer_view.xml',
        'views/view_recruit_applicants.xml',
        'report/appointment_letter.xml',
        'report/offer_letter.xml',
        'report/appointment_letter_individual.xml',
        'report/im30.xml',
        'report/insurance_request.xml',
        'report/srilankan_embassy_domestic_agreement.xml',
        'report/srilankan_embassy_company_agreement.xml',
        'report/report.xml',
    ],

    'assets': {
            'web.assets_backend': [
                'ap_recruitment/static/src/components/**/*.js',
                'ap_recruitment/static/src/components/**/*.xml',
                'ap_recruitment/static/src/components/**/*.scss',
            ]
        },

    'installable': True,
    'application': True,


    'license': 'LGPL-3',

}
