import React from "react";
import ReactDOM from "react-dom";

import {ActionMenu} from "./ActionMenu";

const actionMenu = document.getElementById("action-menu");
const draftId = actionMenu.getAttribute('draftId');
const state = actionMenu.getAttribute('state');
const isAdmin = actionMenu.getAttribute('isAdmin') === 'true'

ReactDOM.render(
    <ActionMenu
        draftId={draftId}
        state={state}
        isAdmin={isAdmin}
    />, actionMenu
);
