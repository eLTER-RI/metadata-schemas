from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    ".",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                "lter_search": "./js/lter/search/index.js",
                "lter_deposit_form": "./js/lter/forms/index.js",
            },
            dependencies={},
            devDependencies={},
            aliases={
                "@lter_search": "js/lter/search",
            },
        )
    },
)
