import React from "react";
import PropTypes from "prop-types";
import {withState} from "react-searchkit";
import {i18next} from "@translations/oarepo_ui/i18next";
import {Grid, Icon, Input, Popup} from "semantic-ui-react";

const SearchBarElement = withState(
    ({
         queryString,
         onInputChange,
         updateQueryState,
         currentQueryState,
         iconName,
         iconColor,
         placeholder: passedPlaceholder,
     }) => {
        const placeholder = passedPlaceholder || i18next.t("Search");

        const onSearch = () => {
            updateQueryState({...currentQueryState, queryString});
        };
        const onBtnSearchClick = () => {
            onSearch();
        };
        const onKeyPress = (event) => {
            if (event.key === "Enter") {
                onSearch();
            }
        };

        const clearInput = () => {
            onInputChange("");
            updateQueryState({...currentQueryState, queryString: ""});
        };

        return (
            <Grid.Row>
                <Input
                    icon={
                        queryString && (
                            <Popup content="Clear search" trigger={
                                <Icon
                                    color="red"
                                    name="delete"
                                    link
                                    onClick={clearInput}
                                    aria-label={i18next.t("Clear search")}
                                />}/>
                        )
                    }
                    iconPosition="left"
                    action={{
                        icon: iconName,
                        onClick: onBtnSearchClick,
                        "aria-label": i18next.t("Search"),
                        className: "search"
                    }}
                    placeholder={placeholder}
                    aria-label={placeholder}
                    onChange={(event, {value}) => {
                        onInputChange(value);
                    }}
                    value={queryString}
                    onKeyPress={onKeyPress}
                    style={{ width: "50%" }}
                    className="search-input"
                />
            </Grid.Row>

        );
    }
);

SearchBarElement.propTypes = {
    placeholder: PropTypes.string,
    queryString: PropTypes.string,
    onInputChange: PropTypes.func,
    updateQueryState: PropTypes.func,
    currentQueryState: PropTypes.object,
    iconName: PropTypes.string,
    iconColor: PropTypes.string,
};

SearchBarElement.defaultProps = {
    placeholder: i18next.t("Search"),
    iconName: "search",
    iconColor: "green",
};

export default SearchBarElement;
