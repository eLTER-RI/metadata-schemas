import React from "react";
import ReactDOM from "react-dom";

import {GeoLocationMap} from "./components";

const geoMapElement = document.getElementById("geo-map");
const geoLocationsRawString = geoMapElement.getAttribute('data-geo');
const geoLocationsJsonString = geoLocationsRawString.replace(/\\u0027/g, "\"").slice(1, -1);
const geoLocationsObject = JSON.parse(geoLocationsJsonString)

ReactDOM.render(
    <GeoLocationMap
        geoLocations={geoLocationsObject}
    />, geoMapElement
);
