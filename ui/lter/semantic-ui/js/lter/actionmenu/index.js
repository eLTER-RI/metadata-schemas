import React from "react";
import ReactDOM from "react-dom";

import {ActionMenu} from "./ActionMenu";

const actionMenu = document.getElementById("action-menu");
const draftId = actionMenu.getAttribute('draftId');
const state = actionMenu.getAttribute('state');
const isAdmin = actionMenu.getAttribute('isAdmin')

ReactDOM.render(
    <ActionMenu
        draftId={draftId}
        state={state}
        isAdmin
    />, actionMenu
);
