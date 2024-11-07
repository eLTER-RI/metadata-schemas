export const useNavigation = () => {
    const navigateToUrl = (url, shouldReplace = false) => {
        if (shouldReplace) {
            history.replaceState({}, "", url);
        } else {
            history.pushState({}, "", url);
        }
        history.go();
    };

    const navigateBack = () => {
        history.back();
    };

    const getCurrentPath = () => window.location.pathname;

    const isOnPageWithPathPart = (pathPart) => {
        return window.location.pathname.includes(pathPart);
    }

    const reloadPage = () => {
        window.location.reload();
    }

    return {
        navigateToUrl,
        navigateBack,
        getCurrentPath,
        isOnPageWithPathPart,
        reloadPage
    };
};