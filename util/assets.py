from flask_assets import Bundle

bundles = {
    'home_css': Bundle(
        'css/home.scss',
        filters='libsass',
        depends='css/*.scss',
        output='gen/home.%(version)s.css'
    ),
}