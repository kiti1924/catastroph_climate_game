from os import environ

SESSION_CONFIGS = [
    dict(
        name='ccg',
        app_sequence=["tutorial",'ccg',"survey","payment_info"],
        num_demo_participants=5,
    ),
    dict(
        name='tutorial', app_sequence=['tutorial'], num_demo_participants=1
    ),
    dict(
        name='survey', app_sequence=['survey'], num_demo_participants=1
    ),
    dict(
        name='payment_info', app_sequence=['payment_info'], num_demo_participants=1
    ),
    
]

ROOMS = [
        dict(
        name='free',
        display_name='自由入力',
    ),
    dict(
        name='system',
        display_name='40人(1-40)',
        participant_label_file='_rooms/system.txt',
        use_secure_urls=True
    ),
    dict(
        name='human',
        display_name='100人(1-100)',
        participant_label_file='_rooms/human.txt',
        use_secure_urls=True
    ),
    dict(
        name='humancounter',
        display_name='1000人(1-1000)',
        participant_label_file='_rooms/humancounter.txt',
        use_secure_urls=True
    ),
]
# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=10.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ["is_dropout", "Final_BLACK", "Final_RED", "Final_CONTRIBUTION", "Final_REWARD", "Final_REWARD_JPY", "hit_estimate"]
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ja'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'JPY'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '3672880940814'


