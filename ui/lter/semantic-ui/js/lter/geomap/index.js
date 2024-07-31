import React from "react";
import ReactDOM from "react-dom";

import {GeoLocationMap} from "./components";

const geoMapElement = document.getElementById("geo-map");
const geoDataAttr = geoMapElement.getAttribute('geoData');

const geoLocationTest = [
    {
        "description": "description of geolocation place",
        "point": {
            "longitude": 10.50,
            "latitude": 10.50
        }
    },
    {
        "description": "description of geolocation place",
        "box": {
            "westLongitude": 9.50,
            "eastLongitude": 10.50,
            "southLatitude": 9.50,
            "northLatitude": 10.50
        }
    },
    {
        "description": "description of geolocation place",
        "polygon": [
            {
                "points": [
                    {
                        "longitude": 10.50,
                        "latitude": 10.50
                    },
                    {
                        "longitude": 15.50,
                        "latitude": 15.50
                    },
                    {
                        "longitude": 12.50,
                        "latitude": 11.50
                    },
                    {
                        "longitude": 17.50,
                        "latitude": 17.50
                    }
                ],
                "inPolygonPoint": {
                    "longitude": 13.50,
                    "latitude": 13.50
                }
            }
        ]
    }
]

console.log(JSON.parse(geoDataAttr))
ReactDOM.render(
    <GeoLocationMap
        geoLocations={geoLocationTest}
    />,
    geoMapElement
);
