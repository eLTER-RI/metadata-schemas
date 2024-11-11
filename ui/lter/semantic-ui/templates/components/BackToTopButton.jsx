import React, {useEffect} from 'react';
import {Button, TransitionablePortal} from "semantic-ui-react";

export const BackToTopButton = () => {

    const [scrollToTopVisible, setScrollToTopVisible] = React.useState(false);


    const scrollToTop = () => {
        window.scrollTo({top: 0, behavior: "smooth"});
    };

    useEffect(() => {
        const handleScrollButtonVisibility = () => {
            window.scrollY > 300 ? setScrollToTopVisible(true) : setScrollToTopVisible(false);
            window.scroll
        };

        window.addEventListener("scroll", handleScrollButtonVisibility);

        return () => {
            window.removeEventListener("scroll", handleScrollButtonVisibility);
        };
    }, []);

    return (

        <TransitionablePortal
            open={scrollToTopVisible}
            transition={{animation: " fade up", duration: 300}}
        >
            <Button
                size="huge"
                onClick={scrollToTop}
                className="scroll-to-top-button"
                circular
                icon="chevron up"
            />
        </TransitionablePortal>

    );

}