from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    ".",
    default="semantic-ui",
    themes={
        "semantic-ui": {
            "entry": {
                "branding": "./js/branding.js",
            },
            "dependencies": {
                "react-searchkit": "^2.0.0",
                "leaflet": "^1.9.4",
                "react-leaflet": "^2.1.4"
            },
            "devDependencies": {
                "leaflet": "^1.9.4",
                "react-leaflet": "^2.1.4",
            },
            "aliases": {
                "../../theme.config$": "less/theme.config",
                "../../less/site": "less/site",
                "../../less": "less",
                "@less": "less",
            },
        }
    },
)
