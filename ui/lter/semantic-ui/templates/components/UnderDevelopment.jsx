import React from 'react';
import {Container, Header, Icon, Segment} from "semantic-ui-react";

const UnderDevelopment = () => {
    return (
        <Container
            textAlign="center"
            style={{
                margin: "1rem",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
            }}
        >
            <Segment padded="very">
                <Icon name="wrench" size="huge" color="blue"/>
                <Header as="h1">Page Under Development</Header>
                <p>You are using a development system of the emerging eLTER Research Infrastructure (RI).Please note
                    that this service is still under construction and may not yet be fully functional.</p>
                <Icon name="spinner" size="big" loading/>
            </Segment>
        </Container>
    );
};

export default UnderDevelopment;
