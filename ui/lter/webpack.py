from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    ".",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                "lter_search": "./js/lter/search/index.js",
                # "lter_detail": "./js/lter/detail/index.js",
                "lter_geomap": "./js/lter/geomap/index.js",
                "lter_deposit_form": "./js/lter/forms/index.js",
            },
            dependencies={
                "leaflet": "^1.9.4",
                "react-leaflet": "^2.1.4",
                "@oarepo/file-manager": "^1.1.0",
                "react-searchkit": "^2.0.0",
            },
            devDependencies={},
            aliases={
                "@js/lter": "./js/lter",
                # "@lter_detail": "js/lter/detail",
                "@lter_search": "js/lter/search",
                "@lter_geomap": "js/lter/geomap",
            },
        )
    },
)
