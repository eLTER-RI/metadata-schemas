export const useNavigateOutOfRouter = () => {
    return (path, replace) => {
        if (replace) {
            history.replaceState({}, "", path);
        } else {
            history.pushState({}, "", path);
        }

        history.go();
    };
};