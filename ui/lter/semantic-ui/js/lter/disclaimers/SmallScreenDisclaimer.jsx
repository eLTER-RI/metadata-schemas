import React, {useState, useEffect} from 'react';
import {Button, Modal} from "semantic-ui-react";


export const SmallScreenDisclaimer = () => {
    const [open, setOpen] = useState(false);

    useEffect(() => {
        const width = window.innerWidth;

        if (width < 768) {
            setOpen(true);
        }
    }, []);

    return (
        <Modal open={open} onClose={() => setOpen(false)} size="small">
            <Modal.Header>Small screen warning</Modal.Header>
            <Modal.Content>
                <p>Our website is designed to provide the best experience on larger screens, such as tablets and PCs.
                    While it's accessible on smaller devices, viewing it on a bigger screen ensures optimal readability
                    and
                    functionality.
                </p>
                <p><strong>For the best experience, consider switching to a larger device!</strong></p>
            </Modal.Content>
            <Modal.Actions>
                <Button onClick={() => setOpen(false)}>Ok</Button>
            </Modal.Actions>
        </Modal>
    );
};

SmallScreenDisclaimer.propTypes = {};